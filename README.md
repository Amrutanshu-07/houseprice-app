# House Price Prediction Web Application

This repository contains a web-based application for predicting house prices using a trained machine learning model. The app is built using Python and deployed with Streamlit Cloud.

Access the live app here:  
**[https://housepricewebapp.streamlit.app/](https://housepricewebapp.streamlit.app/)**

---

## Project Overview

This project demonstrates a basic implementation of a machine learning regression model to predict house prices based on various features. The Streamlit interface allows users to input values and receive real-time predictions from the trained model.

---

## Features

- Real-time house price prediction
- Simple, interactive interface
- Model trained using scikit-learn
- Deployed on Streamlit Cloud for easy access

---

## Technologies Used

- Python 3
- scikit-learn
- pandas
- numpy
- pickle (for saving/loading the model)
- Streamlit

---

## File Structure
houseprice-app/
├── housepricewebapp.py 
├── trained_model.sav 
├── requirements.txt 
└── README.md

---

## Setup Instructions (Run Locally)

To run the application on your local machine:

1. Clone this repository:

   ```bash
   git clone https://github.com/Amrutanshu-07/houseprice-app.git
   cd houseprice-app
   
2. Install the required packages:
   pip install -r requirements.txt
   
4. streamlit run housepricewebapp.py

