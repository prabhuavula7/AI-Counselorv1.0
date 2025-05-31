import re
from config import CRISIS_PATTERNS

#Detect if the input text indicates a crisis situation
def detect_crisis(text, lang="en"):
    text = text.lower()

    # ollect both native and romanized patterns
    patterns = CRISIS_PATTERNS.get(lang, []) + CRISIS_PATTERNS.get(f"{lang}-romanized", [])

    #Check if any pattern matches
    return any(re.search(p, text) for p in patterns)
