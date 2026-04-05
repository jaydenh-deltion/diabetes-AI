import streamlit as st 

def main():
    st.title("Diabetes AI")
    st.write("This is a simple app that uses a random forest classifier to predict whether or not a person has diabetes based on their health data.") 

    glucose = st.number_input("Please enter the Glucose level:")
    blood_pressure = st.number_input("Please enter the Blood Pressure level:")
    skin_thickness = st.number_input("Please enter the Skin Thickness level:")
    insulin = st.number_input("Please enter the Insulin level:")
    bmi = st.number_input("Please enter the BMI level:")
    pregnancies = st.number_input("Please enter the number of Pregnancies:")
    diabetes_pedigree_function = st.number_input("Please enter the Diabetes Pedigree Function level:")
    age = st.number_input("Please enter the Age:")


if __name__ == "__main__":
    main()
# streamlit run app.py