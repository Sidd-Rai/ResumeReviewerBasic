from google import genai
from src.config.settings import GEMINI_MODEL_NAME
from src.prompts.default_prompt import PROMPT_PREFIX
from src.prompts.default_prompt import PROMPT_SUFFIX
from src.prompts.default_prompt import PROMPT_JD_PREFIX
from src.prompts.default_prompt import PROMPT_JD_SUFFIX  

def construct_prompt(pdf_text,job_description):
    prompt = PROMPT_PREFIX + pdf_text
    if(job_description==""):
        prompt += PROMPT_SUFFIX
    else:
        prompt += PROMPT_SUFFIX + PROMPT_JD_PREFIX + job_description + PROMPT_JD_SUFFIX
    return prompt

def send_pdf_text_to_gemini(pdf_text,job_description=""):
    client = genai.Client()
    response = client.models.generate_content(
        model=GEMINI_MODEL_NAME,
        contents=construct_prompt(pdf_text,job_description)
    )
    return response.text

    if message:
        if len(message) < 3:
            st.error("Message too short!")
        else:
            client = genai.Client()
            response = client.models.generate_content_stream(
                model=GEMINI_MODEL_NAME,
                contents=message
            )
            
            placeholder = st.empty()
            full_text = ""
            
            for chunk in response:
                if chunk.text:
                    words = chunk.text.split(" ")
                    for index,word in enumerate(words):
                        full_text += word
                        if index < len(words) - 1:
                            full_text += " "
                        placeholder.markdown(full_text + "▌")   
                        time.sleep(0.05)     
            placeholder.markdown(full_text)
            st.caption("Output generated")  
    return