import streamlit as st
import pandas as pd

st.title("Solar Power Prediction")

# User Inputs
temperature = st.number_input("Temperature")
exhaust_vacuum = st.number_input("Exhaust Vacuum")
ambient_pressure = st.number_input("Ambient Pressure")
relative_humidity = st.number_input("Relative Humidity")

day_of_year = st.number_input("Day of Year")
year = st.number_input("Year")
month = st.number_input("Month")
day = st.number_input("Day")
first_hour = st.number_input("First Hour of Period")
is_daylight = st.number_input("Is Daylight (0/1)")
distance_solar_noon = st.number_input("Distance to Solar Noon")
avg_temp_day = st.number_input("Average Temperature (Day)")
avg_wind_dir_day = st.number_input("Average Wind Direction (Day)")
avg_wind_speed_day = st.number_input("Average Wind Speed (Day)")
sky_cover = st.number_input("Sky Cover")
visibility = st.number_input("Visibility")
avg_wind_speed_period = st.number_input("Average Wind Speed (Period)")
avg_barometric_pressure = st.number_input("Average Barometric Pressure (Period)")

# Create DataFrame
input_data = pd.DataFrame({
    "Temperature":[temperature],
    "Exhaust Vacuum":[exhaust_vacuum],
    "Ambient Pressure":[ambient_pressure],
    "Relative Humidity":[relative_humidity],
    "Day of Year":[day_of_year],
    "Year":[year],
    "Month":[month],
    "Day":[day],
    "First Hour of Period":[first_hour],
    "Is Daylight":[is_daylight],
    "Distance to Solar Noon":[distance_solar_noon],
    "Average Temperature (Day)":[avg_temp_day],
    "Average Wind Direction (Day)":[avg_wind_dir_day],
    "Average Wind Speed (Day)":[avg_wind_speed_day],
    "Sky Cover":[sky_cover],
    "Visibility":[visibility],
    "Average Wind Speed (Period)":[avg_wind_speed_period],
    "Average Barometric Pressure (Period)":[avg_barometric_pressure]
})

st.write("Input Data:")
st.dataframe(input_data)
