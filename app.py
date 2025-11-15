import streamlit as st
import pandas as pd
import joblib
import os

st.title("🎓 Student Exam Score Prediction (Regression Model)")
st.write("Predict a student's expected exam score based on lifestyle and academic factors.")

MODEL_PATH = "best_model.pkl"

# Load model
if not os.path.exists(MODEL_PATH):
    st.error("Model not found! Please upload best_model.pkl.")
    st.stop()

model = joblib.load(MODEL_PATH)

# ---------------------------
# INPUT FIELDS (ONLY 6 FEATURES)
# ---------------------------

hours = st.slider("Hours Studied", 0, 10, 5)
attendance = st.slider("Attendance (%)", 0, 100, 80)
sleep_hours = st.slider("Sleep Hours", 0, 12, 7)

internet = st.selectbox("Internet Access", ["Yes", "No"])
parent_edu = st.selectbox("Parental Education Level", ["High School", "College", "Postgraduate"])
gender = st.selectbox("Gender", ["Male", "Female"])

# Encoding – must match training
encode = {
    "Yes": 1, "No": 0,
    "High School": 0, "College": 1, "Postgraduate": 2,
    "Male": 1, "Female": 0
}

# Create input dataframe EXACTLY LIKE TRAINING
input_df = pd.DataFrame({
    "Hours_Studied": [hours],
    "Attendance": [attendance],
    "Sleep_Hours": [sleep_hours],
    "Internet_Access": [encode[internet]],
    "Parental_Education_Level": [encode[parent_edu]],
    "Gender": [encode[gender]]
})

st.subheader("📝 Input Preview")
st.write(input_df)

# ---------------------------
# PREDICT BUTTON
# ---------------------------

if st.button("Predict Score"):
    pred = model.predict(input_df)[0]
    st.success(f"🎯 Predicted Exam Score: **{pred:.2f}**")
