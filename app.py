import streamlit as st
import pandas as pd

# Page title
st.title("AI-powered recommendation system for master’s programs abroad")

# Load the CSV file (make sure path is correct)
df = pd.read_csv("data/universities.csv")

# Show first 5 rows of the data
st.subheader("Sample University Data")
st.write(df.head())
