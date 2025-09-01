📊 Data Sage - an Excel Data Cleaner & Insights Bot

A powerful automation tool to clean, validate, and analyze Excel datasets with ease.
Built as part of my Summer Internship Project (2025), this bot provides:
Automated data cleaning (duplicates, missing values, formatting).
Validation checks for column consistency.
Anomaly detection on numeric features.
Predictive Insights (linear regression + clustering).
Professional reports (HTML + PDF) with visualizations.
An interactive Streamlit GUI for non-technical users.

🚀 Features

✔ Data Cleaning – Removes duplicates, fills missing values, standardizes formats.
✔ Validation – Configurable rules via config.yaml.
✔ Anomaly Detection – Detects outliers using IQR.
✔ Visualizations – Heatmaps, correlation matrix, distributions.
✔ Predictive Insights –

Salary prediction using linear regression (if Experience + Salary exist).

Automatic clustering of numeric columns.
✔ Reports – Exports styled HTML + PDF reports with insights.
✔ Interactive GUI – Upload, preview, clean, analyze, and download results in one click.

🛠️ Tech Stack

Python 3.10+
Pandas, NumPy (data processing)
Seaborn, Matplotlib (visualizations)
Scikit-learn (predictive models)
Streamlit (interactive GUI)
Jinja2 + wkhtmltopdf (report generation)

📂 Project Structure

excel-data-cleaner-bot-advanced/
│── src/
│   ├── cleaning.py         # Data cleaning functions
│   ├── validation.py       # Validation rules
│   ├── anomalies.py        # Anomaly detection
│   ├── visualize.py        # Data visualizations
│   ├── predictive.py       # Predictive insights (ML)
│   ├── reporting.py        # HTML + PDF report generation
│   ├── io_utils.py         # File helpers
│   ├── main.py             # CLI pipeline entrypoint
│── templates/
│   └── report_template.html # Jinja2 HTML report template
│── config/
│   └── config.yaml         # Cleaning + validation rules
│── app.py                  # Streamlit GUI
│── sample_data/sample.xlsx # Example dataset
│── outputs/                # Cleaned files + reports


