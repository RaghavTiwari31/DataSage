import os
import base64
from io import BytesIO
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def _fig_to_base64(fig) -> str:
    """
    Convert a matplotlib figure to a base64 string.
    """
    buf = BytesIO()
    fig.savefig(buf, format="png", bbox_inches="tight", facecolor=fig.get_facecolor())
    buf.seek(0)
    img_b64 = base64.b64encode(buf.read()).decode("utf-8")
    plt.close(fig)
    return img_b64

# def generate_visuals(df: pd.DataFrame, output_dir: str) -> dict:
#     print("📈 Generating visualizations...")
#     figs = {}
#     os.makedirs(output_dir, exist_ok=True)

#     # Apply dark style
#     plt.style.use('dark_background')
#     sns.set_style("darkgrid")

#     # 1. Missing values heatmap
#     if df.isnull().sum().sum() > 0:
#         fig, ax = plt.subplots(figsize=(8, 5))
#         sns.heatmap(df.isnull(), cbar=False, cmap="viridis", ax=ax)
#         ax.set_title("Missing Values Heatmap", color='white')
#         path = os.path.join(output_dir, "missing_values.png")
#         fig.savefig(path, facecolor=fig.get_facecolor())
#         figs["missing_values"] = _fig_to_base64(fig)

#     # 2. Correlation heatmap
#     numeric_df = df.select_dtypes(include=["number"])
#     if not numeric_df.empty:
#         fig, ax = plt.subplots(figsize=(8, 6))
#         sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", ax=ax)
#         ax.set_title("Correlation Heatmap", color='white')
#         path = os.path.join(output_dir, "correlation_matrix.png")
#         fig.savefig(path, facecolor=fig.get_facecolor())
#         figs["correlation_matrix"] = _fig_to_base64(fig)

#     # 3. Distribution plots for first 3 numeric columns
#     for col in numeric_df.columns[:3]:
#         fig, ax = plt.subplots(figsize=(6, 4))
#         sns.histplot(numeric_df[col], kde=True, bins=30, color="#1f77b4", ax=ax)
#         ax.set_title(f"Distribution of {col}", color='white')
#         path = os.path.join(output_dir, f"dist_{col}.png")
#         fig.savefig(path, facecolor=fig.get_facecolor())
#         figs[f"dist_{col}"] = _fig_to_base64(fig)

#     # 4. Bar plot of first categorical column frequencies
#     cat_df = df.select_dtypes(include=["object"])
#     if not cat_df.empty:
#         col = cat_df.columns[0]
#         fig, ax = plt.subplots(figsize=(7, 4))
#         df[col].value_counts().plot(kind="bar", color="#ff7f0e", ax=ax)
#         ax.set_title(f"Frequency of {col}", color='white')
#         path = os.path.join(output_dir, f"freq_{col}.png")
#         fig.savefig(path, facecolor=fig.get_facecolor())
#         figs[f"freq_{col}"] = _fig_to_base64(fig)

#     print(f"✅ Generated {len(figs)} figures")
#     return figs

import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def generate_visuals(df: pd.DataFrame, output_dir: str) -> dict:
    print("📈 Generating visualizations...")
    figs = {}
    os.makedirs(output_dir, exist_ok=True)

    # Apply dark style
    plt.style.use('dark_background')
    sns.set_style("darkgrid")

    # 1. Missing values heatmap
    if df.isnull().sum().sum() > 0:
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.heatmap(df.isnull(), cbar=False, cmap="viridis", ax=ax)
        ax.set_title("Missing Values Heatmap", color='white')
        path = os.path.join(output_dir, "missing_values.png")
        fig.savefig(path, facecolor=fig.get_facecolor())
        figs["missing_values"] = _fig_to_base64(fig)
        plt.close(fig)

    # 2. Correlation heatmap
    numeric_df = df.select_dtypes(include=["number"])
    if not numeric_df.empty and numeric_df.shape[1] > 1:
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", ax=ax)
        ax.set_title("Correlation Heatmap", color='white')
        path = os.path.join(output_dir, "correlation_matrix.png")
        fig.savefig(path, facecolor=fig.get_facecolor())
        figs["correlation_matrix"] = _fig_to_base64(fig)
        plt.close(fig)

    # 3. Distribution plots for numeric columns (max 3)
    if not numeric_df.empty:
        for col in numeric_df.columns[:3]:
            if df[col].dropna().empty:  # Skip if all NaN
                print(f"⚠️ Skipping {col} (no valid numeric data)")
                continue
            fig, ax = plt.subplots(figsize=(6, 4))
            sns.histplot(numeric_df[col].dropna(), kde=True, bins=30, color="#1f77b4", ax=ax)
            ax.set_title(f"Distribution of {col}", color='white')
            path = os.path.join(output_dir, f"dist_{col}.png")
            fig.savefig(path, facecolor=fig.get_facecolor())
            figs[f"dist_{col}"] = _fig_to_base64(fig)
            plt.close(fig)

    # 4. Bar plot for first categorical column
    cat_df = df.select_dtypes(include=["object", "category"])
    if not cat_df.empty:
        col = cat_df.columns[0]
        if df[col].dropna().empty:  # Skip if empty
            print(f"⚠️ Skipping {col} (no categorical values)")
        else:
            fig, ax = plt.subplots(figsize=(7, 4))
            df[col].value_counts().plot(kind="bar", color="#ff7f0e", ax=ax)
            ax.set_title(f"Frequency of {col}", color='white')
            path = os.path.join(output_dir, f"freq_{col}.png")
            fig.savefig(path, facecolor=fig.get_facecolor())
            figs[f"freq_{col}"] = _fig_to_base64(fig)
            plt.close(fig)

    print(f"✅ Generated {len(figs)} figures successfully")
    return figs

