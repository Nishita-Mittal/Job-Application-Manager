Job Application Manager
Developer: Nishita Mittal
Repository: Job-Application-Manager

This is a Streamlit-based web application that simulates an Applicant Tracking System (ATS) resume scanner. It enables users to evaluate their resume against a job description using natural language processing techniques and large language models.

🔍 Features
✅ Upload PDF Resume
Upload your resume in .pdf format for processing and analysis.

📝 Input Job Description
Paste or type the job description into the provided text area.

🤖 "Tell Me About the Resume"
AI-generated summary evaluating how well the resume fits the job description, including strengths, weaknesses, and recommendations.

🧠 Get Keywords
Extracts important skills, technologies, and keywords relevant to the job, returned in JSON format.

📊 Percentage Match
Calculates how closely the resume matches the job description. Also displays:

❌ Keywords missing

✅ Overall compatibility percentage

💡 Final thoughts to improve your resume

🚀 Installation
1. Clone the Repository
git clone https://github.com/Nishita-Mittal/Job-Application-Manager.git
cd Job-Application-Manager
2. Install Dependencies
pip install -r requirements.txt
3. Run the Streamlit App
streamlit run app.py
💻 Usage Instructions
Launch the app using Streamlit.

Paste your job description into the text area.

Upload your PDF resume.

Click:

Tell Me About the Resume → For profile evaluation

Get Keywords → For keyword extraction

Get Percentage Match → To evaluate fit and receive suggestions

🧰 Technologies & Libraries Used
Frontend & Backend: Streamlit

Programming Language: Python

LLM API: Google Gemini

PDF Handling: pdf2image, PyMuPDF, pdfminer.six

File Handling: os, uuid, base64

Data Visualization: JSON response formatting

📂 Project Structure
Job-Application-Manager/
├── app.py                   # Main Streamlit app
├── requirements.txt         # Python dependencies
├── uploads/                 # Directory for uploaded resumes
│   └── reports/             # Analysis reports (optional)
├── index.html               # For PDF preview (optional)
└── jd_matcher.py            # Keyword matching & scoring logic
🧠 Future Improvements
Add support for multiple resumes comparison.

Visualize match results using charts.

Include LinkedIn URL parsing for auto-fetching resumes.

Option to export results as PDF report.

🙋‍♀️ Author
Nishita Mittal
📧 nishitamittal0816@gmail.com


