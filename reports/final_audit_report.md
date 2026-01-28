# AI Data Quality Audit Report

## Dataset Overview
- Shape: (15, 16)
- Dataset Risk Score: **100/100**
- Risk Interpretation: **High Risk – Significant data quality issues detected.**

## Detected Issues & AI Reasoning

### 1. ML-based outliers detected in numerical features

**(a) Why it matters:**
1. This data quality issue matters because it can significantly impact the performance of machine learning models. Outliers are data points that deviate significantly from the normal pattern or distribution of the data. If these outliers are not properly handled, they can lead to biased or inaccurate predictions by the ML models. This can result in poor decision-making and suboptimal outcomes.
2. Outliers in numerical features can have a significant impact on ML model performance. They can skew the distribution of the data, leading to biased estimations of model parameters. This can result in overfitting or under

**(b) Recommendation:**
1. Remove outliers using statistical methods such as the Z-score.
2. Winsorize the data by replacing extreme values with less extreme values.
3. Use robust regression algorithms that are less sensitive to outliers.

---

### 2. High correlation between income and age

**(a) Why it matters:**
1. This data quality issue matters because it can lead to biased predictions and unfair treatment of individuals. If the income and age variables are highly correlated, the ML model may mistakenly assume that age determines income, leading to inaccurate predictions and potentially discriminatory outcomes.
2. The high correlation between income and age can impact ML model performance by introducing noise and reducing the model's ability to accurately capture the relationship between the variables. This can result in suboptimal predictions and a lack of generalizability to new data.

**(b) Recommendation:**
1. Remove the income variable from the analysis to reduce the correlation.
2. Use a different statistical technique, such as principal component analysis, to reduce the correlation.
3. Conduct a sensitivity analysis to assess the impact of the correlation on the results.

---

### 3. High correlation between credit_score and age

**(a) Why it matters:**
1. This data quality issue matters because it can lead to biased predictions and unfair treatment of individuals. If credit_score and age are highly correlated, it means that individuals with similar ages are likely to have similar credit scores. This can result in ML models making inaccurate predictions based on age alone, without considering other relevant factors.
2. The high correlation between credit_score and age can impact ML model performance by introducing bias and reducing the model's ability to accurately predict creditworthiness. If the model relies solely on age as a predictor, it may overlook other important factors that contribute to creditworthiness,

**(b) Recommendation:**
1. Remove one of the variables (credit_score or age) from the analysis to reduce the correlation.
2. Use a different statistical technique, such as principal component analysis, to identify the underlying factors driving the correlation.
3. Conduct a regression analysis to determine if the correlation is statistically significant and if it has a meaningful impact on the model's performance.

---

### 4. High correlation between credit_score and income

**(a) Why it matters:**
1. This data quality issue matters because it can lead to biased predictions and unfair treatment of individuals. If credit_score and income are highly correlated, the ML model may assign higher credit scores to individuals with higher incomes, even if their creditworthiness is not accurately reflected. This can result in discrimination against individuals with lower incomes, who may be unfairly denied credit or offered higher interest rates.
2. The high correlation between credit_score and income can impact ML model performance by introducing bias and reducing the model's ability to accurately predict creditworthiness. If the model relies heavily on credit_score as a

**(b) Recommendation:**
1. Remove one of the variables (credit_score or income) from the analysis to reduce the correlation.
2. Use a different statistical technique, such as principal component analysis, to identify the underlying factors driving the correlation.
3. Conduct a regression analysis to determine the impact of credit_score on income while controlling for other variables.

---

### 5. High correlation between tenure_months and age

**(a) Why it matters:**
1. This data quality issue matters because it can lead to biased predictions and inaccurate insights. If there is a high correlation between tenure_months and age, it means that the two variables are closely related, and using one as a predictor for the other may not provide meaningful results.
2. This issue impacts ML model performance because it can introduce noise and distort the relationships between variables. If the model relies on tenure_months as a predictor for age, it may assign incorrect values to age based on the high correlation, leading to inaccurate predictions and potentially misleading insights.

**(b) Recommendation:**
1. Remove tenure_months from the dataset.
2. Use a different variable to measure tenure, such as years of service.
3. Perform a correlation analysis to determine the strength and direction of the relationship between tenure and age.

---

### 6. High correlation between tenure_months and income

**(a) Why it matters:**
1. This data quality issue matters because it can lead to biased predictions and inaccurate insights. If there is a high correlation between tenure_months and income, it means that the model is relying heavily on this feature to make predictions. This can result in overfitting, where the model performs well on the training data but fails to generalize to new, unseen data.
2. The high correlation between tenure_months and income can impact ML model performance by introducing noise and reducing the model's ability to capture other important features. It can also lead to biased predictions, as the model may give more weight

**(b) Recommendation:**
1. Remove one of the variables (e.g., tenure_months) from the analysis to reduce the correlation.
2. Use a different statistical technique, such as principal component analysis, to identify and remove correlated variables.
3. Conduct a sensitivity analysis to assess the impact of removing one variable on the overall analysis and conclusions.

---

### 7. High correlation between tenure_months and credit_score

**(a) Why it matters:**
1. This data quality issue matters because it can lead to biased predictions in the ML model. If there is a high correlation between tenure_months and credit_score, it means that the model is relying heavily on one feature to make predictions. This can result in inaccurate predictions for new customers who may have different tenure_months but similar credit_scores.
2. The high correlation between tenure_months and credit_score impacts ML model performance by reducing its ability to capture the complexity of the data. The model may become overly reliant on the tenure_months feature and fail to consider other important

**(b) Recommendation:**
1. Remove one of the variables (either tenure_months or credit_score) from the analysis to reduce the correlation.
2. Use a different statistical technique, such as principal component analysis, to identify the underlying factors driving the correlation.
3. Conduct a sensitivity analysis to assess the impact of removing one of the variables on the overall analysis results.

---

### 8. High correlation between avg_session_time and age

**(a) Why it matters:**
1. This data quality issue matters because it can lead to biased predictions and inaccurate insights. If there is a high correlation between avg_session_time and age, it means that the model is relying heavily on age as a predictor of session time. This can result in unfair treatment of certain age groups and inaccurate recommendations.
2. The high correlation between avg_session_time and age impacts ML model performance by introducing bias and reducing the model's ability to accurately predict session time for users who are not in the same age group. This can lead to suboptimal recommendations and a lack of diversity

**(b) Recommendation:**
1. Remove the age column from the dataset.
2. Use a different feature to predict avg_session_time, such as the number of active users.
3. Use a different machine learning algorithm that is less sensitive to correlation, such as a decision tree.

---

### 9. High correlation between avg_session_time and income

**(a) Why it matters:**
1. This data quality issue matters because it can lead to biased predictions and inaccurate insights. If there is a high correlation between avg_session_time and income, it means that the model is relying heavily on this feature to make predictions. This can result in unfair treatment of certain individuals or groups based on their income, as the model may not consider other relevant factors.
2. The high correlation between avg_session_time and income can impact ML model performance by introducing bias and reducing the model's ability to generalize to new data. If the model is trained on data that has a strong

**(b) Recommendation:**
1. Remove one of the variables from the analysis to reduce the correlation.
2. Use a different statistical method to analyze the relationship between the variables.
3. Conduct a regression analysis to determine the impact of each variable on income.

---

### 10. High correlation between avg_session_time and credit_score

**(a) Why it matters:**
1. This data quality issue matters because it can lead to biased predictions in the ML model. If there is a high correlation between avg_session_time and credit_score, the model may mistakenly assume that longer session times are indicative of higher credit scores. This can result in unfair lending decisions and potentially harm individuals who may have lower session times but still have good credit scores.
2. The high correlation between avg_session_time and credit_score can impact ML model performance by introducing bias and reducing the model's ability to accurately predict credit scores. The model may give more weight to session

**(b) Recommendation:**
1. Remove one of the variables from the analysis to reduce the correlation.
2. Use a different statistical method, such as principal component analysis, to reduce the correlation.
3. Conduct a regression analysis to determine if there is a causal relationship between the two variables.

---

### 11. High correlation between avg_session_time and tenure_months

**(a) Why it matters:**
1. This data quality issue matters because it can lead to biased predictions and inaccurate insights. If there is a high correlation between avg_session_time and tenure_months, it means that the two variables are strongly related. This can result in overfitting, where the ML model becomes too specific to the training data and fails to generalize well to new data.
2. The high correlation between avg_session_time and tenure_months can impact ML model performance by introducing noise and reducing the model's ability to capture other important features. It can also lead to biased predictions, as the model

**(b) Recommendation:**
1. Remove one of the variables from the analysis to reduce the correlation.
2. Use a different statistical method to analyze the relationship between the variables.
3. Conduct a regression analysis to determine the impact of each variable on the other.

---

### 12. High correlation between avg_session_time and num_complaints

**(a) Why it matters:**
1. This data quality issue matters because it can lead to biased predictions and inaccurate insights. If there is a high correlation between avg_session_time and num_complaints, it means that the two variables are strongly related. This can result in ML models incorrectly assuming that longer session times are indicative of higher complaint rates, leading to flawed predictions and recommendations.
2. The high correlation between avg_session_time and num_complaints impacts ML model performance by introducing noise and reducing the model's ability to capture other important factors. ML models rely on patterns and relationships in the data to make

**(b) Recommendation:**
1. Remove one of the variables from the analysis to reduce the correlation.
2. Use a different statistical method, such as principal component analysis, to reduce the correlation.
3. Conduct a regression analysis to determine if there is a causal relationship between the two variables.

---

### 13. High correlation between discount_rate and num_complaints

**(a) Why it matters:**
1. This data quality issue matters because it can lead to biased predictions in the ML model. If there is a high correlation between discount_rate and num_complaints, it means that the model may be overfitting the data and not generalizing well to new instances. This can result in inaccurate predictions and unreliable insights.
2. The high correlation between discount_rate and num_complaints can impact ML model performance by introducing noise and reducing the model's ability to capture the underlying patterns in the data. It can lead to overfitting, where the model memorizes the training data instead of

**(b) Recommendation:**
1. Remove one of the variables from the model to reduce multicollinearity.
2. Use a different variable to predict the discount_rate, such as the average rating of the product.
3. Use a different machine learning algorithm that is less sensitive to multicollinearity, such as a decision tree or random forest.

---

### 14. High correlation between discount_rate and last_login_days

**(a) Why it matters:**
1. This data quality issue matters because it can lead to biased predictions and inaccurate insights. If there is a high correlation between discount_rate and last_login_days, it means that the model is relying heavily on one feature to make predictions, which may not be a reliable indicator of customer behavior. This can result in poor model performance and misleading conclusions.
2. The high correlation between discount_rate and last_login_days can impact ML model performance by introducing noise and reducing the model's ability to capture other important factors that influence customer behavior. The model may become overly focused on the

**(b) Recommendation:**
1. Remove the last_login_days column from the dataset.
2. Use a different feature to capture the frequency of logins, such as the number of logins per month.
3. Use a different feature to capture the frequency of logins, such as the number of logins per year.

---

### 15. High correlation between discount_rate and avg_session_time

**(a) Why it matters:**
1. This data quality issue matters because it can lead to biased predictions and inaccurate insights. If there is a high correlation between discount_rate and avg_session_time, it means that the model is relying heavily on one feature to make predictions, which may not be a reliable indicator of customer behavior. This can result in misleading recommendations and poor decision-making.
2. The high correlation between discount_rate and avg_session_time impacts ML model performance by introducing noise and reducing the model's ability to capture other important patterns and relationships in the data. It can lead to overfitting,

**(b) Recommendation:**
1. Remove one of the variables from the model to reduce multicollinearity.
2. Use a different variable to predict avg_session_time, such as avg_session_duration.
3. Use a different machine learning algorithm that is less sensitive to multicollinearity, such as decision trees.

---

