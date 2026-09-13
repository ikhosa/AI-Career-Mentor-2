import os
from groq import Groq

def generate_ai_guidance(top_careers, aptitude_scores, interest_scores):
    """
    Generates personalized career mentoring using Groq API, shortlisting 
    undergraduate programs and top Pakistani universities based on QS rankings.
    """
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        return "⚠️ **GROQ_API_KEY** environment variable is missing. Please configure it to receive AI guidance."

    client = Groq(api_key=api_key)

    # University mapping reference based on recent QS Subject Rankings in Pakistan
    qs_reference_data = """
    - Computer Science / Software Engineering / AI:
      1. NUST (National University of Sciences and Technology), Islamabad (QS Asia #68 / World #334)
      2. FAST-NUCES (Islamabad / Lahore / Karachi)
      3. COMSATS University Islamabad (QS Asia #150)
      * Honorable mentions: ITU Lahore, LUMS
    
    - Business Administration / Finance / Economics:
      1. LUMS (Suleman Dawood School of Business), Lahore (QS World #101-150 in Business)
      2. IBA (Institute of Business Administration), Karachi (QS World #151-250)
      3. NUST Business School (NBS), Islamabad
      * Honorable mentions: Lahore School of Economics (LSE), Quaid-i-Azam University (QAU)

    - Medicine / Health / Biotechnology:
      1. Aga Khan University (AKU), Karachi (QS Medicine World #201-250)
      2. King Edward Medical University (KEMU) / UHS Lahore
      3. Dow University of Health Sciences (DUHS), Karachi / NUMS Rawalpindi

    - Engineering (Electrical, Mechanical, Civil, Mechatronics):
      1. NUST (College of EME / SEECS / SCME), Islamabad
      2. UET Lahore (QS World #251-300 Engineering)
      3. GIKI (Ghulam Ishaq Khan Institute), Topi / PIEAS Islamabad

    - Cyber Security / Information Security:
      1. Air University, Islamabad
      2. NUST (SEECS), Islamabad
      3. FAST-NUCES / COMSATS Islamabad
    """

    prompt = f"""
    You are an expert Pakistani academic counselor. Analyze the student's assessment results below:

    Top 3 Career Matches:
    1. {top_careers[0]['career']} ({top_careers[0]['suitability_score']}% match)
    2. {top_careers[1]['career']} ({top_careers[1]['suitability_score']}% match)
    3. {top_careers[2]['career']} ({top_careers[2]['suitability_score']}% match)

    Aptitude Breakdown: {aptitude_scores}
    Interest Profile: {interest_scores}

    Reference Ranking Data for Pakistan:
    {qs_reference_data}

    Generate a structured, professional guide adhering strictly to the following markdown headings:

    ### 🎓 Recommended Undergraduate Programs & Universities
    List the **Top 3 Undergraduate Programs** (e.g., BS Computer Science, BBA, BS Cyber Security, MBBS) best suited for this student based on their highest career match. For EACH program, list the **Top 3 Universities in Pakistan** based on QS Subject Rankings.

    Format each program like this:
    * **[Program Name]**
      1. **University 1** (Short reason / QS Standing)
      2. **University 2** (Short reason)
      3. **University 3** (Short reason)

    ### 💡 Career & Skill Roadmap
    Provide 3 concise bullet points on key technical/academic skills they should build during high school or intermediate to excel in these degree paths.

    ### 💼 Job Market & Freelancing Prospects
    A short paragraph discussing local employment demand in Pakistan and global remote freelancing opportunities.
    """

    try:
        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.6,
            max_tokens=1000
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error generating AI career guidance: {str(e)}"
