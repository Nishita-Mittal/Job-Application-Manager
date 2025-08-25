# 🧾 Job Application Manager<br>
A Streamlit-based web application that simulates an Applicant Tracking System (ATS) resume scanner. This tool helps job seekers evaluate their resume against a job description using Natural Language Processing (NLP) and LLM-powered analysis to optimize for better hiring outcomes.

---

## 📌 Features
- ✅ Resume Evaluation:<br>
Upload resumes in PDF format for parsing and intelligent analysis.<br>
AI-generated summary feedback highlighting strengths, weaknesses, and suggestions.<br>

- ✅ Job Description Matcher:<br>
Paste or type any job description into the app.<br>
Smart comparison of resume content against job expectations.<br>
Highlights missing keywords and areas for improvement.<br>

- ✅ Keyword Extraction:<br>
Extracts technical skills, tools, and domain-specific terms from the job description.<br>
Presents output in structured JSON format.<br>

- ✅ Match Percentage:<br>
Calculates an overall compatibility score between the resume and job description.<br>

## 🖥️Displays:

- ❌ Missing Keywords<br>
- ✅ Match Percentage<br>
- 💡Actionable Insights<br>

---

## 🛠️ Technologies Used
- Frontend & Backend: Streamlit<br>
- Programming Language: Python<br>
- LLM Integration: Google Gemini API<br>
- PDF Handling: pdf2image, PyMuPDF, pdfminer.six<br>
- File Handling: os, uuid, base64<br>
- Visualization: JSON-formatted response<br>
- Version Control: Git & GitHub<br>

---

## 📁 Project Structure

Job-Application-Manager/<br>
├── app.py               # Main Streamlit app logic<br>
├── requirements.txt     # List of Python dependencies<br>
├── uploads/             # Directory where uploaded resumes are stored<br>
│   └── reports/         # Generated reports (optional)<br>
├── index.html           # For PDF preview (optional)<br>
└── jd_matcher.py        # Job description matching and scoring module<br>

---

## 🚀 Installation
To run this project locally:<br>
# Step 1: Clone the repository<br>
git clone https://github.com/Nishita-Mittal/Job-Application-Manager.git<br>

# Step 2: Navigate into the project directory<br>
cd Job-Application-Manager<br>

# Step 3: Install all required packages<br>
pip install -r requirements.txt<br>

# Step 4: Launch the Streamlit app<br>
streamlit run app.py<br>

---

## 💻 Usage Instructions<br>
- Open the Streamlit app in your browser.

- Paste your job description into the provided text area.<br>
- Upload your PDF resume.<br>
- Click on the desired options:<br>
🧠 Tell Me About the Resume → for AI-generated evaluation<br>
🔍 Get Keywords → for skill extraction<br>
📊 Get Percentage Match → for fit analysis and final suggestions<br>

---

## 🌱 Future Enhancements<br>
- 📁 Compare multiple resumes for the same job<br>
- 📊 Visualize results using charts or graphs<br>
- 🔗 Support LinkedIn URL parsing for automatic resume fetch<br>
- 📝 Export match reports as downloadable PDFs<br>

---

## 🙋‍♀️ Author<br>
Nishita Mittal<br>
📧 nishitamittal0816@gmail.com

