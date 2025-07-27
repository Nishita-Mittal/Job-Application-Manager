📂 Job Application Manager
A Streamlit-based web application that simulates an Applicant Tracking System (ATS) resume scanner. It allows users to evaluate their resume against a job description using NLP techniques and Large Language Models (LLMs) for better job application outcomes.

📌 Features
✅ Resume Analysis:
Upload PDF Resume and extract relevant content

AI-generated summary with strengths, weaknesses, and recommendations

✅ Job Description Matcher:
Paste or type job descriptions

Highlights resume-to-JD alignment

Displays missing keywords and areas to improve

✅ Keyword Extraction:
Extracts skills and technologies relevant to the job

Returns result in clean JSON format

✅ Match Percentage:
Shows compatibility score between resume and JD

Provides:

❌ Missing Keywords

✅ Compatibility Percentage

💡 Final Thoughts

🛠️ Technologies Used
Language: Python

Framework: Streamlit

LLM API: Google Gemini

PDF Handling: pdf2image, PyMuPDF, pdfminer.six

Utilities: os, uuid, base64

Visualization: JSON output formatting

IDE & Tools: VS Code, Git, GitHub

🧠 Concepts Covered
Natural Language Processing for resume and JD matching

Prompt engineering for LLM-based resume evaluation

Real-time interaction with uploaded PDFs

Data-driven feedback for resume improvement

🚀 Installation
git clone https://github.com/Nishita-Mittal/Job-Application-Manager.git
cd Job-Application-Manager
pip install -r requirements.txt
streamlit run app.py

💻 Usage Instructions
Launch the app using streamlit run app.py
Paste your job description in the input area
Upload your PDF resume
Click on:
Tell Me About the Resume → for evaluation summary
Get Keywords → for keyword extraction
Get Percentage Match → for compatibility score and suggestions

📁 Project Structure

Job-Application-Manager/
├── app.py               # Main Streamlit app
├── requirements.txt     # Python dependencies
├── uploads/             # Uploaded resume directory
│   └── reports/         # Analysis reports (optional)
├── index.html           # Optional PDF preview
└── jd_matcher.py        # JD matching & scoring logic

🌱 Future Improvements
Compare multiple resumes in one go
Visualize match insights with charts
Parse LinkedIn profiles to auto-fetch resumes
Export analysis reports as downloadable PDFs

🙋‍♀️ Author
Nishita Mittal
📧 nishitamittal0816@gmail.com

