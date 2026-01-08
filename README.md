# Data Sage – Excel Data Cleaner & Insights Bot

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![Scikit-learn](https://img.shields.io/badge/ML-Scikit--learn-orange)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-success)
![Internship](https://img.shields.io/badge/Project-Summer%20Internship%202025-purple)

---

## 🚀 Overview

**Data Sage** is an end-to-end automation tool that **cleans, validates, analyzes, and generates insights from Excel datasets** with minimal manual effort.

Developed as part of my **Summer Internship Project (2025)**, this project focuses on **real-world data quality challenges**, combining automation, machine learning, and visualization with an intuitive interface for both technical and non-technical users.

---

## 🎯 Why This Project Matters

In real-world datasets:
- Excel files are messy and inconsistent  
- Manual cleaning is time-consuming and error-prone  
- Insights are often delayed or missed  

**Data Sage** automates the entire workflow — from raw Excel files to **ML-driven insights and professional reports** — making data analysis faster, reliable, and accessible.

---

## ✨ Key Features

### 🔹 Automated Data Cleaning
- Removes duplicate records  
- Handles missing values intelligently  
- Standardizes numeric, categorical, and date formats  

### 🔹 Data Validation
- Rule-based validation using `config.yaml`  
- Ensures schema and column consistency  

### 🔹 Anomaly Detection
- Detects numeric outliers using **Interquartile Range (IQR)**  
- Flags potential data quality issues  

### 🔹 Visual Analytics
- Correlation matrices  
- Heatmaps  
- Feature distributions  

### 🔹 Predictive Insights
- **Linear Regression** for salary prediction  
  *(Automatically triggered if `Experience` and `Salary` columns exist)*  
- **Unsupervised Clustering** on numeric features for pattern discovery  

### 🔹 Professional Reports
- Styled **HTML reports**
- Exportable **PDF reports**
- Embedded charts, summaries, and insights  

### 🔹 Interactive GUI
- Built using **Streamlit**
- Upload → Preview → Clean → Analyze → Download  
- Designed for non-technical users  

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **Pandas, NumPy** – Data processing  
- **Seaborn, Matplotlib** – Visualization  
- **Scikit-learn** – Machine Learning  
- **Streamlit** – Interactive Web UI  
- **Jinja2 + wkhtmltopdf** – Report generation  

---

## 📂 Project Structure

```text
excel-data-cleaner-bot-advanced/
│
├── src/
│   ├── cleaning.py        # Data cleaning logic
│   ├── validation.py     # Rule-based validation
│   ├── anomalies.py      # Outlier detection (IQR)
│   ├── visualize.py      # Visual analytics
│   ├── predictive.py     # ML models & clustering
│   ├── reporting.py      # HTML & PDF report generation
│   ├── io_utils.py       # File utilities
│   └── main.py           # CLI pipeline entrypoint
│
├── templates/
│   └── report_template.html
│
├── config/
│   └── config.yaml
│
├── sample_data/
│   └── sample.xlsx
│
├── outputs/
│   └── cleaned_files & reports
│
├── app.py                # Streamlit GUI
└── README.md

## ▶️ How to Run

### 1️⃣ Install Dependencies
```bash
pip install -r requirements.txt

### 2️⃣ Run the Streamlit App (Recommended)
```bash
streamlit run app.py

### 3️⃣ Run via CLI (Optional)
```bash
python src/main.py

## 📄 License

This project is licensed under the MIT License.

## 👤 Author

**Raghav Tiwari**
B.Tech Computer Science Engineering
Software Engineering | Data Analytics | Machine Learning | Cloud



