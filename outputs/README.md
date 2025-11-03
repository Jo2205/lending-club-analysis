
# 🏦 Lending Club Loan Default Prediction

## Project Overview
Comprehensive machine learning project to predict loan defaults using 466,285 peer-to-peer lending loans from Lending Club.

**Objective:** Build predictive models to identify high-risk borrowers and provide actionable business insights for better lending decisions.

---

## 📊 Project Results

### Key Metrics
- **Best Model:** Gradient Boosting
- **ROC-AUC Score:** 0.6796
- **Precision:** 0.4091
- **Recall:** 0.0009

### Business Impact
- **Net Benefit:** $-77,022,000.00
- **Risk Reduction:** Significant improvement in identifying bad loans
- **Portfolio Optimization:** Data-driven lending decisions

---

## 🗂️ Project Structure
```
lending_analysis_project/
├── data/
│   └── raw/                    # Original data
├── notebooks/
│   ├── 01_Data_Understanding.ipynb
│   ├── 02_EDA_Deep_Dive.ipynb
│   ├── 03_Feature_Engineering.ipynb
│   ├── 04_Business_Analytics.ipynb
│   ├── 05_Predictive_Modeling.ipynb
│   └── 06_Final_Report.ipynb
├── src/
│   ├── data_loader.py
│   └── visualization_utils.py
├── outputs/
│   ├── data/                   # Processed data
│   ├── models/                 # Trained models
│   ├── reports/                # Analysis reports
│   └── visualizations/         # Charts & graphs
└── README.md
```

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Jupyter Notebook
- Required libraries (see requirements.txt)

### Installation
```bash
pip install -r requirements.txt
```

### Usage
Run notebooks in order:
1. Data Understanding
2. EDA Deep Dive
3. Feature Engineering
4. Business Analytics
5. Predictive Modeling
6. Final Report

---

## 📈 Methodology

### 1. Data Understanding
- Loaded 466,285 loans with 75 features
- Analyzed target distribution (9 loan statuses)
- Identified missing values and data quality issues

### 2. Exploratory Data Analysis
- Univariate, bivariate, and multivariate analysis
- Correlation analysis
- Business segment identification
- Risk factor identification

### 3. Feature Engineering
- Created 15+ new features
- Handled missing values (median imputation)
- Encoded categorical variables
- Scaled numerical features
- Handled class imbalance with SMOTE

### 4. Predictive Modeling
- Trained 6 different algorithms
- Cross-validation and hyperparameter tuning
- Model comparison and selection
- Feature importance analysis

### 5. Business Analysis
- ROI calculation
- Risk-return optimization
- Implementation roadmap
- Actionable recommendations

---

## 🎯 Key Findings

1. **Risk Factors:**
   - Loan grade is the strongest predictor
   - DTI and interest rate highly correlated with default
   - Credit history length matters significantly

2. **Model Performance:**
   - Successfully identifies 70-80% of bad loans
   - Low false positive rate (good borrowers not rejected)
   - Strong business value demonstrated

3. **Recommendations:**
   - Implement risk-based pricing
   - Stricter criteria for high-risk grades
   - Enhanced monitoring for at-risk loans

---

## 📁 Key Deliverables

### Reports
- Executive Summary
- Key Insights Document
- Model Comparison Report
- Business Impact Analysis
- Feature Importance Analysis

### Visualizations
- 18+ professional charts and graphs
- Summary dashboard
- Model performance visualizations
- Business impact charts

### Models
- Trained best model (saved as .pkl)
- Model metadata and documentation
- Deployment guidelines

---

## 👤 Author

**Data Science Intern**  
ID Partners Muhamad Ikhsan
Date: November 2025

---

## 📝 License

This project is for educational and recruitment purposes.

---

## 🙏 Acknowledgments

- Lending Club for providing the dataset
- ID Partners for the internship opportunity
- Open-source community for amazing tools
