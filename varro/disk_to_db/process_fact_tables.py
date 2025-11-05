import pandas as pd


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
            # TODO: Implement this
            pass
    return df
