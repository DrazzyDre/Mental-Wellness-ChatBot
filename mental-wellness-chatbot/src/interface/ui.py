import sys
import os
import streamlit as st

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from src.chatbot import MentalWellnessChatbot

if 'chatbot' not in st.session_state:
    st.session_state['chatbot'] = MentalWellnessChatbot()
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

def main():
    st.title("Mental Wellness Chatbot")
    st.write("Welcome to the Mental Wellness Chatbot. How can I assist you today?")

    # Display chat history at the top
    for speaker, message in st.session_state['chat_history']:
        if speaker == "You":
            st.markdown(
                """
                <div style='display: flex; justify-content: flex-end;'>
                    <div style='background-color: #444; color: #fff; padding: 10px 16px; border-radius: 18px; margin: 4px 0 4px 40px; max-width: 70%; text-align: right;'>
                        {}</div>
                </div>
                """.format(message),
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                """
                <div style='display: flex; justify-content: flex-start;'>
                    <div style='background-color: #fff; color: #222; padding: 10px 16px; border-radius: 18px; margin: 4px 40px 4px 0; max-width: 70%; text-align: left; border: 1px solid #eee;'>
                        {}</div>
                </div>
                """.format(message),
                unsafe_allow_html=True,
            )

    # Add a large spacer so the input is always visible at the bottom
    st.markdown("<div style='height: 80px;'></div>", unsafe_allow_html=True)

    # Hide "Press Enter to submit form"
    st.markdown("""
        <style>
        div[role="form"] p,
        div[role="form"] label,
        div[role="form"] .stMarkdown {
            display: none !important;
        }
        div[role="form"] [data-testid="stMarkdownContainer"] {
            display: none !important;
        }
        </style>
    """, unsafe_allow_html=True)

    # Place the input form at the bottom of the app
    with st.form(key="chat_form", clear_on_submit=True):
        col1, col2 = st.columns([10, 1])
        user_input = col1.text_input(
            "", value="", placeholder="Type a message", label_visibility="collapsed"
        )
        send_clicked = col2.form_submit_button(
            label="✉️",  # Unicode envelope icon
            help="Send",
            use_container_width=True
        )
        if send_clicked and user_input.strip():
            response = st.session_state['chatbot'].process_input(user_input)
            st.session_state['chat_history'].append(("You", user_input))
            st.session_state['chat_history'].append(("Chatbot", response))
            st.rerun()

if __name__ == "__main__":
    main()