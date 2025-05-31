import torch
import numpy as np
import regex as re 
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from langdetect import detect_langs, DetectorFactory
from config import SENTIMENT_MODEL_NAME

DetectorFactory.seed = 0

#Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(SENTIMENT_MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(SENTIMENT_MODEL_NAME)
model.eval()

#Device setup
device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
model.to(device)

# Language and Script detection functions

def detect_language(text: str) -> str:
    try:
        lang_probs = detect_langs(text)
        top = lang_probs[0]
        return top.lang if top.prob > 0.7 else "en"
    except Exception:
        return "en"

def detect_script(text: str) -> str:
    """
    Detect if the text is in Latin script (romanized) or native script.
    """
    try:
        non_latin = re.search(r'\p{IsDevanagari}|\p{IsArabic}|\p{IsCyrillic}|\p{IsHebrew}|\p{IsHangul}|\p{IsHiragana}|\p{IsThai}|\p{IsTelugu}|\p{IsTamil}|\p{IsMalayalam}', text)
        return "native" if non_latin else "romanized"
    except:
        return "romanized"

# Classifying sentiment and mapping to emotions

def classify_sentiment(text: str):
    inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True)
    inputs = {k: v.to(device) for k, v in inputs.items()}
    with torch.no_grad():
        outputs = model(**inputs)
    scores = torch.nn.functional.softmax(outputs.logits, dim=1).cpu().numpy()[0]
    return int(np.argmax(scores)), float(np.max(scores))

def map_sentiment_and_emotion(score_idx: int, confidence: float):
    sentiment_labels = ["very negative", "negative", "neutral", "positive", "very positive"]
    emotion_map = {
        0: "hopelessness/despair",
        1: "sadness/frustration",
        2: "indifferent/flat",
        3: "hope/contentment",
        4: "joy/excitement"
    }
    return sentiment_labels[score_idx], emotion_map[score_idx]

# Analysis function

def analyze_input(text: str, debug: bool = False) -> dict:
    language = detect_language(text)
    script = detect_script(text)
    score_idx, confidence = classify_sentiment(text)
    sentiment, emotion = map_sentiment_and_emotion(score_idx, confidence)

    result = {
        "language": language,
        "script": script,  # <-- added field
        "sentiment": sentiment,
        "sentiment_score": round(confidence, 4),
        "emotion": emotion
    }

    if debug:
        print("[Sentiment Debug]", result)

    return result
