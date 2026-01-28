from transformers import pipeline

llm = pipeline(
    "text-generation",
    model="microsoft/phi-2",
    device_map="auto"
)

def explain_issue(issue: str) -> str:
    prompt = f"""
Explain clearly why the following data quality issue matters
and how it impacts machine learning model performance:

Issue: {issue}
"""
    return llm(prompt, max_new_tokens=120, do_sample=False)[0]["generated_text"]

def recommend_fix(issue: str) -> str:
    prompt = f"""
Suggest 3 practical data preprocessing or modeling fixes
for the following issue:

Issue: {issue}
"""
    return llm(prompt, max_new_tokens=120, do_sample=False)[0]["generated_text"]
