import pandas as pd


def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Fill missing values
    df.fillna(0, inplace=True)

    # Encode categorical
    if "gender" in df.columns:
        df["gender"] = df["gender"].map({"M": 1, "F": 0}).fillna(0)

    return df