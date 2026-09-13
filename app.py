import streamlit as st
import pandas as pd
import plotly.express as px

from questions import INTEREST_QUESTIONS, APTITUDE_QUESTIONS
from scoring import calculate_scores
from ai_mentor import generate_ai_guidance

st.set_page_config(
    page_title="AI Career Mentor - Pakistan",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling with explicitly forced dark text and high-contrast background to work in both Light & Dark themes
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #004d4d 0%, #008080 100%);
        padding: 24px;
        border-radius: 12px;
        color: #ffffff !important;
        text-align: center;
        margin-bottom: 25px;
    }
    .main-header h1 {
        color: #ffffff !important;
    }
    .cui-badge {
        background-color: #f0a500;
        color: #111111 !important;
        padding: 4px 12px;
        border-radius: 20px;
        font-weight: bold;
        font-size: 0.85rem;
    }
    
    /* High Contrast Card Styling for Both Light and Dark Streamlit Themes */
    .card {
        background-color: #ffffff !important;
        padding: 22px;
        border-radius: 12px;
        border-left: 6px solid #008080;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
        margin-bottom: 20px;
        color: #111111 !important;
    }
    
    .card h3 {
        color: #004d4d !important;
        font-size: 1.25rem !important;
        font-weight: 700 !important;
        margin-bottom: 10px !important;
    }
    
    .card h2 {
        color: #008080 !important;
        font-size: 2rem !important;
        font-weight: 800 !important;
        margin-top: 5px !important;
        margin-bottom: 15px !important;
    }
    
    .card p {
        color: #222222 !important;
        font-size: 0.95rem !important;
        line-height: 1.4 !important;
        margin-bottom: 8px !important;
    }
    
    .card strong {
        color: #000000 !important;
    }

    .disclaimer {
        font-size: 0.8rem;
        color: #6c757d;
        border-top: 1px solid #dee2e6;
        padding-top: 15px;
        margin-top: 30px;
    }
</style>
""", unsafe_allow_html=True)

ALL_QUESTIONS = INTEREST_QUESTIONS + APTITUDE_QUESTIONS

if "step" not in st.session_state:
    st.session_state.step = "welcome"
if "current_q" not in st.session_state:
    st.session_state.current_q = 0
if "user_answers" not in st.session_state:
    st.session_state.user_answers = {}

st.markdown("""
<div class="main-header">
    <span class="cui-badge"> WELCOME ! </span>
    <h1 style="margin-top:10px;">🎓 AI-Assisted Career Mentor </h1>
    <p>Discover Top-Demand, High-Income & Freelancing Careers in Pakistan tailored to your unique profile.</p>
</div>
""", unsafe_allow_html=True)

if st.session_state.step == "welcome":
    col1, col2 = st.columns([2, 1])
    with col1:
        st.subheader("Welcome to Your Intelligent Career Assessment")
        st.write("""
        This tool helps high school and intermediate students identify the most suitable career pathways in Pakistan.
        
        **What to Expect:**
        - **20 Interactive Questions:** 10 simple scenario-based interest questions + 10 straightforward aptitude questions.
        - **Data-Driven Scoring:** Combining logical reasoning, numerical skills, and personal preferences.
        - **AI-Powered Mentorship:** Detailed feedback powered by Groq LLM explaining your custom results.
        - **Focus on Local Demand & Freelancing:** Insights into domestic job markets and global remote options.
        """)
        
        if st.button("🚀 Start Assessment Now", type="primary", use_container_width=True):
            st.session_state.step = "assessment"
            st.session_state.current_q = 0
            st.session_state.user_answers = {}
            st.rerun()

    with col2:
        st.info("""
        💡 **Tips for best results:**
        - Answer interest questions based on your natural inclination.
        - Work through aptitude questions carefully.
        - Takes roughly 5 minutes to complete.
        """)

elif st.session_state.step == "assessment":
    total_q = len(ALL_QUESTIONS)
    current_idx = st.session_state.current_q
    q_data = ALL_QUESTIONS[current_idx]

    progress = (current_idx + 1) / total_q
    st.progress(progress)
    st.caption(f"Question **{current_idx + 1} of {total_q}** | Category: **{q_data['type'].upper()}**")

    st.markdown(f"### {q_data['question']}")

    options = q_data["options"]
    option_keys = list(options.keys())
    
    previous_ans = st.session_state.user_answers.get(q_data["id"], None)
    default_idx = option_keys.index(previous_ans) if previous_ans in option_keys else 0

    selected_choice = st.radio(
        "Select your response:",
        options=option_keys,
        format_func=lambda x: f"{x}) {options[x]}",
        index=default_idx,
        key=f"q_{q_data['id']}"
    )

    col_back, col_next = st.columns([1, 1])
    
    with col_back:
        if current_idx > 0:
            if st.button("⬅️ Previous", use_container_width=True):
                st.session_state.user_answers[q_data["id"]] = selected_choice
                st.session_state.current_q -= 1
                st.rerun()

    with col_next:
        if current_idx < total_q - 1:
            if st.button("Next ➡️", type="primary", use_container_width=True):
                st.session_state.user_answers[q_data["id"]] = selected_choice
                st.session_state.current_q += 1
                st.rerun()
        else:
            if st.button("🎯 Submit & View Results", type="primary", use_container_width=True):
                st.session_state.user_answers[q_data["id"]] = selected_choice
                st.session_state.step = "results"
                st.rerun()

elif st.session_state.step == "results":
    st.balloons()
    st.subheader("📊 Your Personalized Career Guidance Dashboard")

    top_careers, aptitude_scores, interest_scores = calculate_scores(
        st.session_state.user_answers, INTEREST_QUESTIONS, APTITUDE_QUESTIONS
    )

    st.markdown("### 🏆 Top 3 Recommended Career Pathways")
    cols = st.columns(3)
    
    for idx, item in enumerate(top_careers):
        career = item["details"]
        with cols[idx]:
            st.markdown(f"""
            <div class="card">
                <h3>#{idx+1} {item['career']}</h3>
                <h2>{item['suitability_score']}% <span style="font-size:14px; color:#444444; font-weight:normal;">Match</span></h2>
                <p><strong>Domestic Demand:</strong> {career['demand_in_pk']}</p>
                <p><strong>Freelance Potential:</strong> {career['freelance_potential']}</p>
            </div>
            """, unsafe_allow_html=True)

    tab1, tab2 = st.tabs(["🤖 AI Mentor Detailed Analysis", "📈 Aptitude & Interest Breakdown"])

    with tab1:
        st.markdown("### AI Mentorship Guidance")
        with st.spinner("Generating personalized career analysis via Groq LLM..."):
            ai_guidance = generate_ai_guidance(top_careers, aptitude_scores, interest_scores)
            st.markdown(ai_guidance)

    with tab2:
        col_chart1, col_chart2 = st.columns(2)
        with col_chart1:
            st.markdown("#### Aptitude Assessment Performance")
            df_apt = pd.DataFrame({
                "Category": [c.replace("_", " ").title() for c in aptitude_scores.keys()],
                "Score (%)": [v * 100 for v in aptitude_scores.values()]
            })
            fig_apt = px.bar(df_apt, x="Category", y="Score (%)", color="Score (%)", color_continuous_scale="Teal")
            st.plotly_chart(fig_apt, use_container_width=True)

        with col_chart2:
            st.markdown("#### Identified Interest Profile")
            if interest_scores:
                df_int = pd.DataFrame({
                    "Interest": list(interest_scores.keys()),
                    "Affinity": list(interest_scores.values())
                })
                fig_int = px.pie(df_int, names="Interest", values="Affinity", color_discrete_sequence=px.colors.qualitative.Set3)
                st.plotly_chart(fig_int, use_container_width=True)

    if st.button("🔄 Retake Assessment"):
        st.session_state.step = "welcome"
        st.session_state.current_q = 0
        st.session_state.user_answers = {}
        st.rerun()

st.markdown("""
<div class="disclaimer">
    <strong>Disclaimer:</strong> This application is an educational career-guidance tool designed to assist Pakistani students in exploring modern high-demand academic and freelancing pathways. It does not constitute a formal psychological diagnosis, certified academic advisory, or guarantee of employment outcomes.
</div>
""", unsafe_allow_html=True)
