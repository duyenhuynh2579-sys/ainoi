import streamlit as st
import speech_recognition as sr
from datetime import date, datetime

# Cấu hình trang
st.set_page_config(
    page_title="Voice Assistant",
    page_icon="🤖"
)

st.title("🤖 Voice Assistant")

# Khởi tạo session state
if "history" not in st.session_state:
    st.session_state.history = []

robot_ear = sr.Recognizer()

def process_command(text):
    text = text.lower()

    if not text:
        return "Can you try again?"

    elif "hello" in text:
        return "Hello Duyen"

    elif "today" in text:
        return date.today().strftime("%b-%d-%Y")

    elif "time" in text:
        return datetime.now().strftime("%H:%M:%S")

    elif "bye" in text:
        return "Bye Duyen"

    else:
        return "I don't know"

# Nút ghi âm
if st.button("🎤 Start Listening"):

    try:
        with sr.Microphone() as mic:

            st.info("Listening...")

            # Giảm nhiễu môi trường
            robot_ear.adjust_for_ambient_noise(mic, duration=1)

            audio = robot_ear.listen(
                mic,
                timeout=5,
                phrase_time_limit=10
            )

        # Nếu nói tiếng Việt:
        # you = robot_ear.recognize_google(audio, language="vi-VN")

        # Nếu nói tiếng Anh:
        you = robot_ear.recognize_google(audio, language="en-US")

        st.success(f"You: {you}")

        robot_brain = process_command(you)

        st.session_state.history.append(
            {"user": you, "bot": robot_brain}
        )

    except sr.WaitTimeoutError:
        st.error("Không nghe thấy giọng nói.")

    except sr.UnknownValueError:
        st.error("Không nhận diện được nội dung.")

    except sr.RequestError:
        st.error("Lỗi kết nối tới Google Speech API.")

    except Exception as e:
        st.error(f"Lỗi: {e}")

# Hiển thị lịch sử chat
if st.session_state.history:
    st.subheader("📜 Conversation History")

    for item in reversed(st.session_state.history):
        st.write(f"🧑 You: {item['user']}")
        st.write(f"🤖 Robot: {item['bot']}")
        st.divider()
