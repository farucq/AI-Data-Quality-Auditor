
# Autonomous AI System for Data Quality Auditing

## Overview
This project implements an **Autonomous AI-powered Data Quality Auditor** that automatically analyzes datasets, identifies data quality problems, explains why those problems matter, and suggests corrective actions.

The system is designed to behave like a **junior data analyst**, capable of auditing datasets without human guidance and producing a professional, human-readable audit report.

---

## Problem Statement
Real-world datasets often contain hidden quality issues such as:
- Missing or inconsistent values
- Outliers that silently affect model performance
- Highly correlated or redundant features
- Data patterns that can bias machine learning models

These issues are often overlooked and can significantly degrade the reliability of analytics and ML systems.
This project addresses that problem by building an **AI-driven automated auditing pipeline**.

---

## Objectives
The main objectives of this project are:
- Automatically analyze any CSV dataset
- Detect common and advanced data quality issues
- Use an AI model to **reason** about why each issue matters
- Recommend practical data preprocessing and modeling fixes
- Generate a structured audit report
- Compute an overall **Dataset Risk Score (0–100)**

---

## Input Requirements
- Dataset format: CSV
- Minimum of **15 columns**
- At least **1 target variable**
- Works on unseen datasets without hardcoded rules

---

## Output
The system generates the following outputs:
- Dataset summary (shape, data types, missing value percentages)
- Detected data quality issues (outliers, correlations, etc.)
- AI-generated explanations describing the impact on ML models
- AI-generated recommendations for fixing each issue
- Dataset Risk Score with interpretation
- Final audit report in Markdown format

---

## Dataset Risk Score
The Dataset Risk Score provides a single numerical measure of data quality risk.

- **0–30** → Low Risk (dataset is mostly clean)
- **31–60** → Medium Risk (cleaning and validation recommended)
- **61–100** → High Risk (significant data quality issues present)

The score is computed based on missing values, number of detected issues, and their severity.

---

## Technology Stack
- Python
- Pandas, NumPy
- Scikit-learn
- HuggingFace Transformers
- Open-source Large Language Model: **Microsoft Phi-2**

---

## Project Structure
AI-Data-Quality-Auditor/
├── data/               # Sample dataset
├── notebooks/          # Google Colab / Jupyter notebook
├── src/                # Modular source code
├── reports/            # Generated audit reports
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation

---

## How to Run the Project

### Option 1: Google Colab (Recommended)
1. Open the notebook `AI_Data_Quality_Auditor.ipynb` in Google Colab
2. Install dependencies using the provided cells
3. Upload or use the sample CSV dataset
4. Run all cells from top to bottom
5. View the generated audit report and risk score

### Option 2: Local Execution
1. Clone the repository
2. Install dependencies using `pip install -r requirements.txt`
3. Run the notebook or Python scripts
4. Review the generated audit report

---

## How the System Works
1. Loads the dataset
2. Generates a dataset summary
3. Detects data quality issues automatically
4. Uses an AI model to explain why each issue matters
5. Suggests fixes and improvements
6. Calculates dataset risk score
7. Produces a final audit report

---

## Future Improvements
- Auto-fix mode with before/after comparison
- Streamlit-based user interface
- PDF export of audit reports
- Feature importance and validation diagnostics

---

## Conclusion
This project demonstrates how **agentic AI systems** can be used to automate data quality auditing.
By combining statistical analysis with AI-based reasoning, the system provides meaningful insights that help improve dataset reliability and machine learning performance.
