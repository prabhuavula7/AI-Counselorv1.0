# 🌱 Sana – Your Empathetic AI Counselor

*Sana* (from *Sanare*, Latin for “to heal”) is a privacy-respecting, multilingual AI chatbot built for safe, emotionally aware mental health support. It detects language, sentiment, and emotional tone, and responds in a matching script and tone using localized examples.

---

## ✨ Features

- 💬 Emotionally intelligent replies (with emojis 🌱🫂)
- 🌐 Multilingual + romanized input support
- 🧠 Sentiment & emotion detection (using multilingual BERT)
- 🚨 Crisis pattern detection in 30+ languages
- 📂 File-powered contextual responses using RAG (Qdrant + Sentence Transformers)
- 🌓 Light/Dark mode toggle

---

## 🛠 Tech Stack

- **Frontend**: Gradio + custom CSS
- **LLM**: Mistral via Ollama. Feel free to use your own model or APIs
- **Sentiment**: `nlptown/bert-base-multilingual-uncased-sentiment`
- **Embeddings**: `all-MiniLM-L6-v2`
- **Vector DB**: Qdrant
- **Language Detection**: `langdetect` + script heuristic

---

## 🚀 Running the App

```bash
# Install dependencies
pip install -r requirements.txt

# Start services
docker run -p 6333:6333 -v qdrant_data:/qdrant/storage qdrant/qdrant
ollama run mistral

# Launch the app
python main.py
```

---

## 📁 Project Structure

```
├── main.py             # Gradio frontend + core loop
├── llm.py              # Prompt assembly and LLM query
├── sentiment.py        # Language + emotion analysis
├── crisis.py           # Crisis keyword matching
├── rag.py              # Embedding + Qdrant context retrieval
├── config.py           # Centralized config + patterns
├── utils.py            # Input cleaner + logger
├── chatlog.jsonl       # Optional chat log
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🧪 Example Inputs

- **Hindi (romanized)**: `mujhe lagta hai sab kuch bekaar hai`
- **Telugu (romanized)**: `naa manasu baadha tho undhi`
- **Urdu (romanized)**: `main thak gaya hoon zindagi se`
- **Spanish (romanized)**: `ya no puedo más`
- **English**: `I can't do this anymore`
- **German**: `ich kann nicht mehr`

---

## 👤 Author

Built with ❤️ by [Prabhu Kiran Avula](https://github.com/prabhuavula7)  
For feedback, suggestions, or collaborations — feel free to reach out!