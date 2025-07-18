import streamlit as st
import ollama
import base64

# Set page config
st.markdown("""
    <div style="text-align: center; padding: 20px; background-color: rgba(255, 255, 255, 0.1); border-radius: 12px; margin-top: 20px;">
        <h4 style="margin-bottom: 10px; color: #ffffff;">Panchani Ruchit Maheshbhai</h4>
        <p style="margin: 4px 0; font-size: 16px; color: #ffffff;">Computer Engineering – Semester 7</p>
        <p style="margin: 4px 0; font-size: 16px; color: #ffffff;">
            Shree Swami Atmanand Saraswati Institute of Technology<br>
            <strong>College Code:</strong> 076 &nbsp;|&nbsp; <strong>Branch Code:</strong> 07
        </p>
        <p style="margin: 6px 0; font-size: 16px; color: #ffffff;"><strong>Enrollment No:</strong> 220760107087</p>
    </div>
""", unsafe_allow_html=True)
st.set_page_config(page_title="HealthBuddy Chatbot", layout="wide")

# Background image setup
def get_base64(image_path):
    with open(image_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Load background image (you can change the file name accordingly)
bin_str = get_base64("meditation1.png")

st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{bin_str}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
        color: white;
    }}
    .chat-bubble {{
        background-color: rgba(0, 0, 0, 0.6);
        padding: 10px 15px;
        border-radius: 12px;
        margin-bottom: 10px;
        color: white;
    }}
    .user-bubble {{
        background-color: rgba(70, 130, 180, 0.8);
    }}
    .assistant-bubble {{
        background-color: rgba(34, 139, 34, 0.8);
    }}
    </style>
""", unsafe_allow_html=True)

# Initialize session state
st.session_state.setdefault('conversation_history', [])       

# Response Generator
def generate_response(user_input):
    st.session_state['conversation_history'].append({"role": "user", "content": user_input})
    response = ollama.chat(model="llama2", messages=st.session_state['conversation_history'])
    ai_response = response['message']['content']
    st.session_state['conversation_history'].append({"role": "assistant", "content": ai_response})
    return ai_response

# Affirmation Generator
def generate_affirmation():
    prompt = "Give a short, uplifting affirmation for mental wellness."
    response = ollama.chat(model="llama2", messages=[{"role": "user", "content": prompt}])
    return response['message']['content']

# Meditation Guide Generator
def generate_meditation_guide():
    prompt = "Provide a 5-minute guided meditation for stress relief."
    response = ollama.chat(model="llama2", messages=[{"role": "user", "content": prompt}])
    return response['message']['content']

# Wellness Tip Generator
def generate_wellness_tip():
    prompt = "Give a helpful daily mental wellness tip."
    response = ollama.chat(model="llama2", messages=[{"role": "user", "content": prompt}])
    return response['message']['content']

# Breathing Exercise Generator
def generate_breathing_exercise():
    prompt = "Guide me through a 1-minute deep breathing exercise."
    response = ollama.chat(model="llama2", messages=[{"role": "user", "content": prompt}])
    return response['message']['content']

def get_health_tip():
    tip_prompt = "Give a short daily health tip in one sentence."
    response = ollama.chat(model="llama2", messages=[{"role":"user", "content":tip_prompt}])
    return response['message']['content']

def get_yoga_tip():
    prompt = "Give a short and practical daily yoga tip for relaxation or flexibility. Keep it simple and under 20 words."
    response = ollama.chat(model="llama2", messages=[{"role":"user", "content":prompt}])
    return response['message']['content']


# App Title
st.title("🧘‍♀️ HealthBuddy – Your Mental Wellness Companion")

# Display chat history
for msg in st.session_state['conversation_history']:
    role_class = "user-bubble" if msg['role'] == "user" else "assistant-bubble"
    st.markdown(
        f'<div class="chat-bubble {role_class}"><strong>{"You" if msg["role"]=="user" else "AI"}:</strong> {msg["content"]}</div>',
        unsafe_allow_html=True
    )

# User input
user_message = st.text_input("💬 How can I help you today?")
if user_message:
    with st.spinner("🤖 Thinking..."):
        ai_response = generate_response(user_message)
        st.markdown(
            f'<div class="chat-bubble assistant-bubble"><strong>AI:</strong> {ai_response}</div>',
            unsafe_allow_html=True
        )

# Logical layout for wellness tools
col1, col2 , col3= st.columns(3)

with col1:
    if st.button("🌈 Positive Affirmation"):
        affirmation = generate_affirmation()
        st.markdown(
            f'<div class="chat-bubble assistant-bubble"><strong>Affirmation:</strong> {affirmation}</div>',
            unsafe_allow_html=True
        )
    if st.button("🧘 Breathing Exercise"):
        breathing = generate_breathing_exercise()
        st.markdown(
            f'<div class="chat-bubble assistant-bubble"><strong>Breathing Exercise:</strong><br>{breathing}</div>',
            unsafe_allow_html=True
        )
    if st.button("💡 Health Tip"):
        tip = get_health_tip()
        st.markdown(f'<div class="chat-bubble assistant-bubble"><strong>Tip:</strong> {tip}</div>', unsafe_allow_html=True)

with col2:
    if st.button("🧘‍♂️ Guided Meditation"):
        meditation_guide = generate_meditation_guide()
        st.markdown(
            f'<div class="chat-bubble assistant-bubble"><strong>Guided Meditation:</strong><br>{meditation_guide}</div>',
            unsafe_allow_html=True
        )
    if st.button("🌿 Wellness Tip"):
        tip = generate_wellness_tip()
        st.markdown(
            f'<div class="chat-bubble assistant-bubble"><strong>Wellness Tip:</strong> {tip}</div>',
            unsafe_allow_html=True
        )


    if st.button("🧘 Daily Yoga Tip"):
        yoga_tip = get_yoga_tip()
        st.markdown(
            f'<div class="chat-bubble assistant-bubble"><strong>Yoga Tip:</strong> {yoga_tip}</div>',
            unsafe_allow_html=True
        )


   








        