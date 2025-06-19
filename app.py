import streamlit as st
import pandas as pd

# Load data
df = pd.read_csv("data/universities.csv")

st.title("🎓 Master's Program Recommender")

# User Inputs
subject = st.selectbox("Choose your subject of interest", df['Subject'].unique())
country = st.selectbox("Preferred study country", df['Country'].unique())
ielts = st.slider("Your IELTS score", 5.0, 9.0, 6.5)
gpa = st.slider("Your GPA (out of 4.0)", 2.0, 4.0, 3.0)

# Filtering
filtered = df[
    (df['Subject'] == subject) &
    (df['Country'] == country) &
    (df['IELTS'] <= ielts) &
    (df['Min_GPA'] <= gpa)
]

st.subheader("Recommended Programs:")

if not filtered.empty:
    st.dataframe(filtered[['University', 'Program', 'Tuition']])
else:
    st.warning("No matching programs found. Try adjusting your scores.")
