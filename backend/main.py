from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
import pdfplumber
import io
import os
import random
import re
import json
from groq import Groq
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 🔑 PUT YOUR GROQ KEY HERE
import os
client = Groq(api_key=os.environ["GROQ_API_KEY"])
client = Groq()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def extract_text(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text

def similarity_score(resume, jd):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([resume, jd])
    score = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
    return round(score * 100, 2)

def simulate_rounds(score):
    return {
        "ATS Round": round(score, 2),
        "Technical Round 1": round(max(score - 10, 0), 2),
        "Technical Round 2": round(max(score - 20, 0), 2),
        "System Design": round(max(score - 25, 0), 2),
        "HR Round": round(min(score + 5, 100), 2),
    }

def career_path(score):
    if score > 75:
        return "Tier-1 Product Company Path | 5-Year Salary: 35-50 LPA"
    elif score > 50:
        return "Mid-Tier Company Path | 5-Year Salary: 15-25 LPA"
    else:
        return "Service-Based Path | 5-Year Salary: 6-12 LPA"

def call_llm(prompt):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
    )
    return response.choices[0].message.content

def extract_skills(text):
    prompt = f"""
Extract ONLY technical skills from the following text.
Return STRICTLY a JSON array.

Text:
{text}
"""
    response = call_llm(prompt)
    match = re.search(r"\[.*\]", response, re.DOTALL)
    if match:
        try:
            return json.loads(match.group())
        except:
            return []
    return []

@app.post("/analyze/")
async def analyze(
    resume: UploadFile = File(...),
    job_description: str = Form(...),
    improve_dsa: bool = Form(False),
    add_project: bool = Form(False),
    internship: bool = Form(False)
):
    file_bytes = await resume.read()
    pdf_file = io.BytesIO(file_bytes)
    resume_text = extract_text(pdf_file)

    base_score = similarity_score(resume_text, job_description)

    boost = 0
    if improve_dsa: boost += 10
    if add_project: boost += 10
    if internship: boost += 8

    final_score = round(min(base_score + boost, 100), 2)

    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(job_description)

    missing_skills = list(set(jd_skills) - set(resume_skills))
    strong_skills = list(set(resume_skills).intersection(set(jd_skills)))

    psychology_prompt = f"""
Analyze the following resume psychologically.

Resume:
{resume_text}

Provide:
Confidence Level: X/10
Ownership Signals: X/10
Measurable Impact: X/10
Leadership Indicators: X/10

Then give a short evaluation paragraph.
"""
    psychology = call_llm(psychology_prompt)

    return {
        "final_score": final_score,
        "rounds": simulate_rounds(final_score),
        "career": career_path(final_score),
        "strong_skills": strong_skills,
        "missing_skills": missing_skills,
        "psychology": psychology
    }