# 🚀 ShadowHire AI – Hiring Outcome Simulator

ShadowHire AI is an AI-powered resume evaluation and career simulation platform that predicts hiring probability, analyzes recruiter psychology, and identifies skill gaps.

---

## 🔥 Problem Statement

Students and early professionals often do not understand how recruiters evaluate resumes. Most resume tools only perform keyword matching and do not simulate real hiring behavior.

ShadowHire AI bridges this gap by combining NLP-based similarity scoring with LLM-driven recruiter psychology analysis.

---

## 🧠 How It Works

### 1️⃣ Resume & Job Description Analysis
- Resume PDF is parsed using `pdfplumber`
- Text is processed using `TF-IDF Vectorization`
- Cosine Similarity calculates hiring probability

### 2️⃣ Skill Gap Detection
A deterministic skill database identifies:
- Strong Skills (matching job requirements)
- Missing Skills (skills required but not present)

### 3️⃣ Recruiter Psychology Simulation
Using Groq’s LLaMA 3.1 model, the system evaluates:

- Confidence Level
- Ownership Signals
- Measurable Impact
- Leadership Indicators

This mimics real recruiter evaluation behavior.

### 4️⃣ Career Outcome Projection
Based on score thresholds, the system predicts:

- Service-Based Path
- Mid-Tier Company Path
- Tier-1 Product Company Path

Each path includes projected 5-year salary insights.

### 5️⃣ What-If Career Simulator
Users can toggle improvements such as:
- Improve DSA
- Add Backend Project
- Add Internship

The system recalculates hiring probability instantly, helping users prioritize improvements strategically.

---

## 🏗 Tech Stack

### Backend
- FastAPI
- Python
- Groq LLM (LLaMA 3.1)
- Scikit-learn (TF-IDF, Cosine Similarity)
- PDFPlumber

### Frontend
- HTML5
- CSS3
- JavaScript
- Chart.js

### Deployment
- Backend: Render
- Frontend: Netlify

---

## 📊 Features

- Hiring Probability Prediction
- Interview Round Simulation
- Skill Gap Analysis
- Recruiter Psychology Insights
- Career Projection Modeling
- Interactive What-If Simulator
- Real-time Score Visualization

---

## 🚀 Installation (Local Setup)

### 1️⃣ Clone Repository
git clone https://github.com/VPriya100code/ShadowHire_ai.git
cd shadowhire-ai


### 2️⃣ Install Dependencies


pip install -r requirements.txt


### 3️⃣ Add Environment Variable

Set your Groq API key:


GROQ_API_KEY=your_api_key


### 4️⃣ Run Backend


uvicorn main:app --reload


Backend runs at:

http://127.0.0.1:8000


---

## 🌍 Deployment

- Deploy backend to Render
- Deploy frontend to Netlify
- Update frontend API endpoint to production URL

---

## 🎯 Future Enhancements

- Multi-resume comparison
- Company-specific hiring simulation
- Resume auto-improvement suggestions
- AI-powered cover letter generation
- Skill heatmap visualization

---

## 👩‍💻 Author

V Priyadharshini 
Computer Science Engineering  
AI & Full Stack Developer

---

## 📜 License

This project is built for educational and hackathon purposes.
