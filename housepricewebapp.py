import streamlit as st
import pickle
import numpy as np
import requests

try:
    model = pickle.load(open("trained_model.sav", "rb"))
except Exception as e:
    st.error("Failed to load model. Make sure 'trained_model.sav' exists in the same folder.")
    st.stop()

def get_live_usd_to_inr():
    try:
        url = "https://api.exchangerate-api.com/v4/latest/USD"
        response = requests.get(url)
        data = response.json()
        return data["rates"]["INR"]
    except:
        return 83.0  


def convert_to_price(predicted_price, exchange_rate):
    usd = predicted_price * 100000 
    inr = usd * exchange_rate       
    return round(usd, 2), round(inr, 2)

st.set_page_config(page_title="House Price Predictor", layout="centered")
st.title("  House Price Prediction App")
st.markdown("Enter house details to predict its price in USD & INR (Live exchange rate)")

medinc = st.number_input("Median Income", min_value=0.0, step=0.1)
houseage = st.number_input("House Age", min_value=0.0, step=1.0)
avgrooms = st.number_input("Average Rooms", min_value=0.0, step=1.0)
avgbedrooms = st.number_input("Average Bedrooms", min_value=0.0, step=1.0)
population = st.number_input("Population", min_value=0.0, step=1.0)
avgoccupany = st.number_input("Average Occupancy", min_value=0.0, step=0.1)
latitude = st.number_input("Latitude", format="%.6f")
longitude = st.number_input("Longitude", format="%.6f")

if st.button("Predict House Price"):
    try:
        input_data = np.array([[medinc, houseage, avgrooms, avgbedrooms,
                                population, avgoccupany, latitude, longitude]])

        prediction = model.predict(input_data)[0]
        rate = get_live_usd_to_inr()
        usd, inr = convert_to_price(prediction, rate)

        st.success(f" Model Prediction: {round(prediction, 4)}")
        st.info(f" Estimated Price in USD: ${usd}")
        st.info(f" Estimated Price in INR: ₹{inr} (at ₹{rate}/USD)")

    except Exception as e:
        st.error(f"Prediction failed: {e}")
