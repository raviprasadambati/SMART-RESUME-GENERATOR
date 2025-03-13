import google.generativeai as genai

genai.configure(api_key="AIzaSyDaOHSzWkwEnJqyJiHsrlpI5EpbzskeAz0")  # Replace with your actual API key

# Use the correct model name
model = genai.GenerativeModel("gemini-1.5-pro")

def generate_resume(name, job_title):
    context = f"Generate a professional resume for {name}, applying for {job_title}. Include summary, skills, experience, and education."
    response = model.generate_content(context)
    return response.text if isinstance(response.text, str) else response.text[0].text