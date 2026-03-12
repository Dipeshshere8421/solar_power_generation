# -*- coding: utf-8 -*-

import streamlit as st
import pandas as pd
import joblib

# Load trained Random Forest model
model = joblib.load("power_prediction_rfr_model.pkl")

st.title("Power Generation Prediction System")
st.write("Enter the input values to predict power generation")

# Inputs
dof = st.number_input("Day of Year")
yr = st.number_input("Year")
mn = st.number_input("Month")
dy = st.number_input("Day")
fhp = st.number_input("First Hour of Period")
id = st.number_input("Is Daylight (0 or 1)")
dtsn = st.number_input("Distance to Solar Noon")

avt = st.number_input("Average Temperature (Day)")
awd = st.number_input("Average Wind Direction (Day)")
aws_day = st.number_input("Average Wind Speed (Day)")

sc = st.number_input("Sky Cover")
v = st.number_input("Visibility")

rh = st.number_input("Relative Humidity")

aws_period = st.number_input("Average Wind Speed (Period)")
ap = st.number_input("Average Barometric Pressure (Period)")

# Create dataframe
input_data = pd.DataFrame({
    "Day of Year": [dof],
    "Year": [yr],
    "Month": [mn],
    "Day": [dy],
    "First Hour of Period": [fhp],
    "Is Daylight": [id],
    "Distance to Solar Noon": [dtsn],
    "Average Temperature (Day)": [avt],
    "Average Wind Direction (Day)": [awd],
    "Average Wind Speed (Day)": [aws_day],
    "Sky Cover": [sc],
    "Visibility": [v],
    "Relative Humidity": [rh],
    "Average Wind Speed (Period)": [aws_period],
    "Average Barometric Pressure (Period)": [ap]
})

# Prediction button
if st.button("Predict Power Generation"):

    prediction = model.predict(input_data)

    st.success(f"Predicted Power Generated: {prediction[0]:.2f}")
