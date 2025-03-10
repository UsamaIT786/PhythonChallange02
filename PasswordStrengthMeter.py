import re
import streamlit as st

st.set_page_config(page_title="Password Checker App Develop By Usama Muzammil", page_icon="🌘", layout="centered")

# Custom CSS
st.markdown("""
    <style>
        body {
            background-color: #1e1e2e;
            color: #ffffff;
            font-family: Arial, sans-serif;
        }
        .stApp {
            background-color: #1e1e2e;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 4px 10px rgba(255, 255, 255, 0.1);
        }
        .stTextInput, .stButton > button {
            background-color: #282c34;
            color: white;
            border-radius: 5px;
            border: none;
        }
        .stButton > button:hover {
            background-color: #ff4b4b;
        }
        .result {
            font-size: 20px;
            font-weight: bold;
            color: #00ff00;
        }
    </style>
""", unsafe_allow_html=True)

def check_password_strength(password):
    strength = 0
    remarks = ""
    
    # Length Check
    if len(password) >= 8:
        strength += 1
    
    # Uppercase Letter Check
    if re.search(r"[A-Z]", password):
        strength += 1
    
    # Lowercase Letter Check
    if re.search(r"[a-z]", password):
        strength += 1
    
    # Number Check
    if re.search(r"[0-9]", password):
        strength += 1
    
    # Special Character Check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    
    # Strength Evaluation
    if strength == 5:
        remarks = "Very Strong"
    elif strength == 4:
        remarks = "Strong"
    elif strength == 3:
        remarks = "Moderate"
    elif strength == 2:
        remarks = "Weak"
    else:
        remarks = "Very Weak"
    
    return remarks

st.title("🔒 Password Strength Checker ")
password = st.text_input("Enter your password:", type="password")

if password:
    strength_result = check_password_strength(password)
    st.markdown(f'<p class="result">Password Strength: {strength_result}</p>', unsafe_allow_html=True)
