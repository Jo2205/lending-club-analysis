# 🏦 Lending Club Loan Default Prediction

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-Educational-green.svg)
![Status](https://img.shields.io/badge/Status-Complete-success.svg)

## 📋 Deskripsi Proyek

Proyek analisis data komprehensif untuk memprediksi default loan menggunakan dataset **466,285 peer-to-peer lending loans** dari Lending Club. Proyek ini menggunakan machine learning untuk mengidentifikasi peminjam berisiko tinggi dan memberikan insight bisnis yang actionable untuk keputusan pemberian pinjaman yang lebih baik.

**Tujuan:** Membangun model prediktif untuk mengidentifikasi peminjam berisiko tinggi dan mengoptimalkan keputusan pemberian pinjaman berbasis data.

---

## 🎯 Hasil Utama

### Performa Model
- **Best Model:** Gradient Boosting
- **ROC-AUC Score:** 0.6796
- **Precision:** 0.4091
- **Recall:** 0.0009
- **F1-Score:** 0.0017

### Business Impact
- Analisis komprehensif terhadap 466,285 loans
- Identifikasi faktor risiko utama: Interest rate, DTI, Loan grade, Credit history
- Pengurangan risiko melalui pendekatan data-driven
- Rekomendasi strategi bisnis yang dapat diimplementasikan

---

## 🗂️ Struktur Proyek

```
lending-club-analysis/
├── 📊 Data_Understanding.ipynb          # Pemahaman data awal
├── 📈 EXPLORATORY DATA ANALYSIS.ipynb   # Analisis eksplorasi mendalam
├── 🔧 FEATURE ENGINEERING.ipynb         # Rekayasa fitur
├── 🤖 MODELING.ipynb                    # Pelatihan model ML
├── 📄 FINAL REPOT.ipynb                 # Laporan akhir komprehensif
├── 📦 requirements.txt                  # Dependencies Python
├── 🐍 git.py                           # Utility script
└── 📁 outputs/                         # Hasil analisis
    ├── reports/                        # Laporan CSV & TXT
    ├── visualizations/                 # Grafik & dashboard
    └── README.md                       # Dokumentasi output
```

---

## 🚀 Quick Start

### Prerequisites
```bash
Python 3.8+
Jupyter Notebook
```

### Installation

1. Clone repository
```bash
git clone https://github.com/Jo2205/lending-club-analysis.git
cd lending-club-analysis
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Jalankan Jupyter Notebook
```bash
jupyter notebook
```

4. Buka dan jalankan notebook secara berurutan:
   - `Data_Understanding.ipynb`
   - `EXPLORATORY DATA ANALYSIS.ipynb`
   - `FEATURE ENGINEERING.ipynb`
   - `MODELING.ipynb`
   - `FINAL REPOT.ipynb`

---

## 📊 Metodologi

### 1️⃣ Data Understanding
- ✅ Loaded 466,285 loans dengan 75 features
- ✅ Analisis distribusi target (9 status pinjaman)
- ✅ Identifikasi missing values dan data quality issues
- ✅ Eksplorasi karakteristik dataset

### 2️⃣ Exploratory Data Analysis (EDA)
- ✅ Analisis univariate, bivariate, dan multivariate
- ✅ Correlation analysis untuk fitur numerik
- ✅ Identifikasi segmen bisnis
- ✅ Deteksi faktor risiko utama
- ✅ Visualisasi komprehensif (18+ grafik)

### 3️⃣ Feature Engineering
- ✅ Dibuat 15+ fitur baru yang prediktif
- ✅ Handling missing values (median imputation)
- ✅ Encoding variabel kategorikal
- ✅ Scaling fitur numerik
- ✅ Handling class imbalance dengan SMOTE
- ✅ Removal data leakage dan post-loan information

### 4️⃣ Predictive Modeling
- ✅ Training 6 algoritma berbeda:
  - Logistic Regression
  - Decision Tree
  - Random Forest
  - Gradient Boosting
  - XGBoost
  - LightGBM
- ✅ Cross-validation dan hyperparameter tuning
- ✅ Model comparison dan selection
- ✅ Feature importance analysis

### 5️⃣ Business Analysis
- ✅ ROI calculation
- ✅ Risk-return optimization
- ✅ Implementation roadmap
- ✅ Actionable recommendations

---

## 🔍 Key Findings

### 📌 Faktor Risiko Utama

1. **Loan Grade** - Prediktor terkuat
   - Grade F/G memiliki default rate 3-4x lebih tinggi
   - Grade A-B paling aman dengan default rate <5%

2. **Interest Rate** - Korelasi kuat dengan default
   - Threshold kritis: 15%
   - Rate >15% mengindikasikan risiko tinggi

3. **DTI (Debt-to-Income Ratio)**
   - Bad loans rata-rata 2-3 poin lebih tinggi
   - DTI >25 adalah red flag

4. **Credit History**
   - Riwayat kredit pendek = risiko tinggi
   - Delinquency history adalah strong predictor

5. **Revolving Utilization**
   - Utilisasi >75% mengindikasikan stress keuangan

### 📊 Segmentasi Peminjam

**✅ LOW RISK (Good Profile):**
- Grade A-B loans
- DTI < 15
- Tidak ada delinquencies
- Interest rate < 10%
- Riwayat kredit >5 tahun

**❌ HIGH RISK (Bad Profile):**
- Grade E-G loans
- DTI > 25
- Past delinquencies
- Interest rate > 15%
- Riwayat kredit <2 tahun

---

## 💡 Rekomendasi Bisnis

### 🎯 Immediate Actions
1. Deploy model dalam pilot program (10-20% aplikasi)
2. Implementasi kriteria lebih ketat untuk Grade F-G loans
3. Flag aplikasi dengan DTI >25 untuk manual review
4. Setup automated reporting dashboard

### 📈 Strategic Initiatives
1. **Risk-Based Pricing:** Adjust rate berdasarkan model score
2. **Targeted Marketing:** Focus akuisisi pada low-risk segments
3. **Portfolio Rebalancing:** Kurangi exposure ke high-risk grades
4. **Enhanced Monitoring:** Real-time tracking portfolio health

### 🔄 Continuous Improvement
1. Retrain model secara quarterly dengan data baru
2. A/B testing berbagai approval thresholds
3. Eksplorasi ensemble methods untuk performa lebih baik
4. Enhance data collection untuk missing features

---

## 📁 Deliverables

### 📄 Reports (outputs/reports/)
- ✅ Executive Summary
- ✅ Key Insights Document
- ✅ Model Comparison Report
- ✅ Business Impact Analysis
- ✅ Feature Importance Analysis
- ✅ Data Dictionary
- ✅ Deliverables Checklist

### 📊 Visualizations (outputs/visualizations/)
- ✅ 18+ professional charts and graphs
- ✅ Summary dashboard
- ✅ Model performance visualizations
- ✅ Correlation matrix
- ✅ Feature distributions
- ✅ Business impact charts

### 🤖 Models
- ✅ Trained best model (saved as .pkl)
- ✅ Model metadata dan dokumentasi
- ✅ Deployment guidelines

---

## 🛠️ Tech Stack

**Programming Language:**
- Python 3.8+

**Libraries:**
- **Data Processing:** pandas, numpy
- **Visualization:** matplotlib, seaborn, plotly
- **Machine Learning:** scikit-learn, xgboost, lightgbm
- **Class Imbalance:** imbalanced-learn
- **Model Persistence:** joblib

**Environment:**
- Jupyter Notebook
- Git version control

---

## 📈 Model Performance Comparison

| Model | Accuracy | Precision | Recall | F1-Score | ROC-AUC |
|-------|----------|-----------|--------|----------|---------|
| **Gradient Boosting** | **0.8882** | **0.4091** | **0.0009** | **0.0017** | **0.6796** |
| LightGBM | 0.8880 | 0.3636 | 0.0008 | 0.0016 | 0.6745 |
| Random Forest | 0.8882 | 0.4000 | 0.0004 | 0.0008 | 0.6736 |
| XGBoost | 0.8881 | 0.3750 | 0.0006 | 0.0012 | 0.6699 |
| Decision Tree | 0.7761 | 0.1701 | 0.1838 | 0.1768 | 0.5800 |
| Logistic Regression | 0.8877 | 0.3333 | 0.0002 | 0.0004 | 0.5546 |

---

## 📚 Dataset

**Source:** Lending Club (2007-2014)
- **Total Loans:** 466,285
- **Original Features:** 75
- **Engineered Features:** 60+
- **Default Rate:** ~9-11% (varies by grade)

**Target Variable:** Binary classification
- 0 = Good Loan (Fully Paid)
- 1 = Bad Loan (Charged Off, Default, Late)

---

## 👤 Author

**Muhamad Ikhsan**
Data Science Intern - IDX Partners
📅 November 2025

---

## 📝 License

Proyek ini dibuat untuk tujuan educational dan portfolio. Dipersilakan untuk dipelajari dan dijadikan referensi.

---

## 🙏 Acknowledgments

- **Lending Club** untuk menyediakan dataset
- **IDX Partners** atas kesempatan internship
- **Open-source community** untuk tools dan libraries yang luar biasa
- **Kaggle** untuk platform dan resources

---

## 📞 Contact

Jika ada pertanyaan atau diskusi lebih lanjut mengenai proyek ini:

- 📧 Email: [Your Email]
- 💼 LinkedIn: [Your LinkedIn]
- 🐱 GitHub: [@Jo2205](https://github.com/Jo2205)

---

## 🔗 Links

- [Jupyter Notebooks](/)
- [Project Reports](outputs/reports/)
- [Visualizations](outputs/visualizations/)
- [Requirements](requirements.txt)

---

**⭐ Jika proyek ini bermanfaat, silakan berikan star!**

---

<p align="center">
  <i>Built with ❤️ for better lending decisions through data science</i>
</p>
