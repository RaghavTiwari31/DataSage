import pandas as pd
import numpy as np

def load_data(filepath):
    """Load Excel file into a pandas DataFrame."""
    print(f"📥 Loading file: {filepath}")
    df = pd.read_excel(filepath)
    print(f"✅ Loaded {len(df)} rows and {len(df.columns)} columns")
    return df

def clean_data(df: pd.DataFrame, config: dict) -> pd.DataFrame:
    """Clean the dataset based on config rules."""
    print("🧹 Starting data cleaning...")

    # Drop duplicates
    if config.get("drop_duplicates", True):
        before = len(df)
        df = df.drop_duplicates()
        after = len(df)
        print(f"🔁 Removed {before - after} duplicate rows")

    # Handle missing values
    fill_cfg = config.get("fill_missing", {})
    strategy = fill_cfg.get("strategy", "median")
    threshold = fill_cfg.get("threshold", 0.3)

    # Drop rows if too many missing values
    row_threshold = int(threshold * df.shape[1])
    before = len(df)
    df = df.dropna(thresh=row_threshold)
    after = len(df)
    print(f"⚖️ Dropped {before - after} rows with too many missing values")

    # Fill remaining missing values
    for col in df.columns:
        if df[col].isna().any():
            if df[col].dtype in [np.float64, np.int64]:
                if strategy == "mean":
                    value = df[col].mean()
                else:  # default to median
                    value = df[col].median()
                df[col] = df[col].fillna(value)
                print(f"📊 Filled NaNs in numeric column '{col}' with {strategy} ({value:.2f})")
            else:
                df[col] = df[col].fillna("Unknown")
                print(f"📝 Filled NaNs in text column '{col}' with 'Unknown'")

    # Standardize text columns
    text_std = config.get("text_standardization", "title")
    for col in df.select_dtypes(include=["object"]).columns:
        if text_std == "lower":
            df[col] = df[col].str.lower()
        elif text_std == "upper":
            df[col] = df[col].str.upper()
        elif text_std == "title":
            df[col] = df[col].str.title()

    # Fix date columns
    # Default date format (global fallback)
    default_date_fmt = config.get("date_format", "%Y-%m-%d")

    # Get column-specific date configs if defined
    date_columns_config = config.get("date_columns", [])

    # Convert date columns
    for col in df.columns:
        if "date" in col.lower():
            # Look up specific format for this column if defined
            col_config = next((c for c in date_columns_config if c.get("name") == col), {})
            date_fmt = col_config.get("format", default_date_fmt)

            try:
                df[col] = pd.to_datetime(df[col], errors="coerce", format=date_fmt).dt.strftime(default_date_fmt)
                print(f"📅 Standardized '{col}' to format {default_date_fmt}")
            except Exception as e:
                print(f"⚠️ Could not standardize '{col}': {e}")


    print("✅ Cleaning complete")
    return df
