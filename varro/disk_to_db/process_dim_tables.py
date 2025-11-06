import pandas as pd


def process_kode_col(df: pd.DataFrame) -> pd.DataFrame:
    if df["KODE"].dtype == "object":
        n_unique = df["KODE"].nunique()
        kode_as_int = df["KODE"].str.replace(".", "").astype(int)
        if n_unique == kode_as_int.nunique():
            df["KODE"] = kode_as_int

    return df
