import streamlit as st
import joblib
import numpy as np

# Load your trained model
# model = pickle.load(open("model.pkl", "rb"))
try:
    model = joblib.load('model_score')
except Exception as e:
    print(f"Error loading the model: {e}")

st.set_page_config(page_title="Score prediction", page_icon="📚")

st.title("💼 Score Prediction Using ML")

st.write("Predict score based on **Hours of Study**")

# Input field (replaces <input type="float">)
study_hours = st.number_input(
    "Study Hours",
    min_value=1.0,
    max_value=50.0,
    step=1.0
)

# Submit button (replaces <form> submit)
if st.button("Submit"):
    # Example prediction logic
    prediction = model.predict([[study_hours]])
    score = prediction[0]


    st.success("Score estimation:")
    st.write(f" {score}")
if st.button("Reset"):
    st.session_state.study_hours = 0.0