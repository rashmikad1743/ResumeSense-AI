import streamlit as st
from pdf_reader import read_resume
from prompt import resume_review_prompt
from groq_model import get_groq_response

st.set_page_config(page_title="ResumeSense AI", layout="centered")

st.title("🤖 ResumeSense AI")
st.write("Upload your resume (PDF) and get AI-powered feedback")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

if uploaded_file:
    st.success("Resume uploaded successfully!")

    if st.button("Review Resume"):
        with st.spinner("Analyzing your resume..."):
            try:
                resume_text = read_resume(uploaded_file)
                prompt = resume_review_prompt(resume_text)
                response = get_groq_response(prompt)

                st.subheader("📄 Resume Review Report")
                st.write(response)
            except Exception as e:
                st.error(f"Configuration error: {e}")
                st.info("Set GROQ_API_KEY via environment, .env, or Streamlit secrets.")
