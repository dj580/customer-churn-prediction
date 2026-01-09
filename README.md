# Customer Churn Prediction – Mini AI Project

## Overview
This project predicts whether a customer is likely to churn based on demographic and service usage data.  
The solution includes data preprocessing, model training, evaluation, and deployment using a Flask API.

---

## Dataset
Telco Customer Churn dataset containing customer demographics, services, and billing information.

---

## Model Used
- Logistic Regression (Final Model)
- Random Forest (Model comparison)

**Why Logistic Regression?**
- Better Recall and F1-score
- Suitable for binary classification
- Interpretable feature coefficients

---

## Preprocessing Steps
- Converted target variable (Churn) to binary (0/1)
- One-hot encoded categorical variables
- Scaled numerical features:
  - tenure
  - MonthlyCharges
  - TotalCharges
- Prevented data leakage by fitting scalers only on training data

---

## Feature Impact
- Long tenure and long-term contracts reduce churn
- High monthly charges and fiber optic internet increase churn
- Support services such as OnlineSecurity and TechSupport reduce churn

---

## API (Flask Deployment)

### Endpoint
**POST** `/predict`

### Input Format (Raw Data)
```json
{
  "gender": "Male",
  "SeniorCitizen": 0,
  "Partner": "Yes",
  "Dependents": "No",
  "tenure": 12,
  "PhoneService": "Yes",
  "MultipleLines": "No",
  "InternetService": "Fiber optic",
  "OnlineSecurity": "No",
  "DeviceProtection": "Yes",
  "TechSupport": "No",
  "StreamingTV": "Yes",
  "StreamingMovies": "No",
  "Contract": "Month-to-month",
  "PaperlessBilling": "Yes",
  "PaymentMethod": "Electronic check",
  "MonthlyCharges": 70.5,
  "TotalCharges": 850.4
}
