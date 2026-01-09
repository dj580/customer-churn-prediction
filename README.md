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
```

## Setup Instructions

##1. Clone the repository

```git clone https://github.com/dj580/customer-churn-prediction.git ```
---
##2. Navigate to the project folder

```cd customer-churn-prediction```
---
##3.Install required dependencies

```pip install -r requirements.txt```
---
##4.Run the Flask application
```python app.py```

The API will run at:http://127.0.0.1:5000
You can test the /predict endpoint using tools like Thunder Client


