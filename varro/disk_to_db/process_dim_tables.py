import pandas as pd


def process_kode_col(df: pd.DataFrame) -> pd.DataFrame:
    if df["kode"].dtype == "object":
        n_unique = df["kode"].nunique()
        kode_as_int = df["kode"].str.replace(".", "").astype(int)
        if n_unique == kode_as_int.nunique():
            df["kode"] = kode_as_int

    return df


def check_if_dim_fits_fact_col(df_fact, df_dim, fact_col):
    diff = set(df_fact[fact_col].unique()) - set(df_dim["kode"].values)
    if diff == set():
        return df_fact
    elif diff == {0}:
        df_fact[df_fact[fact_col] != 0]
        return df_fact
    else:
        raise ValueError(f"Diff: {diff}")
