## Fraud Detection using Machine Learning

## 📌 Project Overview
This project aims to detect fraudulent financial transactions using machine learning techniques. The dataset contains millions of transactions with highly imbalanced classes, making fraud detection a challenging classification problem.

---

## 📊 Dataset
- Source: INSAID Fraud Detection Dataset  
- Total records: 6.3 million  
- Target variable: `isFraud`  

## ⚠️ Note on Data Usage
Due to the large size of the dataset (6.3 million records), a random sample was used during analysis and model training to ensure efficient computation while preserving data distribution.

---

## ⚙️ Steps Performed
- Data Cleaning & Preprocessing  
- Exploratory Data Analysis (EDA)  
- Data Sampling (for efficient processing)  
- Handling Class Imbalance (SMOTE – experimented)  
- Model Building (Random Forest)  
- Threshold Tuning  
- Model Evaluation  

---

## 📈 Model Performance (Random Forest)
- ROC-AUC Score: **0.998**  
- Recall (Fraud): **91%**  
- Precision (Fraud): **19%**  

👉 The model prioritizes recall over precision, which is crucial in fraud detection where missing fraudulent transactions is more costly than false positives.

---

## 🔍 Key Insights
- Balance-related features are the most important indicators of fraud  
- Fraud is more frequent in **TRANSFER** and **CASH_OUT** transactions  
- Large or unusual transaction amounts are more likely to be fraudulent  
- Sampling enabled efficient handling of large-scale data without significant performance loss  

---

## 🛠️ Tech Stack
- Python  
- Pandas, NumPy  
- Scikit-learn  
- Seaborn, Matplotlib  

---

## 📂 Project Structure
- `fraud_detection.ipynb` → Main notebook  

---

## 🚀 Future Improvements
- Try advanced models like XGBoost / LightGBM  
- Improve precision using better threshold tuning or feature engineering  
- Build a real-time fraud detection pipeline  

---

## 👩‍💻 Author
**Mahasweta Kundu**
