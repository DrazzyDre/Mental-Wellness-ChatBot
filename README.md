# Mental Wellness Chatbot

## Project Overview
The Mental Wellness Chatbot is designed to provide users with a supportive conversational interface that promotes mental well-being. The chatbot utilizes sentiment and emotion analysis to understand user inputs and generate empathetic responses. Additionally, it offers emotional trend visualization and maintains user session logs for tracking emotional states over time.

## Features
- **Conversational Interface**: Engaging user interface for seamless interaction.
- **Sentiment Analysis**: Assess user sentiment using advanced NLP techniques.
- **Emotion Detection**: Identify and classify user emotions to tailor responses.
- **Emotional Trend Visualization**: Graphical representation of emotional trends over time.
- **User Session Logs**: Maintain logs of user interactions for review and analysis.

## Project Structure
```
mental-wellness-chatbot
├── src
│   ├── chatbot.py          # Main logic for the chatbot
│   ├── interface
│   │   └── ui.py          # User interface definition
│   ├── analysis
│   │   ├── sentiment.py    # Sentiment analysis functions
│   │   └── emotion.py      # Emotion detection functions
│   ├── visualization
│   │   └── trends.py       # Emotional trends visualization
│   ├── logs
│   │   └── session_log.py   # User session logging
│   └── utils
│       └── helpers.py      # Utility functions
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation
```

## Setup Instructions
1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd mental-wellness-chatbot
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run the chatbot:
   ```
   python src/chatbot.py
   ```

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
