import streamlit as st
import pdf2image
import io
import json
import base64
import google.generativeai as genai

# Configure Gemini
genai.configure(api_key=st.secrets.GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-2.0-flash')

# Custom CSS for better GUI
st.markdown("""
    <style>
        .main {
            background-color: #f9f9f9;
        }
        .stTextInput, .stTextArea, .stFileUploader {
            border-radius: 10px;
        }
        .stButton > button {
            background-color: #4CAF50;
            color: white;
            border-radius: 8px;
            padding: 0.5em 1em;
            font-size: 16px;
        }
        .response-box {
            background-color: #ffffff;
            padding: 1em;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0,0,0,0.05);
            margin-top: 1em;
        }
    </style>
""", unsafe_allow_html=True)

# Caching functions
@st.cache_data()
def get_gemini_response(input, pdf_content, prompt):
    response = model.generate_content([input, pdf_content[0], prompt])
    return response.text

@st.cache_data()
def get_gemini_response_keywords(input, pdf_content, prompt):
    response = model.generate_content([input, pdf_content[0], prompt])
    return json.loads(response.text[8:-4])

@st.cache_data()
def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        images = pdf2image.convert_from_bytes(uploaded_file.read())
        first_page = images[0]
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()
        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")

# Streamlit App Setup
st.set_page_config(page_title="Job Application Manager", layout="wide")
st.title("📄 Job Application Manager")
st.markdown("Upload your resume and paste the job description to evaluate compatibility.")

# Input Section
col1, col2 = st.columns([1, 2])
with col1:
    uploaded_file = st.file_uploader("📎 Upload your Resume (PDF)", type=["pdf"])
with col2:
    input_text = st.text_area("📝 Job Description", key="input", height=200)

# Save resume to session
if 'resume' not in st.session_state:
    st.session_state.resume = None
if uploaded_file is not None:
    st.success("✅ Resume uploaded successfully.")
    st.session_state.resume = uploaded_file

# Buttons Row
colA, colB, colC = st.columns(3)
with colA:
    submit1 = st.button("🧠 Tell Me About the Resume")
with colB:
    submit2 = st.button("🧲 Get Keywords")
with colC:
    submit3 = st.button("📊 Percentage Match")

# Prompts
input_prompt1 = """
You are an experienced Technical Human Resource Manager, your task is to review the provided resume against the job description. 
Please share your professional evaluation on whether the candidate's profile aligns with the role. 
Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
"""

input_prompt2 = """
As an expert ATS (Applicant Tracking System) scanner with an in-depth understanding of AI and ATS functionality, 
your task is to evaluate a resume against a provided job description. Please identify the specific skills and keywords 
necessary to maximize the impact of the resume and provide response in json format as {Technical Skills:[], Analytical Skills:[], Soft Skills:[]}.
Note: Please do not make up the answer only answer from job description provided
"""

input_prompt3 = """
You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality, 
your task is to evaluate the resume against the provided job description. Give me the percentage of match if the resume matches
the job description. First the output should come as percentage and then keywords missing and last final thoughts.
"""

# Handlers
if submit1:
    if st.session_state.resume is not None:
        pdf_content = input_pdf_setup(st.session_state.resume)
        response = get_gemini_response(input_prompt1, pdf_content, input_text)
        st.markdown("### 📋 Resume Evaluation:")
        st.markdown(f"<div class='response-box'>{response}</div>", unsafe_allow_html=True)
    else:
        st.warning("⚠️ Please upload a resume.")

elif submit2:
    if st.session_state.resume is not None:
        pdf_content = input_pdf_setup(st.session_state.resume)
        response = get_gemini_response_keywords(input_prompt2, pdf_content, input_text)
        st.markdown("### 🧩 Extracted Skills:")
        if response:
            st.markdown(f"<div class='response-box'><b>Technical Skills:</b> {', '.join(response['Technical Skills'])}<br><b>Analytical Skills:</b> {', '.join(response['Analytical Skills'])}<br><b>Soft Skills:</b> {', '.join(response['Soft Skills'])}</div>", unsafe_allow_html=True)
    else:
        st.warning("⚠️ Please upload a resume.")

elif submit3:
    if st.session_state.resume is not None:
        pdf_content = input_pdf_setup(st.session_state.resume)
        response = get_gemini_response(input_prompt3, pdf_content, input_text)
        st.markdown("### 📈 Match Percentage:")
        st.markdown(f"<div class='response-box'>{response}</div>", unsafe_allow_html=True)
    else:
        st.warning("⚠️ Please upload a resume.")
