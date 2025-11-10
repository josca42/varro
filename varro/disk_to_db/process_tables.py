import pandas as pd
import numpy as np


STANDARD_COLS = ["indhold", "tid", "alder", "kon"]
DIM_COLS = ["kode", "niveau", "titel"]


def process_fact_table(df: pd.DataFrame) -> pd.DataFrame:
    df = normalize_column_names(df)
    df = process_tid_col(df)
    df = remove_total_rows(df)
    df = process_alder_col(df)
    df = process_indhold_col(df)
    return df


def process_dim_table(df: pd.DataFrame) -> pd.DataFrame:
    df = normalize_column_names(df)
    df = process_kode_col(df)
    df = df[DIM_COLS].copy()
    return df


def process_kode_col(df: pd.DataFrame) -> pd.DataFrame:
    if df["KODE"].dtype == "object":
        try:
            df["KODE_INT"] = df["KODE"].str.replace(".", "").astype(int)
            for group, df_group in df.groupby("NIVEAU"):
                if df_group["KODE"].nunique() != df_group["KODE_INT"].nunique():
                    raise ValueError(f"Kode column is not unique for level {group}")
            df["KODE"] = df["KODE_INT"]
            return df
        except ValueError:
            pass
    return df[["KODE", "NIVEAU", "TITEL"]]


def process_tid_col(df: pd.DataFrame) -> pd.DataFrame:
    if "tid" in df.columns:
        if df["tid"].dtype == "object":
            if "K" in df["tid"].iloc[0]:
                df["tid"] = pd.to_datetime(df["tid"].str.replace("K", "Q"))
            elif "M" in df["tid"].iloc[0]:
                df["tid"] = pd.to_datetime(df["tid"], format="%YM%m")
            else:
                raise ValueError(f"Unknown TID format: {df['TID'].iloc[0]}")
        else:
            assert 1800 < df["tid"].iloc[0] < 2150, "Not a year column"
            df["tid"] = pd.to_datetime(df["tid"], format="%Y")

        df["tid"] = df["tid"].dt.date
    return df


def remove_total_rows(df: pd.DataFrame) -> pd.DataFrame:
    for col in df.columns:
        if col in ["indhold", "tid"]:
            continue

        if df[col].dtype == "object":
            df = df[~df[col].isin(["TOT", "IALT"])].copy()
    return df


def process_alder_col(df: pd.DataFrame) -> pd.DataFrame:
    if "alder" in df.columns:
        if df["alder"].dtype == "object":
            # Check if object do to upper open ended i.e. "99-"
            if sum(["-" in v for v in df["alder"].unique()]) < 2:
                df["alder"] = df["alder"].str.replace("-", "").astype(int)
            else:
                df["alder"] = df["alder"].map(to_int4range_text)
    return df


def process_indhold_col(df: pd.DataFrame) -> pd.DataFrame:
    if "indhold" in df.columns:
        if df["indhold"].dtype == "object":
            if sum(df["indhold"] == "..") > 0:
                df.loc[df["indhold"] == "..", "indhold"] = np.nan
                df["indhold"] = df["indhold"].str.replace(",", ".").astype(float)
    return df


def to_int4range_text(s: str) -> str:
    s = s.strip()
    lo_str, hi_str = s.split("-", 1)  # expect exactly one dash
    lo = int(lo_str.strip())

    hi_str = hi_str.strip()
    if hi_str == "":  # e.g. "100-"
        return f"[{lo},)"

    hi = int(hi_str)  # inclusive upper → make exclusive
    return f"[{lo},{hi + 1})"


def normalize_column_names(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = [
        c.replace("å", "a").replace("ø", "o").replace("æ", "ae")
        for c in df.columns.str.lower()
    ]
    return df


def check_if_dim_fits_fact_col(df_fact, df_dim, fact_col):
    diff = set(df_fact[fact_col].unique()) - set(df_dim["kode"].values)

    if len(diff) > 0:
        df_dim["kode"]

    if diff == set():
        return df_fact
    elif diff == {0}:
        df_fact[df_fact[fact_col] != 0]
        return df_fact
    else:
        missing_values = ", ".join([str(int(v)) for v in diff])
        raise ValueError(
            f"Following values in fact column {fact_col} are not in dimension table: {missing_values}"
        )
