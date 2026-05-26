# Insurance Risk Analytics

A reproducible end-to-end insurance analytics project focused on exploratory data analysis, risk assessment, and data version control using Git, GitHub Actions, and DVC.

The project analyzes historical insurance policy and claims data to uncover profitability patterns, identify high-risk customer segments, and establish an auditable analytics workflow suitable for regulated environments.

---

# Project Objectives

This project aims to:

- Understand the structure and quality of insurance portfolio data
- Explore customer, vehicle, and geographic risk patterns
- Analyze relationships between premiums and claims
- Detect outliers and profitability imbalances
- Build a reproducible data versioning pipeline using DVC
- Establish an industry-standard analytics workflow with CI/CD integration

---

# Project Structure

```text
insurance-risk-analytics/
├── .github/
│   └── workflows/
│       └── ci.yml
├── data/
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_hypothesis_testing.ipynb
│   └── 03_modeling.ipynb
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── eda_utils.py
│   ├── preprocess.py
│   ├── hypothesis_tests.py
│   └── modeling.py
├── reports/
│   └── final_report.md
├── tests/
├── .dvc/
├── requirements.txt
├── dvc.yaml
└── README.md
```

---

# Task 1 — Exploratory Data Analysis

The exploratory analysis investigates the distribution of claims, premiums, vehicle characteristics, and geographic risk concentration across the insurance portfolio.

## Analysis Covered

- Data summarization and statistical profiling
- Data type validation
- Missing value assessment
- Univariate analysis
- Bivariate and multivariate analysis
- Geographic trend analysis
- Outlier detection
- Loss ratio analysis
- Temporal claim trend analysis
- Vehicle risk profiling

---

# Key Insights

- The dataset contains 10,000 insurance policy records with 21 structured features
- Financial variables such as claims and premiums exhibit strong right-skewed distributions
- Several provinces demonstrate significantly higher loss ratios than others
- A small proportion of policies contributes disproportionately to total claims
- Vehicle make and model show measurable impact on claim severity
- Claim activity varies over time, indicating potential seasonal risk behavior

---

# Task 2 — Data Version Control (DVC)

This project uses DVC (Data Version Control) to establish a reproducible and auditable data pipeline.

DVC enables versioning of datasets separately from Git while preserving complete reproducibility of analytics workflows.

## DVC Workflow

### DVC Initialization

```bash
dvc init
```

### Configure Local Remote Storage

```bash
dvc remote add -d localstorage ../dvc-storage
```

### Track Dataset Versions

```bash
dvc add data/insurance_data.csv
dvc add data/insurance_data_cleaned.csv
```

### Push Data to Remote Storage

```bash
dvc push
```

---

# Dataset Versions

## Raw Dataset

- Original insurance dataset before preprocessing

## Cleaned Dataset

- Duplicate records removed
- TransactionDate converted to datetime format
- LossRatio feature engineered
- Prepared for downstream analytics and modeling

---

# Reproducing the Data Pipeline

Clone the repository:

```bash
git clone <repository-url>
cd insurance-risk-analytics
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Pull datasets from DVC storage:

```bash
dvc pull
```

Run preprocessing pipeline:

```bash
python src/preprocess.py
```

Launch Jupyter Notebook:

```bash
jupyter notebook
```

---

# CI/CD Pipeline

GitHub Actions is configured to automatically:

- Install project dependencies
- Run linting checks
- Execute automated tests
- Validate repository integrity on every push and pull request

---

# Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook
- Git & GitHub
- GitHub Actions
- DVC

---
