import streamlit as st
import pandas as pd
import joblib
import numpy as np

# --- PAGE CONFIG ---
st.set_page_config(page_title="Crypto Rug Pull Detector", layout="wide")

# --- LOAD MODEL ---
# We use a cache so the model doesn't reload every time you click a button
@st.cache_resource
def load_model():
    return joblib.load('rug_pull_detector.pkl')

model = load_model()

# --- SIDEBAR ---
st.sidebar.title("About This Project")
st.sidebar.info(
    "This app uses Machine Learning (XGBoost) to detect potential "
    "crypto scams ('Rug Pulls') based on transaction patterns. "
    "Trained on the Elliptic Dataset."
)

# --- MAIN PAGE ---
st.title("🔍 Crypto Transaction Forensics")
st.write("Upload a CSV file of transaction features to detect potential fraud.")

# --- FILE UPLOADER ---
uploaded_file = st.file_uploader("Upload Transaction CSV", type=["csv"])

if uploaded_file is not None:
    # Read the file
    input_df = pd.read_csv(uploaded_file)
    
    st.subheader("1. Input Data Preview")
    st.write(f"Found {input_df.shape[0]} transactions.")
    st.dataframe(input_df.head(5))

    # Prediction Button
    if st.button("Analyze for Scams"):
        with st.spinner('Analyzing patterns...'):
            # Make Predictions
            predictions = model.predict(input_df)
            prediction_probs = model.predict_proba(input_df)
            
            # Create a results dataframe
            results = input_df.copy()
            results['Prediction'] = predictions
            results['Risk Score'] = prediction_probs[:, 1] # Probability of being class 1 (Scam)
            
            # Map 0/1 to text
            results['Status'] = results['Prediction'].map({0: '✅ Legit', 1: '🚨 SCAM'})
            
            # Display Results
            st.subheader("2. Analysis Results")
            
            # Color coding
            def highlight_scam(val):
                color = 'red' if val == '🚨 SCAM' else 'green'
                return f'color: {color}'

            st.dataframe(results[['Status', 'Risk Score']].style.applymap(highlight_scam, subset=['Status']))
            
            # Stats
            scam_count = (predictions == 1).sum()
            st.warning(f"⚠️ Detected {scam_count} suspicious transactions out of {len(predictions)}.")
            
else:
    st.info("Awaiting CSV file upload. (Try uploading 'test_transactions.csv')")

# --- FOOTER ---
st.markdown("---")
st.caption("Data Science Portfolio Project | Blockchain Forensics")