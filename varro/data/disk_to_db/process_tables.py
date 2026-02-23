import pandas as pd
import numpy as np


STANDARD_COLS = ["indhold", "tid", "alder", "kon"]
DIM_COLS = ["kode", "niveau", "titel", "parent_kode"]


def process_fact_table(df: pd.DataFrame) -> pd.DataFrame:
    df = normalize_column_names(df)
    # df = remove_total_rows(df)
    df = process_tid_col(df)
    df = process_alder_col(df)
    df = process_indhold_col(df)
    df = df[df["indhold"].notna()].copy()  # Remove empty rows
    return df


def process_dim_table(df: pd.DataFrame) -> pd.DataFrame:
    df = normalize_column_names(df)
    df = process_kode_col(df)
    df = add_parent_kode_col(df)
    df = df[DIM_COLS].copy()
    return df


# def remove_total_rows(df: pd.DataFrame) -> pd.DataFrame:
#     for col in df.columns:
#         if col in ["indhold", "tid"]:
#             continue

#         if df[col].dtype == "object":
#             df = df[~df[col].isin(["TOT", "IALT", "TOTR"])].copy()

#     return df


def process_kode_col(df: pd.DataFrame) -> pd.DataFrame:
    if df["kode"].dtype == "object":
        try:
            df["kode_int"] = df["kode"].str.replace(".", "", regex=False).astype(int)
            for group, df_group in df.groupby("niveau"):
                if df_group["kode"].nunique() != df_group["kode_int"].nunique():
                    raise ValueError(f"Kode column is not unique for level {group}")
            df["kode"] = df["kode_int"]
            return df
        except ValueError as e:
            print(f"Kode not converted to int: {e}")
            pass
    return df


def add_parent_kode_col(df: pd.DataFrame) -> pd.DataFrame:
    if "sekvens" in df.columns:
        df = df.sort_values("sekvens", kind="stable").copy()
    else:
        df = df.copy()

    stack = {}
    parent_values = []
    for niveau, kode in df[["niveau", "kode"]].itertuples(index=False):
        niveau = int(niveau)
        parent_values.append(stack.get(niveau - 1) if niveau > 1 else None)
        stack[niveau] = kode
        for level in tuple(stack):
            if level > niveau:
                del stack[level]

    if pd.api.types.is_integer_dtype(df["kode"]):
        df["parent_kode"] = pd.Series(parent_values, index=df.index, dtype="Int64")
    else:
        df["parent_kode"] = pd.Series(parent_values, index=df.index)
    return df


def process_tid_col(df: pd.DataFrame) -> pd.DataFrame:
    if "tid" in df.columns:
        if df["tid"].dtype == "object":
            tid_sample = str(df["tid"].dropna().iloc[0])
            if "K" in tid_sample:
                df["tid"] = pd.to_datetime(df["tid"].str.replace("K", "Q"))
            elif "M" in tid_sample and "D" in tid_sample:
                df["tid"] = pd.to_datetime(df["tid"], format="%YM%mD%d")
            elif "H" in tid_sample:
                df["tid"] = df["tid"].map(parse_half_year)
            elif "M" in tid_sample:
                df["tid"] = pd.to_datetime(df["tid"], format="%YM%m")
            elif ":" in tid_sample:
                df["tid"] = df["tid"].str.replace(":", "-").map(to_int4range_text)
            else:
                pass
        else:
            assert 1700 < df["tid"].iloc[0] < 2150, "Not a year column"
            df["tid"] = pd.to_datetime(df["tid"], format="%Y")

        if df["tid"].dtype != "object":
            df["tid"] = df["tid"].dt.date
    return df


def process_alder_col(df: pd.DataFrame) -> pd.DataFrame:
    if "alder" in df.columns:
        if df["alder"].dtype == "object":
            try:
                # Check if object do to upper open ended i.e. "99-"
                if sum(["-" in v for v in df["alder"].unique()]) < 2:
                    df["alder"] = df["alder"].str.replace("-", "").astype(int)
                else:
                    df["alder"] = df["alder"].map(to_int4range_text)
            except:
                pass
        else:
            if df["alder"].max() > 1_000:
                df["alder"] = df["alder"].astype(str)
                # raise ValueError(
                #     f"Alder column has values greater than 1000: {df['alder'].max()}"
                # )

    return df


def process_indhold_col(df: pd.DataFrame) -> pd.DataFrame:
    if "indhold" in df.columns:
        if df["indhold"].dtype == "object":
            if sum(df["indhold"] == "..") > 0:
                df.loc[df["indhold"] == "..", "indhold"] = np.nan
                df["indhold"] = df["indhold"].str.replace(",", ".").astype(float)
    return df


def to_int4range_text(s: str) -> str:
    s = s.strip().replace("OV", "-")
    lo_str, hi_str = s.split("-", 1)  # expect exactly one dash
    lo = int(lo_str.strip())

    hi_str = hi_str.strip()
    if hi_str == "":  # e.g. "100-"
        return f"[{lo},)"

    hi = int(hi_str)  # inclusive upper → make exclusive
    assert lo < hi + 1, "upper bound is less than lower bound"
    return f"[{lo},{hi + 1})"


def parse_half_year(value: str) -> pd.Timestamp:
    year_str, half_str = str(value).split("H", 1)
    half = int(half_str)
    if half == 1:
        month = 1
    elif half == 2:
        month = 7
    else:
        raise ValueError(f"Unknown half-year: {value}")
    return pd.Timestamp(int(year_str), month, 1)


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
