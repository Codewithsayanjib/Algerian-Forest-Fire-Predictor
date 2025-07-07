🔥 Algerian Forest Fire Predictor
A machine learning web application that predicts the Forest Fire Weather Index (FWI) in Algerian regions using meteorological data. Built with regression models, Flask, and deployed on Render.

📂 Dataset
The dataset is sourced from Kaggle and contains daily meteorological observations relevant to forest fire prediction in two Algerian regions.

📁 Included files:

Algerian_forest_fires_dataset_UPDATE.csv – raw dataset

Algerian_forest_fires_cleaned_dataset.csv – cleaned and preprocessed version

🧪 Feature Engineering & Preprocessing
Performed as documented in the notebook:
📓 Algerian forest - Ridge, Lasso Regression(1).ipynb

Steps included:

Removal of missing and inconsistent values

Conversion of categorical columns (e.g., region)

Feature correlation analysis and reduction

Scaling via StandardScaler

🤖 Model Training
Trained and evaluated the following regression models:

Linear Regression

Lasso Regression

Ridge Regression

ElasticNet Regression

✅ Ridge Regression was selected as the final model, achieving an R² score of 98.4% using cross-validation.

🧠 Final Model Artifacts
🔸 ridgecv.pkl – trained Ridge regression model

🔸 scaler.pkl – fitted StandardScaler used for input scaling

🌐 Flask Web Application
Built a simple yet functional web interface using Flask:

application.py: main backend script

index.html: form for user input (located in /templates)

Accepts numeric input, applies preprocessing, and displays the FWI prediction

▶️ Run Locally
bash
Copy
Edit
pip install -r requirements.txt
python application.py
Then open http://127.0.0.1:5000 in your browser.

🚀 Deployment
The web app has been deployed to Render:

🔗 Live App → https://algerian-forest-fire-predictor-7q2x.onrender.com/

👨‍💻 Author
Made with ❤️ by Sayanjib Sur
As part of a machine learning project to integrate model deployment into real-world applications.

🙌 Contribute
Feel free to fork, improve, or use this project as a template.
If you find it helpful, consider ⭐ starring the repo!

