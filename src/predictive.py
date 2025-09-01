import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import base64
import io

def _fig_to_base64():
    """Helper: Convert matplotlib figure to base64 string."""
    buf = io.BytesIO()
    plt.savefig(buf, format="png", bbox_inches="tight")
    plt.close()
    buf.seek(0)
    return base64.b64encode(buf.read()).decode("utf-8")

def run_predictive_models(df: pd.DataFrame) -> dict:
    insights = {}

    # --- Example 1: Salary prediction ---
    if "Experience" in df.columns and "Salary" in df.columns:
        valid = df.dropna(subset=["Experience", "Salary"])
        if not valid.empty:
            X = valid[["Experience"]]
            y = valid["Salary"]

            model = LinearRegression()
            model.fit(X, y)
            coef = model.coef_[0]
            intercept = model.intercept_

            formula = f"Salary = {coef:.2f} * Experience + {intercept:.2f}"
            interpretation = (
                f"Each additional year of experience increases salary by ≈ {coef:.2f} units. "
                f"Base salary starts around {intercept:.2f} when experience is zero."
            )

            insights["salary_prediction"] = {
                "formula": formula,
                "interpretation": interpretation
            }

    # --- Example 2: Clustering ---
    numeric_df = df.select_dtypes(include="number").dropna()
    if numeric_df.shape[1] >= 2:
        kmeans = KMeans(n_clusters=3, n_init="auto", random_state=42)
        clusters = kmeans.fit_predict(numeric_df)

        cluster_info = f"Identified {len(set(clusters))} clusters in the dataset"
        interpretation = (
            "These clusters represent groups of employees/customers with similar numeric patterns. "
            "For example, they may indicate low, medium, and high salary ranges or other natural groupings."
        )

        # --- Visualization ---
        plt.figure(figsize=(6, 5))
        plt.scatter(
            numeric_df.iloc[:, 0], numeric_df.iloc[:, 1],
            c=clusters, cmap="viridis", marker="o", alpha=0.7
        )
        plt.scatter(
            kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1],
            c="red", marker="x", s=200, linewidths=3, label="Centroids"
        )
        plt.xlabel(numeric_df.columns[0])
        plt.ylabel(numeric_df.columns[1])
        plt.title("KMeans Clustering (first 2 numeric features)")
        plt.legend()

        cluster_img = _fig_to_base64()

        insights["clustering"] = {
            "summary": cluster_info,
            "interpretation": interpretation,
            "image": cluster_img
        }

    return insights
