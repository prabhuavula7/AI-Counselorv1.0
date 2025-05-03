from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
from transformers import AutoModelForCausalLM
import torch

#Device setup
device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")

#BERT sentiment model
sentiment_tokenizer = AutoTokenizer.from_pretrained("nlptown/bert-base-multilingual-uncased-sentiment")
sentiment_model = AutoModelForSequenceClassification.from_pretrained("nlptown/bert-base-multilingual-uncased-sentiment").to(device)
sentiment_pipeline = pipeline("sentiment-analysis", model=sentiment_model, tokenizer=sentiment_tokenizer, device=0 if device.type != "cpu" else -1)

#lightweight LLM for response generation
response_model_name = "EleutherAI/gpt-neo-125M"
response_tokenizer = AutoTokenizer.from_pretrained(response_model_name)
response_model = AutoModelForCausalLM.from_pretrained(response_model_name).to(device)

def get_response(user_input):
    #Sentiment Analysis
    print("Running BERT sentiment analysis...")
    sentiment = sentiment_pipeline(user_input)[0]
    label = sentiment['label']
    print(f"Sentiment: {label}")

    #Prompt formatting based on sentiment
    if "1" in label or "2" in label:
        prompt = f"The user is feeling low. Respond with kindness: {user_input}"
    elif "4" in label or "5" in label:
        prompt = f"The user is cheerful. Respond supportively: {user_input}"
    else:
        prompt = f"Respond thoughtfully: {user_input}"

    #Generate response
    print("Generating response...")
    inputs = response_tokenizer(prompt, return_tensors="pt").to(device)
    output = response_model.generate(
        **inputs,
        max_length=150,
        do_sample=True,
        top_p=0.95,
        temperature=0.7,
        pad_token_id=response_tokenizer.eos_token_id
    )

    response = response_tokenizer.decode(output[0], skip_special_tokens=True)
    response = response.replace(prompt, "").strip()
    print("Response generated.")
    return response or "I'm here to help. Tell me more about how you're feeling."
