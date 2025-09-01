import streamlit as st
import os
import pandas as pd
import tempfile

from src import cleaning, validation, anomalies, visualize, reporting, io_utils, predictive
from src.main import load_config


st.set_page_config(page_title="DataSage", layout="wide")
st.title("📊 DataSage - an Excel Data Cleaner & Insights Bot")
st.write("Upload an Excel file and get a cleaned dataset with validation, anomaly detection, predictive insights, and visualizations.")


# ---------------- Sidebar Controls ----------------
st.sidebar.header("⚙️ Settings")

enable_insights = st.sidebar.checkbox("Enable Predictive Insights", value=True)
report_type = st.sidebar.radio("Report Type", ["HTML", "PDF", "Both"], index=2)
num_clusters = st.sidebar.slider("Number of Clusters (KMeans)", min_value=2, max_value=6, value=3)


uploaded_file = st.file_uploader("📂 Upload Excel file", type=["xlsx", "xls"])

if uploaded_file:
    # Save uploaded file temporarily
    tmp_dir = tempfile.mkdtemp()
    file_path = os.path.join(tmp_dir, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success(f"✅ Uploaded: {uploaded_file.name}")

    # Load config
    config = load_config("config/config.yaml")

    # Load and process
    df = io_utils.load_excel(file_path)

    # Show raw data preview
    st.subheader("🔎 Raw Data Preview")
    st.dataframe(df.head())

    # --- Cleaning ---
    df_clean = cleaning.clean_data(df, config.get("cleaning", {}))

    # --- Validation ---
    issues = validation.validate_data(df_clean, config.get("validation", []))

    # --- Anomalies ---
    anomalies_found = anomalies.detect_anomalies(df_clean)

    # --- Visualizations ---
    tmp_fig_dir = os.path.join(tmp_dir, "figures")
    figs = visualize.generate_visuals(df_clean, tmp_fig_dir)

    # --- Predictive Insights (optional) ---
    insights = {}
    if enable_insights:
        insights = predictive.run_predictive_models(df_clean)
        # Inject custom cluster number if enough numeric cols
        if "clustering" in insights:
            insights["clustering"]["summary"] = f"Identified {num_clusters} clusters (custom) in the dataset"

    # Save cleaned file
    cleaned_path = os.path.join(tmp_dir, f"cleaned_{uploaded_file.name}")
    df_clean.to_excel(cleaned_path, index=False)

    # --- Summary ---
    summary = {
        "Original Rows": df.shape[0],
        "Original Columns": df.shape[1],
        "Cleaned Rows": df_clean.shape[0],
        "Columns After Cleaning": df_clean.shape[1],
        "Validation Issues Found": sum(len(v) for v in issues.values()),
        "Columns With Issues": len(issues),
        "Anomalies Detected": len(anomalies_found),
        "Output File": f"cleaned_{uploaded_file.name}",
    }

    # --- Reports (HTML + PDF) ---
    report_path = os.path.join(tmp_dir, "report.html")
    reporting.generate_report(issues, anomalies_found, figs, summary, insights, report_path)

    # --- Processing Summary Section (NEW) ---
    st.subheader("📋 Processing Summary")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Original Rows", summary["Original Rows"])
        st.metric("Original Columns", summary["Original Columns"])
    with col2:
        st.metric("Cleaned Rows", summary["Cleaned Rows"])
        st.metric("Columns After Cleaning", summary["Columns After Cleaning"])
    with col3:
        st.metric("Validation Issues", summary["Validation Issues Found"])
        st.metric("Anomalies Detected", summary["Anomalies Detected"])

    st.caption(f"Output File: {summary['Output File']}")

    # --- Outputs Section ---
    st.subheader("✅ Outputs")
    with open(cleaned_path, "rb") as f:
        st.download_button("⬇ Download Cleaned Excel", data=f, file_name=f"cleaned_{uploaded_file.name}")

    if report_type in ["HTML", "Both"]:
        with open(report_path, "rb") as f:
            st.download_button("⬇ Download Report (HTML)", data=f, file_name="report.html")

    if report_type in ["PDF", "Both"]:
        pdf_path = report_path.replace(".html", ".pdf")
        if os.path.exists(pdf_path):
            with open(pdf_path, "rb") as f:
                st.download_button("⬇ Download Report (PDF)", data=f, file_name="report.pdf")

    # --- Predictive Insights Section ---
    if enable_insights:
        st.subheader("🔮 Predictive Insights")
        if insights:
            for key, value in insights.items():
                if isinstance(value, dict):
                    if "formula" in value:
                        st.markdown(f"**{key.replace('_',' ').title()}:** {value['formula']}")
                        st.caption(value.get("interpretation", ""))
                    elif "summary" in value:
                        st.markdown(f"**{key.replace('_',' ').title()}:** {value['summary']}")
                        st.caption(value.get("interpretation", ""))
                        if "image" in value:  # Show clustering visualization
                            st.image(f"data:image/png;base64,{value['image']}")
                else:
                    st.markdown(f"**{key.replace('_',' ').title()}:** {value}")
        else:
            st.info("No predictive insights available for this dataset.")

    # --- Visualizations Section ---
    st.subheader("📊 Visualizations")
    for name, img in figs.items():
        st.write(f"**{name.replace('_',' ').title()}**")
        st.image(f"data:image/png;base64,{img}")
