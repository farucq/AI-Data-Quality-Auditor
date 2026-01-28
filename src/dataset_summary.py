import pandas as pd

def dataset_summary(df: pd.DataFrame) -> dict:
    return {
        "shape": df.shape,
        "missing_percentage": df.isnull().mean() * 100,
        "dtypes": df.dtypes
    }
