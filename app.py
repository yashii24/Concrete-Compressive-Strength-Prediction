import streamlit as st
import joblib
import numpy as np

model = joblib.load("model/concrete_strength_model.pkl")

st.title("🏗️ Concrete Compressive Strength Predictor")

st.write("Enter material values:")

cement = st.number_input("Cement")
slag = st.number_input("Blast Furnace Slag")
flyash = st.number_input("Fly Ash")
water = st.number_input("Water")
superplasticizer = st.number_input("Superplasticizer")
coarse = st.number_input("Coarse Aggregate")
fine = st.number_input("Fine Aggregate")
age = st.number_input("Age (days)")

if st.button("Predict"):
    input_data = np.array([[cement, slag, flyash, water,
                            superplasticizer, coarse, fine, age]])

    prediction = model.predict(input_data)

    st.success(f"Predicted Strength: {prediction[0]:.2f} MPa")
