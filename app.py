import streamlit as st 
from main import model
import pandas as pd

def main():
    st.title("Diabetes AI")
    st.write("This is a simple app that uses a random forest classifier to predict whether or not a person has diabetes based on their health data.") 

    Glucose = st.number_input("Please enter the Glucose level:")
    BloodPressure = st.number_input("Please enter the Blood Pressure level:")
    SkinThickness = st.number_input("Please enter the Skin fold thickness (mm):")
    Insulin = st.number_input("Please enter the Insulin level:")
    BMI = st.number_input("Please enter the BMI level:")
    Pregnancies = st.number_input("Please enter the number of Pregnancies:")
    DiabetesPedigreeFunction = st.number_input("Please enter the Family history of diabetes (0.0 - 2.5)")
    Age = st.number_input("Please enter the Age:")


    if st.button("Predict Diabetes"):
        df = pd.DataFrame([[BMI,Glucose, BloodPressure, SkinThickness, Insulin, Pregnancies, DiabetesPedigreeFunction, Age ]], columns=['BMI','Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'Pregnancies', 'DiabetesPedigreeFunction', 'Age'])
        prediction = model.predict_proba(df)
        prediction = round(prediction[0][1] * 100)
        st.write(f"This patient has a %{prediction} chance of diabetes. Please consult a doctor.") 

if __name__ == "__main__":
    main()
# streamlit run app.py