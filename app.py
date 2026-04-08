import streamlit as st 
from main import model
import pandas as pd

def main():
    st.title("Diabetes AI")
    st.write("This is a simple app to predict whether or not a person has diabetes based on their health data.")
    st.write("note this is a AI and it can make mistakes so if you are in doubt go to a dockter!") 

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
        
        if prediction > 15: 
            st.write(f"The change of diabetes is {prediction}% we recommend you to see a docter!")
        else:
            st.write("The change that you have diabetes is low. But that will not say that you cant get it. ")

if __name__ == "__main__":
    main()

# streamlit run app.py