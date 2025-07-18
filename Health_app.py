# import streamlit as st
# import google.generativeai as genai
# import base64

# genai.configure(api_key=st.secrets["AIzaSyAtntgrtCLD-7fsiUxj3uhqHwG07vMEmo4"])

# # Set page config
# st.markdown("""
#     <div style="text-align: center; padding: 20px; background-color: rgba(255, 255, 255, 0.1); border-radius: 12px; margin-top: 20px;">
#         <h4 style="margin-bottom: 10px; color: #ffffff;">Panchani Ruchit Maheshbhai</h4>
#         <p style="margin: 4px 0; font-size: 16px; color: #ffffff;">Computer Engineering – Semester 7</p>
#         <p style="margin: 4px 0; font-size: 16px; color: #ffffff;">
#             Shree Swami Atmanand Saraswati Institute of Technology<br>
#             <strong>College Code:</strong> 076 &nbsp;|&nbsp; <strong>Branch Code:</strong> 07
#         </p>
#         <p style="margin: 6px 0; font-size: 16px; color: #ffffff;"><strong>Enrollment No:</strong> 220760107087</p>
#     </div>
# """, unsafe_allow_html=True)
# st.set_page_config(page_title="HealthBuddy Chatbot", layout="wide")

# # Background image setup
# def get_base64(image_path):
#     with open(image_path, "rb") as f:
#         data = f.read()
#     return base64.b64encode(data).decode()

# # Load background image (you can change the file name accordingly)
# bin_str = get_base64("meditation1.png")

# st.markdown(f"""
#     <style>
#     .stApp {{
#         background-image: url("data:image/png;base64,{bin_str}");
#         background-size: cover;
#         background-position: center;
#         background-repeat: no-repeat;
#         background-attachment: fixed;
#         color: white;
#     }}
#     .chat-bubble {{
#         background-color: rgba(0, 0, 0, 0.6);
#         padding: 10px 15px;
#         border-radius: 12px;
#         margin-bottom: 10px;
#         color: white;
#     }}
#     .user-bubble {{
#         background-color: rgba(70, 130, 180, 0.8);
#     }}
#     .assistant-bubble {{
#         background-color: rgba(34, 139, 34, 0.8);
#     }}
#     </style>
# """, unsafe_allow_html=True)

# # Initialize session state
# st.session_state.setdefault('conversation_history', [])       

# # Response Generator
# def generate_response(user_input):
#     st.session_state['conversation_history'].append({"role": "user", "content": user_input})

#     model = genai.GenerativeModel('gemini-pro')
#     chat = model.start_chat(history=st.session_state['conversation_history'])

#     response = chat.send_message(user_input)
#     ai_response = response.text

#     st.session_state['conversation_history'].append({"role": "assistant", "content": ai_response})
#     return ai_response


# # Affirmation Generator
# def generate_affirmation():
#     prompt = "Give me a daily positive affirmation."
#     model = genai.GenerativeModel('gemini-pro')
#     response = model.generate_content(prompt)
#     return response.text

# # Meditation Guide Generator
# def generate_meditation_guide():
#     prompt = "Provide a 5-minute guided meditation for stress relief."
#     response = ollama.chat(model="llama2", messages=[{"role": "user", "content": prompt}])
#     return response['message']['content']

# # Wellness Tip Generator
# def generate_wellness_tip():
#     prompt = "Give a helpful daily mental wellness tip."
#     response = ollama.chat(model="llama2", messages=[{"role": "user", "content": prompt}])
#     return response['message']['content']

# # Breathing Exercise Generator
# def generate_breathing_exercise():
#     prompt = "Guide me through a 1-minute deep breathing exercise."
#     response = ollama.chat(model="llama2", messages=[{"role": "user", "content": prompt}])
#     return response['message']['content']

# def get_health_tip():
#     tip_prompt = "Give a short daily health tip in one sentence."
#     response = ollama.chat(model="llama2", messages=[{"role":"user", "content":tip_prompt}])
#     return response['message']['content']

# def get_yoga_tip():
#     prompt = "Give a short and practical daily yoga tip for relaxation or flexibility. Keep it simple and under 20 words."
#     response = ollama.chat(model="llama2", messages=[{"role":"user", "content":prompt}])
#     return response['message']['content']


# # App Title
# st.title("🧘‍♀️ HealthBuddy – Your Mental Wellness Companion")

# # Display chat history
# for msg in st.session_state['conversation_history']:
#     role_class = "user-bubble" if msg['role'] == "user" else "assistant-bubble"
#     st.markdown(
#         f'<div class="chat-bubble {role_class}"><strong>{"You" if msg["role"]=="user" else "AI"}:</strong> {msg["content"]}</div>',
#         unsafe_allow_html=True
#     )

# # User input
# user_message = st.text_input("💬 How can I help you today?")
# if user_message:
#     with st.spinner("🤖 Thinking..."):
#         ai_response = generate_response(user_message)
#         st.markdown(
#             f'<div class="chat-bubble assistant-bubble"><strong>AI:</strong> {ai_response}</div>',
#             unsafe_allow_html=True
#         )

# # Logical layout for wellness tools
# col1, col2 , col3= st.columns(3)

# with col1:
#     if st.button("🌈 Positive Affirmation"):
#         affirmation = generate_affirmation()
#         st.markdown(
#             f'<div class="chat-bubble assistant-bubble"><strong>Affirmation:</strong> {affirmation}</div>',
#             unsafe_allow_html=True
#         )
#     if st.button("🧘 Breathing Exercise"):
#         breathing = generate_breathing_exercise()
#         st.markdown(
#             f'<div class="chat-bubble assistant-bubble"><strong>Breathing Exercise:</strong><br>{breathing}</div>',
#             unsafe_allow_html=True
#         )
#     if st.button("💡 Health Tip"):
#         tip = get_health_tip()
#         st.markdown(f'<div class="chat-bubble assistant-bubble"><strong>Tip:</strong> {tip}</div>', unsafe_allow_html=True)

# with col2:
#     if st.button("🧘‍♂️ Guided Meditation"):
#         meditation_guide = generate_meditation_guide()
#         st.markdown(
#             f'<div class="chat-bubble assistant-bubble"><strong>Guided Meditation:</strong><br>{meditation_guide}</div>',
#             unsafe_allow_html=True
#         )
#     if st.button("🌿 Wellness Tip"):
#         tip = generate_wellness_tip()
#         st.markdown(
#             f'<div class="chat-bubble assistant-bubble"><strong>Wellness Tip:</strong> {tip}</div>',
#             unsafe_allow_html=True
#         )


#     if st.button("🧘 Daily Yoga Tip"):
#         yoga_tip = get_yoga_tip()
#         st.markdown(
#             f'<div class="chat-bubble assistant-bubble"><strong>Yoga Tip:</strong> {yoga_tip}</div>',
#             unsafe_allow_html=True
#         )


import streamlit as st
import base64
import google.generativeai as genai

# Set page config
st.set_page_config(page_title="HealthBuddy Chatbot", layout="wide")

# 🔐 Check and configure Gemini API key from secrets
if "GOOGLE_API_KEY" not in st.secrets:
    st.error("Google API key not found in secrets.toml")
    st.stop()  # Stop execution if no key
else:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# 🖼️ Load and encode background image
def get_base64(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

bin_str = get_base64("meditation1.png")  # ✅ Make sure this file is present

# 🧑‍🎨 Apply background style
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
    .user-bubble {{ background-color: rgba(70, 130, 180, 0.8); }}
    .assistant-bubble {{ background-color: rgba(34, 139, 34, 0.8); }}
    </style>
""", unsafe_allow_html=True)

# 🧠 Set up chat session
st.session_state.setdefault("conversation_history", [])

# Initialize Gemini model
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=st.session_state["conversation_history"])

# 🧾 Response function
def generate_response(user_input):
    st.session_state["conversation_history"].append({"role": "user", "parts": [user_input]})
    response = chat.send_message(user_input)
    ai_response = response.text
    st.session_state["conversation_history"].append({"role": "model", "parts": [ai_response]})
    return ai_response

# 📌 Reusable prompt handler
def ask_gemini(prompt):
    response = model.generate_content(prompt)
    return response.text

# ✨ Specialized prompt functions
def generate_affirmation():
    return ask_gemini("Give a short, uplifting affirmation for mental wellness.")

def generate_meditation_guide():
    return ask_gemini("Provide a 5-minute guided meditation for stress relief.")

def generate_breathing_exercise():
    return ask_gemini("Guide me through a 1-minute deep breathing exercise.")

def get_health_tip():
    return ask_gemini("Give a short daily health tip in one sentence.")

def get_yoga_tip():
    return ask_gemini("Give a short and practical daily yoga tip for relaxation or flexibility. Keep it simple and under 20 words.")

def generate_wellness_tip():
    return ask_gemini("Give a helpful daily mental wellness tip.")

# 🏷️ Title
st.title("🧘‍♀️ HealthBuddy – Your Mental Wellness Companion")

# 🗨️ Display chat history
for msg in st.session_state["conversation_history"]:
    role = "You" if msg["role"] == "user" else "AI"
    style = "user-bubble" if role == "You" else "assistant-bubble"
    content = msg["parts"][0]
    st.markdown(f'<div class="chat-bubble {style}"><strong>{role}:</strong> {content}</div>', unsafe_allow_html=True)

# 💬 Chat input
user_message = st.text_input("💬 How can I help you today?")
if user_message:
    with st.spinner("🤖 Thinking..."):
        ai_response = generate_response(user_message)
        st.markdown(f'<div class="chat-bubble assistant-bubble"><strong>AI:</strong> {ai_response}</div>', unsafe_allow_html=True)

# ➕ Wellness Features
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🌈 Positive Affirmation"):
        st.markdown(f'<div class="chat-bubble assistant-bubble"><strong>Affirmation:</strong> {generate_affirmation()}</div>', unsafe_allow_html=True)
    if st.button("🦼 Breathing Exercise"):
        st.markdown(f'<div class="chat-bubble assistant-bubble"><strong>Breathing:</strong><br>{generate_breathing_exercise()}</div>', unsafe_allow_html=True)
    if st.button("💡 Health Tip"):
        st.markdown(f'<div class="chat-bubble assistant-bubble"><strong>Health Tip:</strong> {get_health_tip()}</div>', unsafe_allow_html=True)

with col2:
    if st.button("🧘‍♂️ Guided Meditation"):
        st.markdown(f'<div class="chat-bubble assistant-bubble"><strong>Guided Meditation:</strong><br>{generate_meditation_guide()}</div>', unsafe_allow_html=True)
    if st.button("🌿 Wellness Tip"):
        st.markdown(f'<div class="chat-bubble assistant-bubble"><strong>Wellness Tip:</strong> {generate_wellness_tip()}</div>', unsafe_allow_html=True)
    if st.button("🧘 Daily Yoga Tip"):
        st.markdown(f'<div class="chat-bubble assistant-bubble"><strong>Yoga Tip:</strong> {get_yoga_tip()}</div>', unsafe_allow_html=True)


   








        