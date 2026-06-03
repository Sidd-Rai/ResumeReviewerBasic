from google import genai
import streamlit as st
import time

GEMINI_MODEL_NAME = "gemini-3.1-flash-lite"

def streamContent(message):
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

st.title("ChatGippity")
st.header("Start texting now!")
st.subheader("Type here bruh!")

message = st.text_input(
    label='(Currently \'G\' in "Gippity" stands for "Gajni", basically it forgets everything you\'ve said in the previous messages)',
    key="user_input"
)

if message:
    streamContent(message)
