import streamlit as st
import pandas as pd
import pickle
#Load the model
with open("classifier.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Weather Classification")
temparature = st.number_input(label="Temparature")
humidity = st.number_input(label="Humidity")
wind_speed = st.number_input(label="Wind Speed")
Precipitation = st.number_input(label="Precipitation (%)")
CloudCover = st.selectbox(label="Cloud Cover", options=["Overcast","Partly Cloudy", "Clear","Cloudy"])
AtmosphericPressure = st.number_input(label="Atmospheric Pressure")
UVindex = st.number_input(label="UV Index")
Season = st.selectbox(label="Season", options=["Winter", "Spring", "Summer", "Autumn"])
Visibility = st.number_input(label="Visibility")
Location = st.selectbox(label="Location", options=["inland", "mountain", "coastal"])

#Map categorical inputs to numerical values
cloud_cover_map = {"Overcast": 0, "Partly Cloudy": 1, "Clear": 2, "Cloudy": 3}
season_map = {"Winter": 0, "Spring": 1, "Summer": 2, "Autumn": 3}
location_map = {"inland": 0, "mountain": 1, "coastal": 2}


#Create feature array
features = [[
    temparature, 
    humidity, 
    wind_speed, 
    Precipitation, 
    cloud_cover_map[CloudCover], 
    AtmosphericPressure, 
    UVindex, 
    season_map[Season], 
    Visibility, 
    location_map[Location]
]]

if st.button("Predict Weather"):
    prediction = model.predict(features)
    if prediction[0] == 0:
        st.success("The weather is Sunny")
    elif prediction[0] == 1:
        st.success("The weather is Rainy")    
    elif prediction[0] == 2:
        st.success("The weather is Cloudy")
    else:
        st.success("The weather is Snowy")
