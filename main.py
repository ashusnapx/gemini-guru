import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

# Step 1: Load environment variables
load_dotenv()

# Step 2: Configure Google Gemini Pro model
genai.configure(api_key=os.getenv('GOOGLE_GEMINI_KEY'))
model = genai.GenerativeModel('gemini-pro')

# Step 3: Define the role of Gemini Pro
def role_to_streamlit(role, response_text):
    return f'{role.capitalize()}: {response_text}'

# Function to get Gemini responses
def get_gemini_responses(input_prompt, user_input):
    response = model.generate_content([user_input, input_prompt])
    return response.text

# Step 4: Ask the application to store the context of chat
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

# Step 5: Set up the frontend
st.set_page_config(page_title='Gemini Guru', page_icon="🦚", layout="wide")
st.title('OneStop Solution For Your Problems - Gemini Guru 🦚')

# Job description input area
job_description = st.text_area('Pen down your problems:', key='input')

# Buttons
variant1 = st.button('Solution acc. to Mahabharata')
variant2 = st.button('Solution acc. to Ramayan')
variant3 = st.button('Solution acc. to Kabir')

# Input prompts
input_prompt_mahabharata = """
As a seeker of profound wisdom from the Mahabharata, I come to you with a question that weighs heavily on my mind. In the vast ocean of knowledge encapsulated in the Mahabharata, I seek your guidance to unravel the depths of its teachings.

...

I express my gratitude in advance for your invaluable guidance, and I eagerly anticipate the profound insights you will share from the epic Mahabharata. In the end of response, mention all possible reference all over internet, along with their links.
"""

input_prompt_ramayan = """
As a seeker of profound wisdom from the Ramayan, I come to you with a question that weighs heavily on my mind. In the expansive tapestry of the Ramayan's teachings, I seek your guidance to find a solution to my specific problem.

...

I express my gratitude in advance for your invaluable guidance, and I eagerly anticipate the profound insights you will share from the epic Ramayan.In the end of response, mention all possible reference all over internet, along with their links.
"""

input_prompt_kabir_ke_dohe = """
As a seeker of profound wisdom from the teachings of Kabir Ke Dohe, I come to you with a question that holds deep significance for me. In the timeless verses of Kabir, I seek your guidance to find a solution to my specific problem.

...

I express my gratitude in advance for your invaluable guidance, and I eagerly anticipate the profound insights you will share from the teachings of Kabir.In the end of response, mention all possible reference all over internet, along with their links.
"""

# Button actions
if variant1:
    with st.spinner('Fetching response...'):
        response = get_gemini_responses(input_prompt_mahabharata, job_description)
    st.subheader('Solution acc. to Mahabharata:')
    st.write(response + "\n\nHare Krishna 🦚")

elif variant2:
    with st.spinner('Fetching response...'):
        response = get_gemini_responses(input_prompt_ramayan, job_description)
    st.subheader('Solution acc. to Ramayan:')
    st.write(response + "\n\nJai Shri Ram 🪔")

elif variant3:
    with st.spinner('Fetching response...'):
        response = get_gemini_responses(input_prompt_kabir_ke_dohe, job_description)
    st.subheader('Solution acc. to Kabir:')
    st.write(response)

# Footer
footer = """
<hr style="border:0.5px solid #808080">
<div style="display: flex; justify-content: space-between; align-items: center; padding-top: 10px; padding-bottom: 10px;">
    <div>
         <a href="https://ashusnapx.vercel.app/" target="_blank" style="font-size: 12px; text-decoration: none; color: #1DA1F2;">Ashutosh Kumar</a><br>
        <span style="font-size: 12px;">Software Developer</span>
    </div>
    <div>
        <a href="https://twitter.com/ashusnapx" target="_blank" style="font-size: 12px; text-decoration: none; color: #1DA1F2;">Twitter</a><br>
        <a href="https://www.linkedin.com/in/ashusnapx" target="_blank" style="font-size: 12px; text-decoration: none; color: #0077B5;">LinkedIn</a>
    </div>
</div>
"""

# Add footer to the page
st.markdown(footer, unsafe_allow_html=True)
