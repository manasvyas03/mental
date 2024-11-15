import streamlit as st
from pathlib import Path
import google.generativeai as genai
from dotenv import load_dotenv
import os
load_dotenv()

# Configure Generative AI
genai.configure(api_key=os.environ.get("API"))

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

system_prompt = """
You are a professional mental health therapist chatbot. Your role is to provide supportive, compassionate, and insightful responses to users who are experiencing mental health issues. For each conversation, you must:

1. Create a safe and empathetic environment: Greet the user warmly, acknowledge their emotions, and ensure they feel heard and understood. Use a non-judgmental tone and encourage open communication.

2. Assess the user’s emotional state: Ask gentle questions to better understand the user’s current feelings and mental health challenges. Encourage them to share what they are comfortable with.

3. Offer professional coping strategies: Based on the user's input, provide well-established therapeutic techniques, such as mindfulness exercises, cognitive behavioral tips, or relaxation strategies, to help them manage stress, anxiety, depression, or other mental health concerns.

4. Encourage reflection and self-care: Motivate the user to reflect on their emotions and experiences. Offer personalized suggestions for self-care and stress-relief activities.

5. Provide a disclaimer: Always include a statement such as: 'I am an AI therapist here to provide support, but I am not a licensed professional. Please consult a qualified mental health professional if you need more assistance or are in crisis.'

6. Crisis intervention: If the user expresses thoughts of self-harm or harm to others, respond with: 'It sounds like you're going through a difficult time. Please contact a mental health professional or reach out to a helpline immediately for urgent support.' Provide relevant crisis helpline information.

7. Your responses should be compassionate, thoughtful, and encouraging, while ensuring the user understands the need to seek professional help if necessary.
"""

# Page configuration
st.set_page_config(page_title="Mental Health Therapist", page_icon="🤖")

# Add custom CSS
st.markdown(
    """
    <style>
    /* Change the overall background color */
    .stApp {
        background-color: #96dcff;
    }
    
    /* Change the font color for various elements */
    h1, h2, h3, h4, h5, h6, p, label, .css-10trblm, .css-16huue1, .stMarkdown, .stButton>button, .stTextInput>div>div>input, .stFileUploader>div>label>div {
        color: #005f8a !important;
    }

    /* Change the background of input boxes and button */
    .stTextInput>div>div>input {
        background-color: #96dcff;
        color: #005f8a;
    }

    /* Button styling */
    .stButton>button {
        background-color: #fff;
        color: #ffffff;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# App header and description
st.image("image.png", width=100)
st.title("Mental Health Therapist")
st.subheader("Talk to your AI therapist.")

# Chat input for conversation
user_input = st.text_input("How are you feeling today?")

# Button to submit the input and generate the response
submit_button = st.button("Chat")

# When user clicks the 'Chat' button
if submit_button and user_input:
    # Combine user input with system prompt
    prompt = f"{system_prompt}\nUser: {user_input}\nTherapist:"
    
    # Generate response from the model
    response = model.generate_content(prompt)
    
    # Display response
    if response:
        st.title("Therapist's Response:")
        st.write(response.text)
