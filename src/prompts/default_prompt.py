# PROMPT_PREFIX = "You are going to point out possible improvements in this resume: <RESUME_START> "
# PROMPT_SUFFIX = " <RESUME_END> "
# PROMPT_JD_PREFIX = "Tailor the suggestions according to this job description: <JOB_DESCRIPTION_START> "
# PROMPT_JD_SUFFIX = "<JOB_DESCRIPTION_END> "

PROMPT_PREFIX = """
You are an expert resume reviewer and ATS system.

Your task is to analyze the resume and provide actionable, specific improvements, in a concise and point to point manner.

RESUME:
<RESUME_START>
"""

PROMPT_SUFFIX = """
<RESUME_END>

Return your response in the following structure:

1. ATS Score (0-100)
2. Strengths
3. Weaknesses
4. Missing Keywords
5. Suggested Improvements (bullet points)
6. Final Verdict
"""


PROMPT_JD_PREFIX = """
Analyze the resume against the given job description and suggest improvements.

JOB DESCRIPTION:
<JOB_DESCRIPTION_START>
"""

PROMPT_JD_SUFFIX = """
<JOB_DESCRIPTION_END>
"""

