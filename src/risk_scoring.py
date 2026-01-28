def calculate_dataset_risk_score(summary, audit_results):
    risk = 0

    # Missing values (max 30)
    risk += min(summary["missing_percentage"].mean() * 2, 30)

    # Issue count (max 40)
    risk += min(len(audit_results) * 3, 40)

    # Severity (max 30)
    for item in audit_results:
        issue = item["issue"].lower()
        if "outlier" in issue:
            risk += 10
        if "correlation" in issue:
            risk += 5

    return min(int(risk), 100)

def interpret_risk(score):
    if score < 30:
        return "Low Risk – Dataset is mostly clean."
    elif score < 60:
        return "Medium Risk – Data cleaning recommended."
    else:
        return "High Risk – Significant data quality issues detected."
