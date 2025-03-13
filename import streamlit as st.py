import streamlit as st
import google.generativeai as genai

# Configure Google Generative AI
genai.configure(api_key="AIzaSyDaOHSzWkwEnJqyJiHsrlpI5EpbzskeAz0")  # Replace with your actual API key

# Initialize Model
model = genai.GenerativeModel("gemini-1.5-pro")  # Use the correct model name

# Function to generate resume
def generate_resume(name, job_title):
    context = f"Generate a professional resume for {name}, applying for {job_title}. Include summary, skills, experience, and education."
    response = model.generate_content(context)
    return response.text if isinstance(response.text, str) else response.text[0].text

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