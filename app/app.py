import streamlit as st
import pandas as pd
import joblib

# Load model and columns
model = joblib.load("../src/model.pkl")
columns = joblib.load("../src/columns.pkl")

st.title("💳 Fraud Detection App")

st.write("Enter transaction details below:")

# User Inputs
step = st.number_input("Step", min_value=1, value=1)
amount = st.number_input("Amount", min_value=0.0, value=1000.0)
oldbalanceOrg = st.number_input("Old Balance Origin", min_value=0.0, value=5000.0)
newbalanceOrig = st.number_input("New Balance Origin", min_value=0.0, value=4000.0)
oldbalanceDest = st.number_input("Old Balance Destination", min_value=0.0, value=0.0)
newbalanceDest = st.number_input("New Balance Destination", min_value=0.0, value=1000.0)

transaction_type = st.selectbox(
    "Transaction Type",
    ["TRANSFER", "CASH_OUT", "DEBIT", "PAYMENT"]
)

# Predict button
if st.button("Predict Fraud"):

    data = {
        "step": step,
        "amount": amount,
        "oldbalanceOrg": oldbalanceOrg,
        "newbalanceOrig": newbalanceOrig,
        "oldbalanceDest": oldbalanceDest,
        "newbalanceDest": newbalanceDest,
        "type_TRANSFER": 1 if transaction_type == "TRANSFER" else 0,
        "type_CASH_OUT": 1 if transaction_type == "CASH_OUT" else 0,
        "type_DEBIT": 1 if transaction_type == "DEBIT" else 0,
        "type_PAYMENT": 1 if transaction_type == "PAYMENT" else 0
    }

    df = pd.DataFrame([data])

    # Match columns
    df = df.reindex(columns=columns, fill_value=0)

    prediction = model.predict(df)[0]

    if prediction == 1:
        st.error("⚠️ Fraudulent Transaction Detected!")
    else:
        st.success("✅ Transaction is Not Fraud")
