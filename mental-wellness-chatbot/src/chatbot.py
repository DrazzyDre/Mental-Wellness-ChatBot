import os
import pandas as pd
import json
from src.analysis.sentiment import analyze_sentiment
from src.analysis.emotion import detect_emotion
from src.logs.session_log import SessionLogger
from src.utils.helpers import load_data, save_data, get_current_timestamp
from src.llm.response_generator import generate_response

class MentalWellnessChatbot:
    def __init__(self):
        data_path = "data/user_logs.csv"
        # Load user data from CSV, or create a new one if it doesn't exist
        if not os.path.exists(data_path):
            os.makedirs(os.path.dirname(data_path), exist_ok=True)
            pd.DataFrame(columns=["timestamp", "user_input", "response", "sentiment", "emotion"]).to_csv(data_path, index=False)
        self.user_data = load_data(data_path)
        self.session_log = []
        self.logger = SessionLogger()  # create logger instance

    def process_input(self, user_input):
        sentiment = analyze_sentiment(user_input)
        emotion = detect_emotion(user_input)
        response = generate_response(user_input) 
        self.log_user_interaction(user_input, response, sentiment, emotion)
        return response
    

    # def generate_response(self, sentiment, emotion):
    #     dominant_emotion = max(emotion, key=emotion.get) if emotion else None
    #     if sentiment['compound'] >= 0.05:
    #         if dominant_emotion == "joy":
    #             return "That's wonderful! I'm glad you're feeling joyful. Want to share more?"
    #         elif dominant_emotion == "surprise":
    #             return "Surprises can be exciting! Tell me more about it."
    #         else:
    #             return "I'm glad to hear that! How can I assist you further?"
    #     elif sentiment['compound'] <= -0.05:
    #         if dominant_emotion == "sadness":
    #             return "I'm sorry you're feeling sad. Remember, it's okay to feel this way. Would you like to talk more about it?"
    #         elif dominant_emotion == "anger":
    #             return "It sounds like you're upset. I'm here to listen if you want to vent."
    #         else:
    #             return "I'm sorry to hear that. It's okay to feel this way. I'm here to help."
    #     else:
    #         return "Thank you for sharing. How are you feeling right now?"

    def log_user_interaction(self, user_input, response, sentiment, emotion):
        log_entry = {
            'user_input': user_input,
            'response': response,
            'sentiment': sentiment,
            'emotion': emotion,
            'timestamp': self.get_current_time()
        }
        self.session_log.append(log_entry)
        self.logger.log_session(user_input, response, emotion)  # use the logger

    def get_current_time(self):
        from datetime import datetime
        return datetime.now().isoformat()
    
# Added code blocks

if __name__ == "__main__":
    print("Mental Wellness Chatbot (console mode)")
    chatbot = MentalWellnessChatbot()
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        response = chatbot.process_input(user_input)
        print("Chatbot:", response)