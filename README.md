# 🔍 Crypto Transaction Forensics: Predicting Rug Pulls

![](https://img.shields.io/badge/Python-3.8%2B-blue) ![](https://img.shields.io/badge/XGBoost-1.6%2B-orange) ![](https://img.shields.io/badge/Streamlit-App-red)

### **Live Demo**
(https://crypto-scam-detector-mm3fnr8zjfxtdhtswabt47.streamlit.app/)



## 📖 Project Overview
While most financial data science projects focus on predicting stock prices, this project tackles a more pressing modern issue: **Financial Fraud Detection**.

"Rug Pulls" are a prevalent scam in the cryptocurrency world where developers abandon a project and run away with investor funds. This project uses Machine Learning to identify "High Risk" transactions before they result in loss.

## 🚀 The Problem
- **The Challenge:** Detecting illicit transactions in a massive, unstructured blockchain environment.
- **The Goal:** Build a classification model that flags transactions as "Legit" or "Scam" based on historical behavioral patterns.

## 🛠️ Tech Stack & Tools
- **Language:** Python
- **Libraries:** XGBoost, Scikit-Learn, Pandas, NumPy
- **Visualization:** Matplotlib, Seaborn
- **Deployment:** Streamlit, Streamlit Cloud
- **Data Source:** [Elliptic Data Set](https://www.kaggle.com/datasets/ellipticco/elliptic-data-set) on Kaggle.

## 📊 Dataset
This project utilizes the **Elliptic Data Set**, the largest public dataset of labeled cryptocurrency transactions.
- **Features:** 165 anonymized features representing transaction patterns (time-step, local topology, etc.).
- **Targets:** 
  - `1` = **Illicit** (Scam/Rug Pull)
  - `0` = **Licit** (Legit)
- **Scale:** Over 200,000 transactions.

## ⚙️ Methodology

### 1. Data Preprocessing
- Cleaned raw data by removing "Unknown" labels to ensure supervised learning.
- Handled severe **Class Imbalance** using scale_pos_weight in XGBoost (crucial for fraud detection where scams are rare).

### 2. Feature Engineering
- Identified top predictive features using XGBoost Feature Importance.
- Although features are anonymized, correlated them to real-world financial concepts like aggregation and peeling.

### 3. Modeling
- Implemented **XGBoost Classifier** for high performance on tabular data.
- Evaluated using Precision, Recall, and F1-Score (focusing on minimizing False Negatives).

## 📈 Results
The model successfully identifies illicit transactions with high precision.
<img width="1882" height="673" alt="Screenshot 2026-03-06 182833" src="https://github.com/user-attachments/assets/e325965e-58f3-40cf-bbcb-417491eb0cf6" />


## 💻 Running the App Locally

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/crypto-scam-detector.git
   ```
2. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
3. Run Streamlit:
   ```bash
   streamlit run app.py
   ```

## 📂 Repository Structure
```
├── app.py                    # Streamlit application script
├── rug_pull_detector.pkl     # Trained XGBoost model
├── requirements.txt          # Python dependencies
├── test_transactions.csv     # Sample data for testing
└── README.md                 # Project documentation
```

## 👨‍💻 Author
**[Pavan Kumar Aadelli]**
Data Science Portfolio Project
```
