def generate_report(summary, audit_results, risk_score, interpretation):
    report = "# AI Data Quality Audit Report\n\n"

    report += "## Dataset Overview\n"
    report += f"- Shape: {summary['shape']}\n"
    report += f"- Dataset Risk Score: {risk_score}/100\n"
    report += f"- Interpretation: {interpretation}\n\n"

    report += "## Detected Issues & AI Reasoning\n\n"

    for idx, item in enumerate(audit_results, start=1):
        report += f"### {idx}. {item['issue']}\n\n"
        report += f"**(a) Why it matters:**\n{item['explanation']}\n\n"
        report += f"**(b) Recommendation:**\n{item['recommendation']}\n\n"
        report += "---\n\n"

    return report
