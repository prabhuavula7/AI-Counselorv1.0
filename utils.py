import json
from datetime import datetime

#Clean and normalize user input text
def clean_input(text: str) -> str:
    return text.strip()

#Log chat interactions to a JSONL file
def log_chat(input_text, analysis, response, file="chatlog.jsonl", use_utc=False, pretty=False):
    entry = {
        "timestamp": datetime.utcnow().isoformat() if use_utc else datetime.now().isoformat(),
        "language": analysis.get("language", "unknown"),
        "input": input_text,
        "analysis": analysis,
        "response": response
    }
    try:
        with open(file, "a", encoding="utf-8") as f:
            if pretty:
                f.write(json.dumps(entry, indent=2, ensure_ascii=False) + "\n")
            else:
                f.write(json.dumps(entry, ensure_ascii=False) + "\n")
    except Exception as e:
        print(f"⚠️ Logging failed: {e}")
