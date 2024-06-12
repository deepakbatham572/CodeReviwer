import streamlit as st
from io import StringIO
from utils import *
import time
import base64

if 'API_KEY' not in st.session_state:
    st.session_state['API_KEY'] = ''


def text_downloader(raw_text):
    # Generate a timestamp for the filename to ensure uniqueness
    timestr = time.strftime("%Y%m%d-%H%M%S")
    
    # Encode the raw text in base64 format for file download
    b64 = base64.b64encode(raw_text.encode()).decode()
    
    # Create a new filename with a timestamp
    new_filename = "code_review_analysis_file_{}_.txt".format(timestr)
    
    st.markdown("#### Download File ✅###")
    
    # Create an HTML link with the encoded content and filename for download
    href = f'<a href="data:file/txt;base64,{b64}" download="{new_filename}">Click Here!!</a>'
    
    # Display the HTML link using Streamlit markdown
    st.markdown(href, unsafe_allow_html=True)


st.set_page_config("Code Reviewer" , page_icon=':moon:')
st.sidebar.title("😎🔑")
st.session_state['API_KEY'] = st.sidebar.text_input("Enter your Hugging face API key here" , type="password")
st.title("Hey i am helping to review the code")

st.header("Please upload your file here:")

data = st.file_uploader("Upload python file",type= ['.py'  ,'.c' , '.java'])

if data:
    
    # Create a StringIO object and initialize it with the decoded content of 'data'
    stringio = StringIO(data.getvalue().decode('utf-8'))

    # Read the content of the StringIO object and store it in the variable 'read_data'
    fetched_data = stringio.read()

    # Optionally, uncomment the following line to write the read data to the streamlit app
    st.write(fetched_data)

    response = getLLMResponse(fetched_data ,st.session_state['API_KEY'])
    st.write(response)
    text_downloader(response)

