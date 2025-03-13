import streamlit as st
import string
import random
import re

# Generate a random password generator
def password_generator(length,use_digit,use_special):
    character = string.ascii_letters

    if use_digit:
        character +=string.digits
    if use_special:
        character += string.punctuation
    
    return "".join(random.choice(character) for i in range(length))






def password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")
    #score 
    if score == 4:
        return "✅ Strong Password!", "Strong", feedback
    elif score == 3:
        return "⚠️ Moderate Password - Consider adding more security features.", "Moderate", feedback
    else:
        return "❌ Weak Password - Improve using the suggestions below.", "Weak", feedback

# Streamlit UI
st.title("🔐 Password Strength Checker")

check_password_strength = st.text_input("Enter your password!", type="password")

if st.button("Check Strength"):
    if check_password_strength:
        result, strength, feedback = password_strength(check_password_strength)

        if strength == "Strong":
            st.success(result)
            st.balloons()
        elif strength == "Moderate":
            st.warning(result)
            for tip in feedback:
                st.info(tip)  # Show improvement suggestions for Moderate passwords
        else:
            st.error(result)
            for tip in feedback:
                st.warning(tip)  # Show improvement suggestions for Weak passwords
    else:
        st.warning("Please enter a password!")

    





st.title("Password Generator") 
length = st.slider("Select your password Length", min_value=8 , value=12)
use_digit = st.checkbox("Include Digits") 
use_special = st.checkbox("Use Special Char")

if st.button("Generate Password"):
    password = password_generator(length,use_digit,use_special)
    st.success(f"Your Password is:{password}")




   


