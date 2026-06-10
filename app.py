import streamlit as st
import speech_recognition as sr
from datetime import date, datetime

# Khởi tạo recognizer
robot_ear = sr.Recognizer()

st.title("🤖 Voice Assistant")

st.write("Nhấn nút bên dưới và nói vào microphone")

if st.button("🎤 Start Listening"):

    with sr.Microphone() as mic:
        st.info("Robot: I'm listening...")
        audio = robot_ear.listen(mic)

    try:
        you = robot_ear.recognize_google(audio)
        st.success(f"You said: {you}")
    except:
        you = ""
        st.error("Không nhận diện được giọng nói")

    # Xử lý câu lệnh
    if you == "":
        robot_brain = "Can you try again?"

    elif "hello" in you.lower():
        robot_brain = "Hello Duyen"

    elif "today" in you.lower():
        today = date.today()
        robot_brain = today.strftime('%b-%d-%y')

    elif "time" in you.lower():
        now = datetime.now()
        robot_brain = now.strftime('%H:%M:%S')

    elif "bye" in you.lower():
        robot_brain = "Bye Duyen"

    else:
        robot_brain = "I don't know"

    st.write("### 🤖 Robot:")
    st.write(robot_brain)
