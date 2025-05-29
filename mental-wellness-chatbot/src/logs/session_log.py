import os
import json
from datetime import datetime

class SessionLogger:
    def __init__(self, log_file='session_log.json'):
        self.log_file = log_file
        self.ensure_log_file_exists()

    def ensure_log_file_exists(self):
        if not os.path.isfile(self.log_file):
            with open(self.log_file, 'w') as f:
                json.dump([], f)

    def log_session(self, user_input, response, emotions):
        timestamp = datetime.now().isoformat()
        session_entry = {
            'timestamp': timestamp,
            'user_input': user_input,
            'response': response,
            'emotions': emotions
        }
        self.append_to_log(session_entry)

    def append_to_log(self, session_entry):
        with open(self.log_file, 'r+') as f:
            logs = json.load(f)
            logs.append(session_entry)
            f.seek(0)
            json.dump(logs, f, indent=4)

    def get_logs(self):
        with open(self.log_file, 'r') as f:
            return json.load(f)