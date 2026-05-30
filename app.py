import streamlit as st
import google.generativeai as genai

# Set your API key here
genai.configure(api_key="AIzaSyB9P7zcbvgbeWEUQtKZzSENDuGIVCA7Nkk")
model = genai.GenerativeModel("gemini-1.5-flash")

st.set_page_config(page_title="PrepMentor AI")

st.title("🚀 PrepMentor AI")
st.subheader("AI Adaptive Study Planner for GATE & Placements")

name = st.text_input("Enter your name")
goal = st.selectbox("Select your goal", ["GATE", "Placements", "Both"])
hours = st.slider("Daily Study Hours", 1, 12, 4)
weak = st.text_input("Weak Subjects (comma separated)")

if st.button("Generate AI Study Plan"):
    prompt = f"""
    You are an AI study mentor.

    Student Name: {name}
    Goal: {goal}
    Daily Study Hours: {hours}
    Weak Subjects: {weak}

    Create a structured daily study plan for 7 days.
    Include:
    - Day-wise schedule
    - Subject priority
    - Revision tips
    """

    response = model.generate_content(prompt)

    st.success("Your AI Study Plan is ready 🚀")
    st.write(response.text)