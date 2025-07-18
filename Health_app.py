import streamlit as st
import base64
import ollama

# --- Set Streamlit Page Config ---
st.set_page_config(page_title="HealthBuddy Chatbot", layout="wide")

# --- Student Info Header ---
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

# --- Load Background Image ---
def get_base64(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

bin_str = get_base64("meditation1.png")

# --- Apply Styles ---
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

# --- Initialize Session State ---
st.session_state.setdefault("conversation_history", [])

# --- General Chat Response ---
def generate_response(user_input):
    st.session_state["conversation_history"].append({"role": "user", "content": user_input})
    response = ollama.chat(model="llama2", messages=st.session_state["conversation_history"])
    ai_response = response['message']['content']
    st.session_state["conversation_history"].append({"role": "assistant", "content": ai_response})
    return ai_response

# --- Single-turn Prompt Helpers ---
def ask_ollama(prompt):
    response = ollama.chat(model="llama2", messages=[{"role": "user", "content": prompt}])
    return response['message']['content']

def generate_affirmation():
    return ask_ollama("Give me a daily positive affirmation.")

def generate_meditation_guide():
    return ask_ollama("Provide a 5-minute guided meditation for stress relief.")

def generate_breathing_exercise():
    return ask_ollama("Guide me through a 1-minute deep breathing exercise.")

def generate_wellness_tip():
    return ask_ollama("Give a helpful daily mental wellness tip.")

def get_health_tip():
    return ask_ollama("Give a short daily health tip in one sentence.")

def get_yoga_tip():
    return ask_ollama("Give a short and practical daily yoga tip for relaxation or flexibility. Keep it simple and under 20 words.")

# --- Title ---
st.title("🧘‍♀️ HealthBuddy – Your Mental Wellness Companion")

# --- Show Chat History ---
for msg in st.session_state["conversation_history"]:
    role_class = "user-bubble" if msg["role"] == "user" else "assistant-bubble"
    name = "You" if msg["role"] == "user" else "AI"
    st.markdown(
        f'<div class="chat-bubble {role_class}"><strong>{name}:</strong> {msg["content"]}</div>',
        unsafe_allow_html=True
    )

# --- Chat Input ---
user_message = st.text_input("💬 How can I help you today?")
if user_message:
    with st.spinner("🤖 Thinking..."):
        ai_response = generate_response(user_message)
        st.markdown(
            f'<div class="chat-bubble assistant-bubble"><strong>AI:</strong> {ai_response}</div>',
            unsafe_allow_html=True
        )

# --- Action Buttons ---
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🌈 Positive Affirmation"):
        st.markdown(f'<div class="chat-bubble assistant-bubble"><strong>Affirmation:</strong> {generate_affirmation()}</div>', unsafe_allow_html=True)
    if st.button("🧘 Breathing Exercise"):
        st.markdown(f'<div class="chat-bubble assistant-bubble"><strong>Breathing:</strong><br>{generate_breathing_exercise()}</div>', unsafe_allow_html=True)
    if st.button("💡 Health Tip"):
        st.markdown(f'<div class="chat-bubble assistant-bubble"><strong>Health Tip:</strong> {get_health_tip()}</div>', unsafe_allow_html=True)

with col2:
    if st.button("🧘‍♂️ Guided Meditation"):
        st.markdown(f'<div class="chat-bubble assistant-bubble"><strong>Meditation:</strong><br>{generate_meditation_guide()}</div>', unsafe_allow_html=True)
    if st.button("🌿 Wellness Tip"):
        st.markdown(f'<div class="chat-bubble assistant-bubble"><strong>Wellness Tip:</strong> {generate_wellness_tip()}</div>', unsafe_allow_html=True)
    if st.button("🧘 Daily Yoga Tip"):
        st.markdown(f'<div class="chat-bubble assistant-bubble"><strong>Yoga Tip:</strong> {get_yoga_tip()}</div>', unsafe_allow_html=True)





   








        