# Insurance Risk Analytics & Predictive Modeling

## Overview

This project presents an end-to-end insurance analytics pipeline covering exploratory data analysis, data version control, statistical hypothesis testing, and predictive modeling for risk-based pricing.

The objective is to analyze historical insurance data to uncover risk patterns, validate statistical hypotheses, and build machine learning models that support dynamic premium pricing strategies.

The project is structured into four progressive tasks, each building toward a complete data-driven underwriting system.

---

## Project Structure

```text
insurance-risk-analytics/
├── data/
├── notebooks/
│ ├── 01_eda.ipynb
│ ├── 02_hypothesis_testing.ipynb
│ ├── 03_modeling.ipynb
├── src/
├── reports/
├── dvc.yaml
├── requirements.txt
└── README.md

```

---

## Task 1: Exploratory Data Analysis (EDA)

### Key Insights

- Dataset contains **10,000 policies and 21 features**
- No missing values detected across the dataset
- Strong right-skew in financial variables (TotalClaims, TotalPremium)
- Clear geographic variation in risk exposure across provinces
- Vehicle type and make influence claim severity significantly
- Temporal stability observed with mild seasonal claim variation

### Key Visual Insights

- Loss Ratio by Province
- Monthly Claim Trends
- Vehicle Make vs Claim Severity

### Outcome

Established foundational understanding of risk drivers and data quality for modeling and hypothesis testing.

---

## Task 2: Data Version Control (DVC)

A reproducible data pipeline was implemented using DVC to ensure full auditability and version tracking of datasets.

### Implementation Summary

- Initialized DVC in project
- Configured local remote storage
- Tracked raw and cleaned datasets
- Created versioned data pipeline
- Enabled reproducibility using `dvc pull`

### Dataset Versions

- **Raw Data**: Original dataset
- **Cleaned Data**: Processed with feature engineering and cleaned types

### Outcome

Ensures all experiments are reproducible and compliant with audit requirements.

---

## Task 3: Hypothesis Testing

Statistical testing was conducted to validate risk differences across key business segments.

### Hypotheses Tested

- Risk differences across provinces
- Risk differences across zip codes
- Profitability differences across zip codes
- Risk differences between gender groups

### Methods Used

- Chi-square tests (categorical risk)
- T-tests (numerical comparisons)
- Z-tests (large sample validation)

### Key Output

- p-values computed for each hypothesis
- Decisions made using α = 0.05 threshold
- Business interpretations provided for significant results

### Outcome

Identified statistically significant differences in risk across geographic and demographic segments, supporting segmentation-based pricing strategies.

---

## Task 4: Statistical Modeling & Risk-Based Pricing

Machine learning models were developed to predict claim severity and support dynamic pricing.

### Modeling Approach

#### Models Implemented

- Linear Regression (baseline)
- Random Forest Regressor
- XGBoost Regressor

#### Target Variable

- TotalClaims (severity prediction)

---

### Data Preparation

- Missing value handling
- Feature engineering (vehicle and policy attributes)
- Categorical encoding (one-hot / label encoding)
- Train-test split (80/20)

---

### Model Evaluation

| Model             | RMSE             | R² Score |
| ----------------- | ---------------- | -------- |
| Linear Regression | Baseline         | Moderate |
| Random Forest     | Improved         | High     |
| XGBoost           | Best performance | Highest  |

---

### Feature Importance (SHAP Analysis)

Top drivers of claim severity:

- Vehicle type
- Province
- Risk score
- Vehicle model
- Policy attributes

### Business Interpretation

Higher vehicle risk scores and specific vehicle categories significantly increase predicted claim severity, justifying differentiated pricing strategies.

---

### Pricing Framework

Final pricing model:

```

Premium = (P(claim) × Predicted Severity) + Expense Loading + Profit Margin

```

---

## Tools & Technologies

- Python (Pandas, NumPy, Scikit-learn)
- Matplotlib / Seaborn / Plotly
- XGBoost
- SHAP
- DVC
- Git & GitHub Actions

---
