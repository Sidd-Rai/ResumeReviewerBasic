import streamlit as st
import src.services.gemini_service as gem
import src.services.pdf_service as pd
st.title("Resume Review 👏🏻 👏🏻")
st.subheader("Upload you resume here!")
uploaded_file = st.file_uploader("Choose a file",type=["pdf"],accept_multiple_files=False, max_upload_size=2)
enable_job_description_box = st.radio("Tailor according to job description?",["Yes","No"])

if enable_job_description_box=="Yes":
    is_job_description_box_enabled = True
else:
    is_job_description_box_enabled = False
job_description=""
if(is_job_description_box_enabled):
    job_description = st.text_input("Enter the job description of your target role:")


if(st.button('Get insights')):
    if uploaded_file is not None:
        if is_job_description_box_enabled and job_description=="":
            st.text("Please enter the job description!")
        else:
            pdf_text = pd.read_pdf_text(uploaded_file)
            response = gem.send_pdf_text_to_gemini(pdf_text,job_description)
            st.text(response)
    else:
        st.text("No PDF uploaded!")
    pass