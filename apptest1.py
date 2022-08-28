import streamlit as st
import numpy as np
import pandas as pd
import pickle

model = pickle.load(open('model.pkl','rb'))
X=pickle.load(open('X.pkl','rb'))

st.title("Calories Burning Tracker")

Gender = st.selectbox('Gender',['Male', 'Female'])

Age = st.slider ('Enter Age',12,100)

Height = st.select_slider('Enter Height (in Feets , Inches)', (3.0,3.1,3.2,3.3,3.4,3.5,3.6,3.7,3.8,3.9,3.10,3.11,3.12,4.0,4.1,4.2,4.3,4.4,4.5,4.6,4.7,4.8,4.9,4.10,4.11,4.12,5.0,5.1,5.2,5.3,5.4,5.5,5.6,5.7,5.8,5.9,5.10,5.11,5.12,6.0,6.1,6.2,6.3,6.4,6.5,6.6,6.7,6.8,6.9,6.10,6.11,6.12,7.0,7.1,7.2,7.3,7.4,7.5,7.6,7.7,7.8,7.9,7.10,7.11,7.12))

Weight = st.slider ('Enter Weight (in Kgs)',5,160)

Duration = st.slider ('Enter Duration of workout (in Minutes)',1,300)

Heart_Rate = st.slider ('Enter Heart Rate (Usually 60 bpm - 100 bpm)',50,120)

Body_Temp = st.slider ('Enter Body Temperature (in Celsius)',36,42)

if st.button('Track Calories'):
    if Gender == 'Male':
        Gender = 1
    else :
        Gender = 0    
    query = np.array([Gender, Age, Height,Weight,Duration, Heart_Rate, Body_Temp])
    query = query.reshape(1,7)
    print(query)
    var = str(model.predict(query)[0])
    if int(model.predict(query)[0]) < 125 :
        st.title("The Total Calories Burnt : " + str(model.predict(query)[0]))
        st.title("Poor Workout, TRAIN HARDER!")
    elif int(model.predict(query)[0]) < 175:
        st.title("The Total Calories Burnt : " + str(model.predict(query)[0]))
        st.title("Moderate Workout, KEEP GRINDING")
    else :
        st.title("The Total Calories Burnt : " + str(model.predict(query)[0]))
        st.title("Excellent Workout, KEEP IT UP")
