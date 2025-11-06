import pandas as pd
import numpy as np


def process_fact_table(df: pd.DataFrame) -> pd.DataFrame:
    df = process_tid_col(df)
    df = remove_total_rows(df)
    df = process_alder_col(df)
    df = process_indhold_col(df)
    return df


def process_tid_col(df: pd.DataFrame) -> pd.DataFrame:
    if "TID" in df.columns:
        if df["TID"].dtype == "object":
            if "K" in df["TID"].iloc[0]:
                df["TID"] = pd.to_datetime(df["TID"].str.replace("K", "Q"))
            elif "M" in df["TID"].iloc[0]:
                df["TID"] = pd.to_datetime(df["TID"], format="%YM%m")
            else:
                raise ValueError(f"Unknown TID format: {df['TID'].iloc[0]}")
        else:
            assert 1800 < df["TID"].iloc[0] < 2150, "Not a year column"
            df["TID"] = pd.to_datetime(df["TID"], format="%Y")

        df["TID"] = df["TID"].dt.date
    return df


def remove_total_rows(df: pd.DataFrame) -> pd.DataFrame:
    for col in df.columns:
        if col in ["INDHOLD", "TID"]:
            continue

        if df[col].dtype == "object":
            df = df[~df[col].isin(["TOT", "IALT"])].copy()
    return df


def process_alder_col(df: pd.DataFrame) -> pd.DataFrame:
    if "ALDER" in df.columns:
        if df["ALDER"].dtype == "object":
            # Check if object do to upper open ended i.e. "99-"
            if sum(["-" in v for v in df["ALDER"].unique()]) < 2:
                df["ALDER"] = df["ALDER"].str.replace("-", "").astype(int)
            else:
                df["ALDER"] = df["ALDER"].map(to_int4range_text)
    return df


def process_indhold_col(df: pd.DataFrame) -> pd.DataFrame:
    if "INDHOLD" in df.columns:
        if df["INDHOLD"].dtype == "object":
            if sum(df["INDHOLD"] == "..") > 0:
                df.loc[df["INDHOLD"] == "..", "INDHOLD"] = np.nan
                df["INDHOLD"] = df["INDHOLD"].str.replace(",", ".").astype(float)
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
