import requests
import json
from config import OLLAMA_API_URL, OLLAMA_MODEL_NAME

# Generate a response from the LLM based on user input and analysis results
def generate_llm_response(user_input, analysis, context=""):
    if analysis["is_crisis"]:
        return (
            "⚠️ It sounds like you're going through immense pain right now. "
            "You're not alone — please talk to someone you trust or reach out for help: "
            "📞 988 (US) or text HOME to 741741. You matter 🫂."
        )

    # examples to guide romanized and multilingual responses
    examples = """
### Few-Shot Examples

User (Hindi, romanized): mujhe lagta hai sab kuch bekaar hai
AI: Tum akela mehsoos kar rahe ho shayad. Main yahaan hoon sunne ke liye 🫂. Thoda sa break lena kabhi kabhi zaroori hota hai 🌱.

User (Telugu, romanized): naa gunde baadha tho undhi
AI: Oh, adi chala kashtam anipistondi. Nee feelings valid ani nenu cheptunna. Nuvvu matladadam start chesinav ante adi chala pedda vishayam 😊.

User (Spanish, romanized): no tengo ganas de hacer nada
AI: Lo siento que te sientas así 😔. A veces descansar también es importante. Estoy aquí para escucharte 🌱.

User (French, romanized): j’ai besoin d’aide mais je sais pas à qui parler
AI: C’est courageux de l’exprimer. On peut traverser ça ensemble 🧠.

User (Turkish, romanized): hayattan bıktım
AI: Bu duygular çok ağır olabilir. Ama yalnız değilsin, birlikte buradayız 🫂.

User (Urdu, romanized): main thak gaya hoon zindagi se
AI: Zindagi kabhi kabhi bohot bhaari lagti hai. Thoda araam lena bhi zaroori hai 🌱.

User (Gujarati, romanized): mane khub dukhi lage che
AI: Hu tarat madad mate aavish. Taro dukh samjay che, ane tu eklo nathi 🌱.

User (Malayalam, romanized): enikku oru baadha undu
AI: Njan ithu manassilakkunnu. Ningal thaniyalla, njan ivide undu sahayikkunnathinayi 🫂.
"""

    # instructing the model
    instructions = f"""
### Instructions

You are a warm, empathetic AI counselor 🧠.

Respond in the **same language** and **same script** (romanized or native) as the user's input. Match both the language (e.g., Hindi) and the style (e.g., Roman script or Devanagari).

Use gentle, emotionally intelligent language. Include appropriate emojis (😊🌱🫂) to express warmth and support.

If unsure of the user’s script or language, reply in soft, clear English.

Never mention you're an AI unless asked.

Be culturally sensitive, emotionally validating, and avoid robotic phrasing.

Keep replies to 3–6 lines, breaking long sentences for readability.

If signs of distress are detected (already handled), gently encourage help-seeking but don’t diagnose.

Script Detected: {analysis['script']}
"""

    prompt = f"""{instructions}

### Sentiment & Emotion
Sentiment: {analysis['sentiment']} ({analysis['sentiment_score']:.2f})
Emotion: {analysis['emotion']}
Language: {analysis['language']}
Script: {analysis['script']}

### Context from Uploaded Files
{context or 'No additional context provided.'}

{examples}

### Conversation
User: {user_input}
AI:"""

    payload = {
        "model": OLLAMA_MODEL_NAME,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.7,
            "num_predict": 300
        }
    }

    try:
        res = requests.post(OLLAMA_API_URL, headers={"Content-Type": "application/json"}, data=json.dumps(payload))
        res.raise_for_status()
        reply = res.json().get("response", "No response.")
        return reply.strip().removeprefix("AI:").strip()
    except requests.exceptions.ConnectionError:
        return "❌ Ollama server is not running. Start it with: `ollama run mistral`"
    except Exception as e:
        return f"⚠️ LLM Error: {e}"
