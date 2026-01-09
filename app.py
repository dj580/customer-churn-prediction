from flask import Flask, request, jsonify
import pandas as pd
import joblib

app = Flask(__name__)

# Load model and scaler
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

# Feature names learned during training
FEATURE_NAMES = model.feature_names_in_

# Columns
YES_NO_COLS = [
    "Partner", "Dependents", "PhoneService",
    "PaperlessBilling", "OnlineSecurity",
    "DeviceProtection", "TechSupport",
    "StreamingTV", "StreamingMovies"
]

NUM_COLS = ["tenure", "MonthlyCharges", "TotalCharges"]


@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json
        df = pd.DataFrame([data])

        # Fix Yes/No columns (CORRECT WAY)
        for col in YES_NO_COLS:
            df[col] = (
                df[col]
                .astype(str)
                .str.strip()
                .str.capitalize()
                .replace({"Yes": 1, "No": 0})
            )

        # One-hot encode
        df = pd.get_dummies(df)

        # Align with training features
        df = df.reindex(columns=FEATURE_NAMES, fill_value=0)

        # Scale numeric columns only
        df[NUM_COLS] = scaler.transform(df[NUM_COLS])

        prediction = model.predict(df)[0]

        return jsonify({
            "Churn_Prediction": int(prediction),
            "Meaning": "Churn" if prediction == 1 else "No Churn"
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
