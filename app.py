import streamlit as st
from backend import generate_resume

# Streamlit UI
st.title("Smart Resume Generator")
name = st.text_input("Enter your Name")
job_title = st.text_input("Enter your Job Title")

if st.button("Generate Resume"):
    if name and job_title:
        resume = generate_resume(name, job_title)
        st.markdown(resume)
    else:
        st.warning("Please enter both Name and Job Title")