import streamlit as st
import pandas as pd

# Set page config
st.set_page_config(page_title="Master's Program Recommender", layout="centered")

# Title
st.title("🎓 AI-powered Recommendation System for Master’s Programs Abroad")

# Load sample university data
@st.cache_data
def load_data():
    df = pd.read_csv("data/universities.csv")
    return df

df = load_data()

# User input
st.subheader("Enter Your Profile:")

gpa = st.slider("Your GPA (out of 4.0)", 0.0, 4.0, 3.0, 0.1)
gre = st.slider("GRE Score", 260, 340, 300)
ielts = st.slider("IELTS Score", 0.0, 9.0, 7.0, 0.5)
budget = st.number_input("Budget (USD)", value=20000)
preferred_country = st.selectbox("Preferred Country", df["Location"].unique())
field = st.selectbox("Field of Interest", df["Program Focus"].unique())

# Recommend button
if st.button("Recommend Programs"):
    results = df[
        (df["GPA"] <= gpa) &
        (df["GRE"] <= gre) &
        (df["IELTS"] <= ielts) &
        (df["Tuition"] <= budget) &
        (df["Location"] == preferred_country) &
        (df["Program Focus"] == field)
    ]
    
    if len(results) == 0:
        st.warning("No programs found matching your profile. Try changing criteria.")
    else:
        st.success(f"Found {len(results)} matching program(s):")
        st.dataframe(results[["University", "Program", "Location", "Tuition"]])
