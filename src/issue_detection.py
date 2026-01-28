import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import IsolationForest

def detect_outliers(df):
    num_df = df.select_dtypes(include=np.number).dropna()
    if num_df.empty:
        return []

    X = StandardScaler().fit_transform(num_df)
    model = IsolationForest(contamination=0.05, random_state=42)
    preds = model.fit_predict(X)

    if -1 in preds:
        return ["ML-based outliers detected in numerical features"]
    return []

def detect_correlations(df, threshold=0.9):
    corr = df.select_dtypes(include=np.number).corr()
    issues = []

    for i in range(len(corr.columns)):
        for j in range(i):
            if abs(corr.iloc[i, j]) > threshold:
                issues.append(
                    f"High correlation between {corr.columns[i]} and {corr.columns[j]}"
                )
    return issues
