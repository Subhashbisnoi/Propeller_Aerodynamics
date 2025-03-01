import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Load the trained models
model_ct = joblib.load('model_ct.pkl')
model_fm = joblib.load('model_fm.pkl')

# Title of the app
st.title('Propeller Performance Predictor')

# Input fields for user
st.sidebar.header('Input Parameters')
B = st.sidebar.number_input('Blade Count (B)', min_value=1, max_value=4, value=2)
D = st.sidebar.number_input('Diameter (D)', min_value=0.1, value=10.0)
P = st.sidebar.number_input('Pitch (P)', min_value=0.1, value=6.0)
J = st.sidebar.number_input('Advance Ratio (J)', min_value=0.0, value=0.5)
N = st.sidebar.number_input('RPM (N)', min_value=0, value=5000)
CP = st.sidebar.number_input('Power Coefficient (CP)', min_value=0.0, value=0.1)
eta = st.sidebar.number_input('Efficiency (eta)', min_value=0.0, max_value=1.0, value=0.8)
c_R = st.sidebar.number_input('Chord-to-Radius Ratio (c/R)', min_value=0.0, value=0.1)
r_R = st.sidebar.number_input('Radius-to-Radius Ratio (r/R)', min_value=0.0, value=0.75)
beta = st.sidebar.number_input('Blade Twist Angle (beta)', min_value=0.0, value=15.0)
P_D = P / D

# Create a DataFrame for prediction
input_data = pd.DataFrame({
    'B': [B],
    'D': [D],
    'P': [P],
    'J': [J],
    'N': [N],
    'CP': [CP],
    'eta': [eta],
    'c/R': [c_R],
    'r/R': [r_R],
    'beta': [beta],
    'P/D': [P_D]
})

# Predict thrust coefficient (CT) and hover figure of merit (FM)
if st.sidebar.button('Predict'):
    ct_pred = model_ct.predict(input_data)
    fm_pred = model_fm.predict(input_data)

    st.write(f'Predicted Thrust Coefficient (CT): {ct_pred[0]:.4f}')
    st.write(f'Predicted Hover Figure of Merit (FM): {fm_pred[0]:.4f}')