import sys
import os
import streamlit as st
from datetime import datetime

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
    for speaker, message, timestamp in st.session_state['chat_history']:
        if speaker == "You":
            st.markdown(
                f"""
                <div style='display: flex; justify-content: flex-end;'>
                    <div style='background-color: #444; color: #fff; padding: 10px 16px; border-radius: 18px; margin: 4px 0 4px 40px; max-width: 70%; text-align: right;'>
                    {message}
                    <span style='font-size: 0.8em; color: #bbb; float: right; margin-left: 10px;'>{timestamp}</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        else:
            st.markdown(
                f"""
                <div style='display: flex; justify-content: flex-start;'>
                    <div style='background-color: #fff; color: #222; padding: 10px 16px; border-radius: 18px; margin: 4px 40px 4px 0; max-width: 70%; text-align: left; border: 1px solid #eee;'>
                        {message}
                        <span style='font-size: 0.8em; color: #888; float: right; margin-left: 10px;'>{timestamp}</span>
                    </div>
                </div>
                """,
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
            timestamp = datetime.now().strftime("%H:%M")
            st.session_state['chat_history'].append(("You", user_input, timestamp))  # Show user message immediately
            # Limit chat history to last 50 messages
            MAX_HISTORY = 50
            if len(st.session_state['chat_history']) > MAX_HISTORY:
                st.session_state['chat_history'] = st.session_state['chat_history'][-MAX_HISTORY:]
            # Append bot is thinking placeholder
            st.session_state['chat_history'].append(("Chatbot", "Bot is thinking...", timestamp))
            if len(st.session_state['chat_history']) > MAX_HISTORY:
                st.session_state['chat_history'] = st.session_state['chat_history'][-MAX_HISTORY:]
            st.rerun()

    # After rerun, if last message is "Bot is thinking...", replace it with real response
    if (
        st.session_state['chat_history']
        and st.session_state['chat_history'][-1][0] == "Chatbot"
        and st.session_state['chat_history'][-1][1] == "Bot is thinking..."
    ):
        with st.spinner("Bot is thinking..."):
            user_message = None
            # Find the last user message
            for speaker, message, _ in reversed(st.session_state['chat_history']):
                if speaker == "You":
                    user_message = message
                    break
            if user_message:
                try:
                    response = st.session_state['chatbot'].process_input(user_message)
                except Exception:
                    response = "Sorry, I'm having trouble responding right now. Please try again later."
                timestamp = datetime.now().strftime("%H:%M")
                st.session_state['chat_history'][-1] = ("Chatbot", response, timestamp)
                st.rerun()

    # Clear chat button
    if st.button("🗑️ Clear Chat"):
        st.session_state['chat_history'] = []
        st.rerun()

    # Auto-focus input
    st.markdown("""
    <script>
    var input = window.parent.document.querySelector('input[type="text"]');
    if(input){input.focus();}
    </script>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()