# 🎓 Student Performance Prediction (Regression Model)

This project predicts a student's **exam score** based on lifestyle, academic, and personal factors.  
It uses **Machine Learning (Regression)** and is deployed as an interactive **Streamlit Web App**.

---

## 🔗 Live Demo

👉 Try the online prediction app:  
[Student Performance Prediction – Streamlit App](https://student-performance-prediction-hkaslaqtc33er7s82osvfi.streamlit.app/)

---

## 🧠 Problem Motivation

Students’ academic performance is influenced by many factors such as study hours, attendance,
sleep, and motivation.  
The goal of this project is to:

- Help students understand which factors impact their performance.
- Provide an early prediction of their expected exam score.
- Assist teachers and parents in identifying at-risk students.

---

## 🧾 Dataset

- **Name:** Student Performance Factors Dataset  
- **Type:** Tabular data (CSV)  
- **Target Variable:** `Exam_Score` (continuous value – regression)  
- **Example Features:**
  - Hours Studied  
  - Attendance  
  - Sleep Hours  
  - Internet Access  
  - Parental Education Level  
  - Gender  
  - Motivation Level  

> The dataset was cleaned, preprocessed, and used to train a regression model to predict the exam score.

---

## 🧮 Machine Learning Approach

1. **Exploratory Data Analysis (EDA)**
   - Checked missing values and outliers.
   - Visualized distributions and correlations between features and exam score.

2. **Data Preprocessing**
   - Handled missing values.
   - Encoded categorical variables (e.g., gender, parental education).
   - Scaled numerical features where needed.
   - Split data into **train** and **test** sets.

3. **Models Tried**
   - Linear Regression  
   - Random Forest Regressor  
   - XGBoost Regressor *(optional if you used it)*  

4. **Model Evaluation**
   - Metrics: **R² Score**, **Mean Absolute Error (MAE)**, **Root Mean Squared Error (RMSE)**.
   - Selected the best model based on test performance.
   - Saved the final model to `best_model.pkl`.

---

##  Application Architecture

'''text

Dataset (CSV)
   ↓
Data Preprocessing & Model Training (Notebook / Script)
   ↓
Trained Model → best_model.pkl
   ↓
Streamlit Web App (app.py)
   ↓
User inputs features → Predicted Exam Score




## Tech Stack

	•	Language: Python
	•	Web App: Streamlit
	•	ML Libraries: scikit-learn, pandas, numpy
	•	Visualization: matplotlib / seaborn
	•	Model Storage: pickle (best_model.pkl)
	•	Deployment: Streamlit Cloud

## Project Files

•	app.py – Streamlit app (UI + prediction logic)
	•	best_model.pkl – Saved regression model
	•	requirements.txt – Python dependencies
	•	README.md – Project documentation (this file)

## How to Run Locally
# 1. Clone the repository
git clone https://github.com/Rameshreddymusku/student-performance-prediction.git
cd student-performance-prediction

# 2. Create & activate virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the Streamlit app
streamlit run app.py



