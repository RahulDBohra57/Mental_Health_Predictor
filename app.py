import numpy as np
import pandas as pd
import streamlit as st 
import joblib

# Lets load the model
with open('final_model.joblib','rb') as file:
    model = joblib.load(file)

# Lets create the App UI/UX
st.title('MENTAL HEALTH PREDICTOR')
st.header(':blue[This application will predict if you require professional support for mental issues.]')

# Lets Take input from the user
Gender = (lambda x: 0 if x=='Female' else 1) (st.selectbox('Please select your gender:',['Male','Female']))
Country = (lambda x: 34 if x=='United States' else 
           33 if x=='United Kingdom' else
           4 if x=='Canada' else
           0 if x=='Australia' else
           21 if x=='Netherlands' else
           16 if x=='Ireland' else
           13 if x=='Germany' else
           30 if x=='Sweden' else
           15 if x=='India' else
           11 if x=='France' else
           3 if x=='Brazil' else
           22 if x=='New Zealand' else
           29 if x=='South Africa' else
           31 if x=='Switzerland' else
           17 if x=='Israel' else
           18 if x=='Italy' else
           1 if x=='Belgium' else
           25 if x=='Poland' else
           27 if x=='Russia' else
           9 if x=='Denmark' else
           28 if x=='Singapore' else
           14 if x=='Greece' else
           8 if x=='Czech Republic' else
           12 if x=='Georgia' else
           5 if x=='Colombia' else
           20 if x=='Moldova' else
           19 if x=='Mexico' else
           7 if x=='Croatia' else
           32 if x=='Thailand' else
           23 if x=='Nigeria' else
           2 if x=='Bosnia and Herzegovina' else
           26 if x=='Portugal' else
           10 if x=='Finland' else
           6 if x=='Costa Rica' else
           24) (st.selectbox('Please select your country:',['United States','United Kingdom','Canada','Australia','Netherlands','Ireland','Germany','Sweden','India','France','Brazil','New Zealand','South Africa','Switzerland' ,'Israel','Italy' ,'Belgium','Poland' ,'Russia','Denmark' ,'Singapore','Greece','Czech Republic' ,'Georgia','Colombia','Moldova','Mexico','Croatia' ,'Thailand','Nigeria' ,'Bosnia and Herzegovina' ,'Portugal','Finland' ,'Costa Rica']))
Occupation = (lambda x: 2 if x=='Housewife' else
              4 if x=='Student' else
              1 if x=='Corporate' else
              0 if x=='Business' else
              3) (st.selectbox('Please select your occupation:',['Business','Corporate','Housewife','Student','Other']))
self_employed= (lambda x: 0 if x=='No' else 1) (st.selectbox('Are you self-employed?',['Yes','No']))
family_history= (lambda x: 0 if x=='No' else 1) (st.selectbox('Do you have a family history of mental health issues?',['Yes','No']))
Days_Indoors = (lambda x: 0 if x=='1-14 days' else
                1 if x=='15-30 days' else
                2 if x=='31-60 days' else
                3 if x=='Go out Every day' else
                4) (st.selectbox('How often you go out of the house?',['Go out Every day','1-14 days','15-30 days','31-60 days','More than 2 months']))
Growing_Stress = (lambda x: 0 if x=='Maybe' else
                2 if x=='Yes' else
                1) (st.selectbox('Have you been experiencing growing stress in work lately?',['Yes','No','Maybe']))
Mental_Health_History=(lambda x: 0 if x=='Maybe' else
                2 if x=='Yes' else
                1) (st.selectbox('Have you been through any mental health issues in past?',['Yes','No','Maybe']))
Mood_Swings=(lambda x: 1 if x=='Never' else
                2 if x=='Occassionally' else
                0) (st.selectbox('How often you experience mood swings?',['Very Often','Occassionally','Never']))
Coping_Struggles=(lambda x: 0 if x=='Maybe' else
                1 if x=='Yes' else
                0) (st.selectbox('Have you been experiencing like coping with struggles lately?',['Yes','No']))
Work_Interest=(lambda x: 0 if x=='Maybe' else
                2 if x=='Yes' else
                1) (st.selectbox('Are your working/studying in a field of your interest?',['Yes','No','Maybe']))
mental_health_interview= (lambda x: 1 if x=='No' else
                2 if x=='Yes' else
                0) (st.selectbox('Would you bring up a mental health issue with a potential employer in an interview?',['Yes','No','Maybe']))
care_options= (lambda x: 1 if x=='Not sure' else
                2 if x=='Yes' else
                0) (st.selectbox('Are you utilizing any mental health care options available in your country?',['Yes','No','Not sure']))

# Create the imput list 
input_list = [Gender, Country, Occupation, self_employed, family_history, Days_Indoors, Growing_Stress, Mental_Health_History, 
              Mood_Swings, Coping_Struggles, Work_Interest, mental_health_interview, care_options]

# Make prediction
prediction = model.predict_proba([input_list])[:,1]

# Lets show the probability
if st.button('Predict'):
    pred_value = float(prediction)
    if pred_value >= 0.5:
        st.error(f'Chances of Mental Health Support required: {round(pred_value,2) * 100}%')
    else:
        st.success(f'Chances of Mental Health Support required: {round(pred_value,2) * 100}%')