def load_data(file_path):
    import pandas as pd
    return pd.read_csv(file_path)

def save_data(data, file_path):
    import pandas as pd
    data.to_csv(file_path, index=False)

def get_current_timestamp():
    from datetime import datetime
    return datetime.now().isoformat()

def format_date(date):
    return date.strftime("%Y-%m-%d")

def calculate_average_emotion(emotion_list):
    if not emotion_list:
        return None
    return sum(emotion_list) / len(emotion_list)