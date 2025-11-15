import streamlit as st
import pandas as pd
import joblib
import os

st.title("🎓 Student Exam Score Prediction (Regression Model)")
st.write("Predict a student's expected exam score based on lifestyle and academic factors.")

MODEL_PATH = os.path.join("..", "models", "best_model.pkl")

if not os.path.exists(MODEL_PATH):
    st.warning("Model not found. Please train it first using the notebook in the 'notebooks' folder.")
else:
    model = joblib.load(MODEL_PATH)

    st.subheader("Enter Student Details")

    hours_studied = st.slider("Hours Studied", 0.0, 10.0, 5.0, step=0.5)
    attendance = st.slider("Attendance (%)", 0, 100, 80)
    parental_involvement = st.selectbox("Parental Involvement", ["Low", "Medium", "High"])
    sleep_hours = st.slider("Sleep Hours", 0.0, 12.0, 7.0, step=0.5)
    motivation = st.slider("Motivation Level (1-10)", 1, 10, 5)

    mapping = {"Low": 0, "Medium": 1, "High": 2}

    input_df = pd.DataFrame({
        "Hours_Studied": [hours_studied],
        "Attendance": [attendance],
        "Parental_Involvement": [mapping[parental_involvement]],
        "Sleep_Hours": [sleep_hours],
        "Motivation_Level": [motivation]
    })

    st.write("Input Preview:")
    st.dataframe(input_df)

    if st.button("Predict Score"):
        pred = model.predict(input_df)[0]
        st.success(f"📊 Predicted Exam Score: {pred:.2f}")
