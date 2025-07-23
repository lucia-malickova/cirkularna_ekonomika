import gradio as gr
import os
from openai import OpenAI
from dotenv import load_dotenv

# 🔒 Load API key from .env file
load_dotenv()
client = OpenAI(api_key=os.getenv("GROQ_API_KEY"), base_url="https://api.groq.com/openai/v1")

# 💬 Main function to answer user questions
def circular_advisor(question):
    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {
                "role": "system",
                "content": "You are an expert in circular and sharing economy, specializing in small businesses in hospitality and tourism. Respond clearly, practically, and in English."
            },
            {"role": "user", "content": question}
        ]
    )
    return response.choices[0].message.content.strip()

# 🎛️ Gradio interface
demo = gr.Interface(
    fn=circular_advisor,
    inputs=gr.Textbox(lines=2, placeholder="Ask a question, e.g. How can a small hotel reduce single-use plastics?"),
    outputs="text",
    title="Circular Advisor",
    description="An advisor for small businesses in sustainability, circular economy, and the sharing economy."
)

# ▶️ Launch the app
demo.launch()
