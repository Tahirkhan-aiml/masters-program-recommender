import streamlit as st
import pandas as pd

# Load the university data
df = pd.read_csv("data/universities.csv")

st.set_page_config(page_title="Master's Program Recommender", layout="centered")
st.title("🎓 AI-Powered Master's Program Recommender")

st.markdown("Enter your academic profile below to get the best-suited universities for your master's degree abroad.")

# --- Input Form ---
with st.form("student_form"):
    name = st.text_input("Full Name")
    major = st.selectbox("Field of Interest", df['Field'].unique())
    gpa = st.number_input("GPA (out of 4.0)", min_value=0.0, max_value=4.0, step=0.1)
    ielts = st.number_input("IELTS Score", min_value=0.0, max_value=9.0, step=0.5)
    country_pref = st.selectbox("Preferred Country", df['Country'].unique())
    
    submitted = st.form_submit_button("Get Recommendations")

# --- Recommendation Logic ---
if submitted:
    filtered = df[
        (df['Field'] == major) &
        (df['Country'] == country_pref) &
        (df['Min GPA'] <= gpa) &
        (df['IELTS'] <= ielts)
    ]
    
    st.subheader("🔍 Recommended Universities for You:")
    
    if not filtered.empty:
        st.dataframe(filtered[['University', 'Country', 'Field', 'Min GPA', 'IELTS']].head(5))
    else:
        st.warning("No matching universities found. Try adjusting your preferences.")
