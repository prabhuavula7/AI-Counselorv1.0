import gradio as gr
from app import get_response

def chat_interface(user_input, history):
    response = get_response(user_input)
    history = history + [
        {"role": "user", "content": user_input},
        {"role": "assistant", "content": response}
    ]
    return history

chatbot_ui = gr.ChatInterface(
    fn=chat_interface,
    title="AI Counselor",
    description="Chat with an AI counselor trained to support emotional well-being.",
    theme="soft",
    chatbot=gr.Chatbot(type="messages")
)

if __name__ == "__main__":
    chatbot_ui.launch()
