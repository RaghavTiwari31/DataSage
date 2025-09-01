import pandas as pd
import numpy as np
from scipy import stats


def detect_anomalies(df: pd.DataFrame, z_thresh: float = 3.0) -> dict:
    """
    Detect anomalies in numeric columns using Z-score method.
    Returns a dictionary with column name -> list of anomalies.
    """
    print("📊 Starting anomaly detection...")
    anomalies = {}

    numeric_cols = df.select_dtypes(include=[np.number]).columns
    for col in numeric_cols:
        try:
            z_scores = np.abs(stats.zscore(df[col].dropna()))
            outliers = df[col][(z_scores > z_thresh)]
            if not outliers.empty:
                anomalies[col] = outliers.tolist()
                print(f"⚠️ Found {len(outliers)} anomalies in '{col}'")
        except Exception as e:
            print(f"⚠️ Could not compute anomalies for '{col}': {e}")

    if not anomalies:
        print("✅ No anomalies detected")

    return anomalies
