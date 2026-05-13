import pandas as pd
import joblib

# Load model and columns
model = joblib.load("model.pkl")
columns = joblib.load("columns.pkl")

def predict(data):
    # Convert input into DataFrame
    df = pd.DataFrame([data])

    # Convert categorical columns
    df = pd.get_dummies(df)

    # Match training columns
    df = df.reindex(columns=columns, fill_value=0)

    # Make prediction
    prediction = model.predict(df)[0]

    # Return result
    return "Fraud" if prediction == 1 else "Not Fraud"


# Sample transaction for testing
sample = {
    "step": 1,
    "amount": 1000,
    "oldbalanceOrg": 5000,
    "newbalanceOrig": 4000,
    "oldbalanceDest": 0,
    "newbalanceDest": 1000,
    "type_TRANSFER": 1,
    "type_CASH_OUT": 0,
    "type_DEBIT": 0,
    "type_PAYMENT": 0
}

# Print prediction
print(predict(sample))
