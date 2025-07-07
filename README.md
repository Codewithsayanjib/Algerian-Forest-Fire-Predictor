# Algerian-Forest-Fire-Predictor

This project predicts the Forest Fire Index in Algerian regions using machine learning regression models. It includes preprocessing, model training, evaluation, web app development using Flask, and deployment via Render.

## 🔍 Dataset

The dataset was sourced from [Kaggle](https://www.kaggle.com/). It contains meteorological data relevant to forest fires in Algeria. Two versions of the dataset are included:

* `Algerian_forest_fires_dataset_UPDATE.csv` (raw dataset)
* `Algerian_forest_fires_cleaned_dataset.csv` (after cleaning and preprocessing)

## 🧪 Feature Engineering

The dataset was cleaned and transformed as shown in the notebook [`Algerian forest - Ridge, Lasso Regression(1).ipynb`], which includes:

* Handling missing or incorrect values
* Encoding categorical features (e.g., region)
* Normalization and scaling

## 📈 Model Training

The following regression models were trained and evaluated:

* **Linear Regression**
* **Lasso Regression**
* **Ridge Regression**
* **ElasticNet Regression**

Cross-validation was used to compare model performance. Ridge Regression outperformed the others with an R² score of **98.4%**, making it the final choice.

## ✅ Final Model

* The Ridge Regression model and Scaler were pickled as `ridgecv.pkl` and `scaler.pkl`

## 🌐 Web App

A simple Flask web app (`application.py`) was created to allow users to input values and receive a prediction. The template HTML file is located in the `/templates` folder.

### Run Locally

```bash
pip install -r requirements.txt
python application.py
```

## 🚀 Deployment

The app was deployed to [Render](https://render.com):
🔗 [Live App](https://algerian-forest-fire-predictor-7q2x.onrender.com/)



## 🙇‍♂️ Author

Created by **Sayanjib Sur** as part of a machine learning deployment exercise.

Feel free to explore, use, or improve the project. Star ⭐ the repository if you find it helpful!
