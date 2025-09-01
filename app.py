import streamlit as st
import pickle
import numpy as np

# ----------------------------
# 1. Load Trained Model
# ----------------------------
with open("trained_model.sav", "rb") as f:
    model = pickle.load(f)

# ----------------------------
# 2. App Title
# ----------------------------
st.title("👨‍💼 Employee Performance Predictor")
st.write("This app predicts an **Employee’s Performance Score** based on HR and productivity data.")

# ----------------------------
# 3. Input Features
# ----------------------------
 
department = st.number_input("Department (numeric code)", min_value=0, max_value=20, value=1)
gender = st.selectbox("Gender", [0, 1])  # 0 = Female, 1 = Male
age = st.number_input("Age", min_value=18, max_value=65, value=30)
job_title = st.number_input("Job Title (numeric code)", min_value=0, max_value=50, value=1)
years_at_company = st.number_input("Years at Company", min_value=0, max_value=40, value=5)

monthly_salary = st.number_input("Monthly Salary", min_value=1000.0, max_value=20000.0, value=5000.0)
work_hours = st.number_input("Work Hours per Week", min_value=20, max_value=80, value=40)
projects = st.number_input("Projects Handled", min_value=0, max_value=50, value=5)
overtime = st.number_input("Overtime Hours", min_value=0, max_value=100, value=10)
sick_days = st.number_input("Sick Days per Year", min_value=0, max_value=60, value=5)

remote_work = st.number_input("Remote Work Frequency (%)", min_value=0, max_value=100, value=50)
team_size = st.number_input("Team Size", min_value=1, max_value=100, value=10)
training_hours = st.number_input("Training Hours", min_value=0, max_value=500, value=20)
promotions = st.number_input("Number of Promotions", min_value=0, max_value=10, value=1)

satisfaction = st.number_input("Employee Satisfaction Score", min_value=0.0, max_value=5.0, value=3.0)
resigned = st.selectbox("Resigned", [0, 1])  # 0 = No, 1 = Yes
hire_year = st.number_input("Hire Year", min_value=1980, max_value=2025, value=2015)
hire_day = st.number_input("Hire Day of Month", min_value=1, max_value=31, value=15)

# ----------------------------
# 4. Prediction
# ----------------------------
if st.button("🔮 Predict Performance"):
    features = np.array([[department, gender, age, job_title, years_at_company,
                          monthly_salary, work_hours, projects, overtime, sick_days,
                          remote_work, team_size, training_hours, promotions,
                          satisfaction, resigned, hire_year, hire_day]])
    
    prediction = model.predict(features)
    st.success(f"✅ Predicted Performance Score: **{prediction[0]}**")
