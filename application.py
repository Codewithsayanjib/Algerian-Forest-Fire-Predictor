from flask import Flask, request, redirect, url_for, render_template
import pickle
import numpy as np

application = Flask(__name__)

# Load model and scaler
scaler = pickle.load(open('scaler.pkl', 'rb'))
model = pickle.load(open('ridgecv.pkl', 'rb'))

@application.route('/')
def home():
    return render_template('Algerian forest fire index.html')

@application.route('/predict', methods=['POST'])
def predict():
    try:
        features = [float(x) for x in request.form.values()]
        if len(features) != 9:
            return redirect(url_for('home') + "?prediction=Invalid+input")
        scaled = scaler.transform([features])
        prediction = model.predict(scaled)[0]
        return redirect(url_for('home') + f"?prediction={prediction:.2f}")
    except Exception as e:
        return redirect(url_for('home') + f"?prediction=Error:+{str(e)}")

if __name__ == '__main__':
    application.run(debug=True)



