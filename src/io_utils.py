import pandas as pd


def load_excel(path: str) -> pd.DataFrame:
    """Load an Excel file into a pandas DataFrame."""
    try:
        df = pd.read_excel(path)
        print(f"📥 Loaded file: {path} with {df.shape[0]} rows and {df.shape[1]} columns")
        return df
    except Exception as e:
        print(f"❌ Error loading Excel file: {e}")
        raise


def save_excel(df: pd.DataFrame, path: str):
    """Save a pandas DataFrame to an Excel file."""
    try:
        df.to_excel(path, index=False)
        print(f"💾 Saved Excel file: {path}")
    except Exception as e:
        print(f"❌ Error saving Excel file: {e}")
        raise
