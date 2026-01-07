def resume_review_prompt(resume_text):
    return f"""
You are an expert HR recruiter and ATS resume reviewer.

Analyze the resume and provide:

1. Resume Score (out of 10)
2. Strengths
3. Weaknesses
4. Missing or weak skills
5. Project improvement suggestions
6. ATS optimization tips
7. Improved professional summary (rewrite)

Resume Content:
{resume_text}

Give output in a clear, structured format.
"""
