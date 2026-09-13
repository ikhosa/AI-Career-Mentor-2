import os
import streamlit as st
from groq import Groq

def get_groq_client():
    api_key = st.secrets.get("GROQ_API_KEY") or os.environ.get("GROQ_API_KEY")
    if not api_key:
        return None
    return Groq(api_key=api_key)

def generate_ai_guidance(top_careers, aptitude_scores, interest_scores):
    client = get_groq_client()
    
    if not client:
        return "⚠️ *Groq API Key not found in Streamlit Secrets. Please set `GROQ_API_KEY` in Streamlit Cloud Secrets to receive personalized AI recommendations.*"

    prompt = f"""
    You are an expert AI Career Mentor for high school and university students in Pakistan.
    Based on an assessment, here are the student's top 3 custom career recommendations:

    1. {top_careers[0]['career']} - Suitability Score: {top_careers[0]['suitability_score']}%
    2. {top_careers[1]['career']} - Suitability Score: {top_careers[1]['suitability_score']}%
    3. {top_careers[2]['career']} - Suitability Score: {top_careers[2]['suitability_score']}%

    Student Aptitude Breakdown: {aptitude_scores}
    Student Interest Tags: {list(interest_scores.keys())}

    Please provide a concise, structured analysis for EACH of the 3 recommendations.
    Format your response using Markdown with the following sub-headings for EACH career:
    - **Why it Matches Your Interests**
    - **Why it Matches Your Aptitude**
    - **Key Strengths Identified**
    - **High-Income & Freelancing Potential in Pakistan**
    - **Actionable Next Steps**

    Keep the tone empowering, practical, tailored to the Pakistani job market/education system, and professional.
    """

    try:
        response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a professional educational career counseling expert in Pakistan."},
                {"role": "user", "content": prompt}
            ],
            model="openai/gpt-oss-120b",
            temperature=0.6,
            max_tokens=1500,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error generating AI career guidance: {str(e)}"
