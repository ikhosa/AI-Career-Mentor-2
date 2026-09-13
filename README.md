# AI Career Mentor (Pakistan)

An interactive, AI-powered Streamlit web application tailored for students in Pakistan to discover top-demand, high-income, and freelancing career pathways based on interest and aptitude assessments.

## Features
- **20 Interactive Questions:** 10 scenario-based interest questions + 10 aptitude questions covering logic, math, science, english, analytical thinking, and problem solving.
- **Transparent Scoring System:** Combines interest profile and aptitude scores mapped against high-demand Pakistani job market & freelancing profiles.
- **Groq LLM Integration:** Provides personalized, context-aware career recommendations and action steps using Llama-3.3-70B.
- **Visual Analytics:** Interactive charts for aptitude performance and interest distribution via Plotly.

## Repository Structure
```
ai-career-mentor/
├── .streamlit/
│   └── config.toml
├── .gitignore
├── README.md
├── requirements.txt
├── careers.py
├── questions.py
├── scoring.py
├── ai_mentor.py
└── app.py
```

## Setup & Local Running
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/ai-career-mentor.git
   cd ai-career-mentor
   ```
2. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
3. Set your Groq API key in `.streamlit/secrets.toml`:
   ```toml
   GROQ_API_KEY = "your_groq_api_key_here"
   ```
4. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```

## Deployment
Deploy seamlessly via GitHub on [Streamlit Community Cloud](https://share.streamlit.io/). Remember to add `GROQ_API_KEY` in Streamlit's secrets settings.
