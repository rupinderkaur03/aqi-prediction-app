import streamlit as st
import joblib
import numpy as np

model = joblib.load("rf (2).pkl")

st.title("AQI Prediction App 🌍")

pm25 = st.number_input("PM2.5")
pm10 = st.number_input("PM10")
no2 = st.number_input("NO2")
co = st.number_input("CO")
temp = st.number_input("Temperature")

location = st.selectbox("Location", [
    "Anand Vihar",
    "Connaught Place",
    "Dwarka",
    "IGI Airport",
    "Okhla Phase III",
    "Rohini"
])

# One-hot encoding (same as training)
loc_CP = 1 if location == "Connaught Place" else 0
loc_Dwarka = 1 if location == "Dwarka" else 0
loc_IGI = 1 if location == "IGI Airport" else 0
loc_Okhla = 1 if location == "Okhla Phase III" else 0
loc_Rohini = 1 if location == "Rohini" else 0

if st.button("Predict AQI"):
    features = np.array([[ 
        pm25, pm10, no2, co, temp,
        loc_CP, loc_Dwarka, loc_IGI, loc_Okhla, loc_Rohini
    ]])

    prediction = model.predict(features)[0]

    if prediction <= 50:
        category = "Good"
    elif prediction <= 100:
        category = "Satisfactory"
    elif prediction <= 200:
        category = "Moderate"
    elif prediction <= 300:
        category = "Poor"
    elif prediction <= 400:
        category = "Very Poor"
    else:
        category = "Severe"

    st.success(f"AQI: {prediction:.2f}")
    st.write(f"Category: {category}")