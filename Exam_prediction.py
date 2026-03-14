import streamlit as st
import joblib
import numpy as np
import pandas as pd

# load model
model = joblib.load('model_exam_prediction.pkl')

st.title("Exam Score Prediction")

st.write("Masukkan data siswa untuk memprediksi nilai ujian")

# input user
Hours_Studied = st.number_input("Hours Studied (in weeks)", 0)
Attendance = st.number_input("Attendance (%)", 0)
Sleep_Hours = st.number_input("Sleep Hours (hours)", 0)
Previous_Scores = st.number_input("Previous Scores", 0)
Tutoring_Sessions = st.number_input("Tutoring Sessions (in weeks)", 0)
Physical_Activity = st.number_input("Physical Activity (in weeks)", 0)

# INPUT KATEGORIK (DIUBAH JADI ANGKA)
Parental_Involvement = st.selectbox("Parental Involvement", ['Low', 'Medium', 'High'])


Access_to_Resources = st.selectbox("Access to Resources", ['Low', 'Medium', 'High'])


Motivation_Level = st.selectbox("Motivation Level", ['Low', 'Medium', 'High'])


Family_Income = st.selectbox("Family Income", ['Low', 'Medium', 'High'])


Teacher_Quality = st.selectbox("Teacher Quality", ['Low', 'Medium', 'High'])


Peer_Influence = st.selectbox("Peer Influence", ['Negative', 'Neutral', 'Positive'])


Parental_Education_Level = st.selectbox("Parental Education Level", ['High School', 'College', 'Postgraduate'])


Gender = st.selectbox("Gender", ['Female','Male'])

Internet_Access = st.selectbox("Internet Access", ['No', 'Yes'])


Extracurricular_Activities = st.selectbox("Extracurricular Activities", ['No', 'Yes'])


Learning_Disabilities = st.selectbox("Learning Disabilities", ['No', 'Yes'])


School_Type = st.selectbox("School Type", ['Private', 'Public'])


Distance_from_Home = st.selectbox("Distance from Home", ['Near', 'Moderate', 'Far'])


input_data = pd.DataFrame({
    "Hours_Studied":[Hours_Studied],
    "Attendance":[Attendance],
    "Sleep_Hours":[Sleep_Hours],
    "Previous_Scores":[Previous_Scores],
    "Tutoring_Sessions":[Tutoring_Sessions],
    "Physical_Activity":[Physical_Activity],

    "Parental_Involvement":[Parental_Involvement],
    "Access_to_Resources":[Access_to_Resources],
    "Motivation_Level":[Motivation_Level],
    "Family_Income":[Family_Income],
    "Teacher_Quality":[Teacher_Quality],
    "Peer_Influence":[Peer_Influence],
    "Parental_Education_Level":[Parental_Education_Level],
    "Distance_from_Home":[Distance_from_Home],

    "Gender":[Gender],
    "Internet_Access":[Internet_Access],
    "Extracurricular_Activities":[Extracurricular_Activities],
    "Learning_Disabilities":[Learning_Disabilities],
    "School_Type":[School_Type]
})

# tombol prediksi
if st.button("Predict Exam Score"):
    
    prediction = model.predict(input_data)

    st.success(f"Predicted Exam Score: {prediction[0]:.2f}")