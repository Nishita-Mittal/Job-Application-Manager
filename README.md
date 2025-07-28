🧾 Job Application Manager
A Streamlit-based web application that simulates an Applicant Tracking System (ATS) resume scanner. This tool helps job seekers evaluate their resume against a job description using Natural Language Processing (NLP) and LLM-powered analysis to optimize for better hiring outcomes.

📌 Features
✅ Resume Evaluation:
Upload resumes in PDF format for parsing and intelligent analysis.

AI-generated summary feedback highlighting strengths, weaknesses, and suggestions.

✅ Job Description Matcher:
Paste or type any job description into the app.

Smart comparison of resume content against job expectations.

Highlights missing keywords and areas for improvement.

✅ Keyword Extraction:
Extracts technical skills, tools, and domain-specific terms from the job description.

Presents output in structured JSON format.

✅ Match Percentage:
Calculates an overall compatibility score between the resume and job description.

Displays:

❌ Missing Keywords

✅ Match Percentage

💡 Actionable Insights

🛠️ Technologies Used
Frontend & Backend: Streamlit

Programming Language: Python

LLM Integration: Google Gemini API

PDF Handling: pdf2image, PyMuPDF, pdfminer.six

File Handling: os, uuid, base64

Visualization: JSON-formatted response

Version Control: Git & GitHub

📁 Project Structure

Job-Application-Manager/
├── app.py               # Main Streamlit app logic
├── requirements.txt     # List of Python dependencies
├── uploads/             # Directory where uploaded resumes are stored
│   └── reports/         # Generated reports (optional)
├── index.html           # For PDF preview (optional)
└── jd_matcher.py        # Job description matching and scoring module

🚀 Installation
To run this project locally:
# Step 1: Clone the repository
git clone https://github.com/Nishita-Mittal/Job-Application-Manager.git

# Step 2: Navigate into the project directory
cd Job-Application-Manager

# Step 3: Install all required packages
pip install -r requirements.txt

# Step 4: Launch the Streamlit app
streamlit run app.py

💻 Usage Instructions
Open the Streamlit app in your browser.

Paste your job description into the provided text area.

Upload your PDF resume.

Click on the desired options:

🧠 Tell Me About the Resume → for AI-generated evaluation

🔍 Get Keywords → for skill extraction

📊 Get Percentage Match → for fit analysis and final suggestions

🌱 Future Enhancements
📁 Compare multiple resumes for the same job

📊 Visualize results using charts or graphs

🔗 Support LinkedIn URL parsing for automatic resume fetch

📝 Export match reports as downloadable PDFs

🙋‍♀️ Author
Nishita Mittal
📧 nishitamittal0816@gmail.com

