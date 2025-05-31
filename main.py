import gradio as gr
from sentiment import analyze_input
from crisis import detect_crisis
from llm import generate_llm_response
from rag import ensure_collection, embed_documents, retrieve_context
from utils import clean_input, log_chat
from config import LOG_FILE

# Ensure the Qdrant collection exists before starting
ensure_collection()
chat_history = []

theme_mode = {"dark": False}  # mutable theme toggle state

# Main chat function
def chat(user_input, files, progress=gr.Progress(track_tqdm=True)):
    if not user_input.strip():
        yield chat_history, gr.update(value="")
        return

    chat_history.append((user_input, "🧠 Typing..."))
    yield chat_history, ""

    cleaned_input = clean_input(user_input)
    progress(0.1, desc="Analyzing sentiment...")
    analysis = analyze_input(cleaned_input)
    analysis["is_crisis"] = detect_crisis(cleaned_input, lang=analysis["language"])

    context = ""
    if files:
        progress(0.3, desc="Retrieving context...")
        context = retrieve_context(cleaned_input)

    progress(0.6, desc="Generating response...")
    response = generate_llm_response(cleaned_input, analysis, context)

    log_chat(user_input, analysis, response, LOG_FILE)

    chat_history[-1] = (user_input, response)
    progress(1.0)
    yield chat_history, ""

def upload_files(file_list):
    if not file_list:
        return "No files selected."
    try:
        file_paths = [f.name for f in file_list]
        embed_documents(file_paths)
        return f"✅ {len(file_paths)} file(s) embedded."
    except Exception as e:
        return f"❌ Error embedding files: {e}"

# Create the Gradio app 

with gr.Blocks(
    css="""
    body.light { background-color: #f8f5e2; color: #222; }
    body.dark { background-color: #0f0f0f; color: #eee; }
    .chat-entry { border-radius: 12px; padding: 8px 14px; margin: 5px 0; }
    .user-msg { background: #d8f0ff; align-self: flex-end; }
    .bot-msg { background: #fff3cc; align-self: flex-start; }
    #theme-switcher { display: flex; justify-content: flex-end; padding: 0 20px; }
    #dark-toggle { appearance: none; width: 50px; height: 26px; background: #ccc; border-radius: 13px; position: relative; cursor: pointer; }
    #dark-toggle:checked { background: #333; }
    #dark-toggle::before {
        content: ""; width: 22px; height: 22px; border-radius: 50%;
        background: white; position: absolute; top: 2px; left: 2px;
        transition: 0.3s;
    }
    #dark-toggle:checked::before { transform: translateX(24px); }
    """,
    theme=gr.themes.Soft(primary_hue="orange" if not theme_mode["dark"] else "gray")
) as app:

    gr.HTML("""
    <div id='theme-switcher'>
        <label>
            <input type='checkbox' id='dark-toggle' onchange='document.body.classList.toggle("dark"); document.body.classList.toggle("light")'>
        </label>
    </div>
    """)

    gr.Markdown("<h1 style='text-align:center;'>🌱 Sana - Your Empathetic AI</h1><p style='text-align:center;'>Safe, multilingual mental health support with file-powered context</p>")

    with gr.Row():
        with gr.Column(scale=4):
            chatbox = gr.Chatbot(label="Chat", height=500)
        with gr.Column(scale=1):
            with gr.Accordion("📂 Upload Files", open=False):
                file_input = gr.File(file_types=[".txt", ".pdf", ".md"], file_count="multiple")
                file_status = gr.Markdown("No files uploaded.")
            gr.Markdown("""
            ### 🔗 Resources
            - [988 Lifeline](https://988lifeline.org)
            - [Find Therapists](https://www.psychologytoday.com/)
            - [ASAN](https://autisticadvocacy.org/)
            - [CHADD](https://www.chadd.org/)
            - [NAD](https://www.nad.org/)
            """)
            gr.Button("💬 Talk to a Counselor", link="https://988lifeline.org")

    with gr.Row():
        user_input = gr.Textbox(label="Type your message...", scale=4)
        send_btn = gr.Button("Send", scale=1)

    user_input.submit(chat, inputs=[user_input, file_input], outputs=[chatbox, user_input])
    send_btn.click(chat, inputs=[user_input, file_input], outputs=[chatbox, user_input])
    file_input.change(upload_files, inputs=[file_input], outputs=[file_status])

    gr.Markdown("<p style='text-align:center;'>Built with 💛 | Privacy-respecting local AI</p>")

app.queue().launch()
