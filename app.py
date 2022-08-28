import streamlit as st
import numpy as np
import pandas as pd
import pickle

model = pickle.load(open('model.pkl','rb'))
X=pickle.load(open('X.pkl','rb'))

st.title("Calories Burning Tracker")

Gender = st.selectbox('Gender',['Male', 'Female'])

Age = st.number_input ('Enter Age',min_value=18,max_value=100)

Height = st.number_input ('Enter Height (in)')

Weight = st.number_input ('Enter Weight (in Kgs)')

Duration = st.number_input ('Enter Duration of workout (in Minutes)')

Heart_Rate = st.number_input ('Enter Heart Rate (Usually 60 bpm - 100 bpm)')

Body_Temp = st.number_input ('Enter Body Temperature (in Celsius)')

if st.button('Track Calories'):
    if Gender == 'Male':
        Gender = 1
    else :
        Gender = 0    
    query = np.array([Gender, Age, Height,Weight,Duration, Heart_Rate, Body_Temp])
    query = query.reshape(1,7)
    print(query)
    st.title("The Total Calories Burnt : " + str(model.predict(query)[0]))