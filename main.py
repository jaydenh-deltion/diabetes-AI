import pandas as pd
import numpy as np 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier



df = pd.read_csv('data/diabetes.csv')
print(df.head())


df['Glucose'] = df['Glucose'].replace(0, np.nan) # if there is a 0 that that will be replaced with the avarege 
df['Glucose'] = df['Glucose'].fillna(df['Glucose'].mean())

df['BloodPressure'] = df['BloodPressure'].replace(0, np.nan)
df['BloodPressure'] = df['BloodPressure'].fillna(df['BloodPressure'].mean())

df['SkinThickness'] = df['SkinThickness'].replace(0, np.nan)
df['SkinThickness'] = df['SkinThickness'].fillna(df['SkinThickness'].mean())

df['Insulin'] = df['Insulin'].replace(0, np.nan)
df['Insulin'] = df['Insulin'].fillna(df['Insulin'].mean())

df['BMI'] = df['BMI'].replace(0, np.nan)
df['BMI'] = df['BMI'].fillna(df['BMI'].mean())


X = df[['BMI', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'Pregnancies', 'DiabetesPedigreeFunction', 'Age']] #everything except the outcome
y = df['Outcome'] # Outcome

X_train, X_test, y_train, y_test = train_test_split(X,y ,
                                   random_state=104, # need to dive deeper in to that 
                                   test_size=0.25, # you do 768%100*25 
                                   shuffle=True) # shuffels the data 




print(df['Glucose'] == 0)
print(df['BloodPressure'] == 0)
print(df['SkinThickness'] == 0)
print(df['Insulin'] == 0)
print(df['BMI'] == 0)
