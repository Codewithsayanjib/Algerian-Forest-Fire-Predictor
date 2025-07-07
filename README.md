# 🔥 Algerian Forest Fire Predictor

> Predict forest fire risk in Algerian regions using machine learning and meteorological data.  
> Built with regression models, Flask, and deployed on Render.

---

## 📊 Dataset

The dataset is sourced from [Kaggle](https://www.kaggle.com/) and includes meteorological data from two Algerian regions relevant to forest fire prediction.

**Included files:**
- `Algerian_forest_fires_dataset_UPDATE.csv` – raw dataset  
- `Algerian_forest_fires_cleaned_dataset.csv` – cleaned and preprocessed version

---

## 🧪 Feature Engineering

Preprocessing and transformation steps are documented in the notebook:  
📘 [`Algerian forest - Ridge, Lasso Regression(1).ipynb`](./Algerian%20forest%20-%20Ridge,%20Lasso%20Regression(1).ipynb)

**Key steps:**
- Removal of missing or incorrect values  
- Encoding categorical variables (e.g., `Region`)  
- Feature correlation analysis and dimensionality reduction  
- Input scaling using `StandardScaler`

---

## 🧠 Model Training

The following regression models were trained and evaluated:

- Linear Regression  
- Lasso Regression  
- Ridge Regression ✅  
- ElasticNet Regression  

📌 **Final Model**: Ridge Regression  
📈 **R² Score**: 98.4% (via cross-validation)

---

## 💾 Model Artifacts

- `ridgecv.pkl` – Trained Ridge Regression model  
- `scaler.pkl` – Fitted `StandardScaler` for preprocessing

---

## 🌐 Flask Web App

A lightweight web application built using Flask to make real-time predictions from user input.

**File structure:**



