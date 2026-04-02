import pandas as pd
import numpy as np 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


df = pd.read_csv('data/diabetes.csv')

df['Glucose'] = df['Glucose'].replace(0, np.nan) # if there is a 0 that that will be replaced with the avarege 
df['Glucose'] = df['Glucose'].fillna(df['Glucose'].median())

df['BloodPressure'] = df['BloodPressure'].replace(0, np.nan)
df['BloodPressure'] = df['BloodPressure'].fillna(df['BloodPressure'].median())

df['SkinThickness'] = df['SkinThickness'].replace(0, np.nan)
df['SkinThickness'] = df['SkinThickness'].fillna(df['SkinThickness'].median())

df['Insulin'] = df['Insulin'].replace(0, np.nan)
df['Insulin'] = df['Insulin'].fillna(df['Insulin'].median())

df['BMI'] = df['BMI'].replace(0, np.nan)
df['BMI'] = df['BMI'].fillna(df['BMI'].median())

X = df[['BMI', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'Pregnancies', 'DiabetesPedigreeFunction', 'Age']] #everything except the outcome
y = df['Outcome'] # Outcome

X_train, X_test, y_train, y_test = train_test_split(X,y ,
                                   random_state=104, # need to dive deeper in to that 
                                   test_size=0.25, # you do 768%100*25 = 0.25
                                   shuffle=True) # shuffels the data 

model = RandomForestClassifier(
    n_estimators=200,
    max_depth=5,
    random_state=42,
    class_weight='balanced'
) # if you have unbalanced data you can use that to balance it

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

score = accuracy_score(y_test, y_pred)


print(score)
print(y.value_counts())