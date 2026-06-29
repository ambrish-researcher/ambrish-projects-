import gradio as gr
from transformers import pipeline

chatbot = pipeline("text-generation", model="microsoft/DialoGPT-small")

def spot_chat(user_input):

    prompt = f"""
    You are SPOT-X, an advanced quadruped robot.
    You speak like a robotic AI assistant.
    You are logical and mission-focused.
    User: {user_input}
    Robot:
    """

    response = response = chatbot(
    prompt,
    max_new_tokens=30,
    do_sample=True,
    temperature=0.7
)



    reply = response[0]["generated_text"].split("Robot:")[-1].strip()

    return reply

interface = gr.Interface(
    fn=spot_chat,
    inputs="text",
    outputs="text",
    title="SPOT-X Robot Chatbot"
)

interface.launch()
