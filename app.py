from flask import Flask, render_template, request
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

app = Flask(__name__)

df = pd.read_csv('heatwave.csv')
X = df[['MaxTemp','MinTemp','Humidity','WindSpeed','Pressure','HistAvgTemp']]
y = df['Heatwave']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        input_features = [
            float(request.form.get("MaxTemp")),
            float(request.form.get("MinTemp")),
            float(request.form.get("Humidity")),
            float(request.form.get("WindSpeed")),
            float(request.form.get("Pressure")),
            float(request.form.get("HistAvgTemp")),
        ]
        prediction = model.predict([input_features])[0]

        if prediction <= 0.25:
            pred = 'Low Risk'
        elif prediction >= 0.25 and prediction <= 0.6:
            pred = 'Moderate Risk'
        else:
            pred = 'High Risk — Heatwave Likely'

        return render_template("index.html", prediction_text=pred)
    except:
        return render_template("index.html", prediction_text="Error: Please enter valid numeric values.")

if __name__ == "__main__":
    app.run(debug=True)
