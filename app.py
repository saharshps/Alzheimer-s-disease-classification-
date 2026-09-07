import pickle

import streamlit as st
import numpy as np

# Load model
model = pickle.load(open('alzheimer_model.pkl', 'rb'))

# Title
st.title("Alzheimer's Disease Prediction App")
st.write("Enter patient details below to predict Alzheimer's Disease")

# Inputs
mmse = st.number_input("MMSE Score (0-30)", min_value=0, max_value=30)
functional = st.number_input("Functional Assessment (0-10)", min_value=0, max_value=10)
adl = st.number_input("ADL Score (0-10)", min_value=0, max_value=10)
memory = st.selectbox("Memory Complaints", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
behavioral = st.selectbox("Behavioral Problems", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")

# Predict Button
if st.button("Predict"):
    data = np.array([[mmse, functional, adl, memory, behavioral]])
    result = model.predict(data)

    if result[0] == 1:
        st.error("⚠️ Alzheimer's Disease Detected")
        st.write("Please consult a doctor immediately")
    else:
        st.success("✅ No Alzheimer's Disease Detected")
        st.write("Patient appears healthy")