from google import genai
import streamlit as st

GEMINI_MODEL_NAME = "gemini-3.1-flash-lite"
def generateContent(message):
    if(message):
        if len(message)<3:
            st.text("Message too short!")
        else:
            client = genai.Client()
            response = client.models.generate_content(
                model = GEMINI_MODEL_NAME,
                contents=message
                )
            st.text(response.text)
            st.text("Output generated") 
    return

st.title("ChatGippity")
st.header("Start texting now!")
message = st.text_input("(Currently 'G' in \"Gippity\" stands for \"Gajni\", basically it forgets everything you've said in the previous messages)")
generateContent(message)
