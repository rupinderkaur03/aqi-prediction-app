# 🌍 AQI Prediction App

🚀 Live Demo: https://aqi-prediction-app-svnpxmqj7rj5gsbl7nbg3n.streamlit.app/

---

## 📌 Project Overview

This project predicts the **Air Quality Index (AQI)** using Machine Learning based on pollution and weather parameters.

It helps in understanding air quality levels and categorizing them into health-based levels like Good, Moderate, Poor, etc.

---

## 🎯 Problem Statement

Air pollution is increasing rapidly, and real-time AQI prediction is important for public awareness and preventive measures.

This project aims to build a predictive model that estimates AQI based on environmental features.

---

## 📊 Features Used

- PM2.5  
- PM10  
- NO₂  
- CO  
- Temperature  
- Location  

---

## 🤖 Machine Learning Model

- Model Used: **Random Forest Regressor**
- Feature Engineering: One-hot encoding for location
- Model Optimization: Reduced features for better performance and deployment

---

## 🛠️ Tech Stack

- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- Streamlit  

---

## 💻 Web App Features

- User-friendly interface  
- Input pollution parameters  
- Select location  
- Predict AQI instantly  
- Displays AQI category (Good, Moderate, Severe, etc.)

---

## 🚀 How to Run Locally

```bash
git clone https://github.com/your-username/aqi-prediction-app.git
cd aqi-prediction-app
pip install -r requirements.txt
streamlit run app.py
