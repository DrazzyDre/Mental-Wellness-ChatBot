from transformers import pipeline


# ----------------

# Move pipeline creation outside the function for efficiency
emotion_classifier = pipeline("text-classification", model="bhadresh-savani/roberta-base-emotion", top_k=1)

def detect_emotion(text):
    results = emotion_classifier(text)
    # results is a list of lists when top_k=1, so flatten it
    if isinstance(results[0], list):
        results = results[0]
    emotions = {result['label']: result['score'] for result in results}
    return emotions


def get_dominant_emotion(emotions):
    return max(emotions, key=emotions.get) if emotions else None

def analyze_emotion(text):
    emotions = detect_emotion(text)
    dominant_emotion = get_dominant_emotion(emotions)
    return dominant_emotion, emotions