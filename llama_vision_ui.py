import os
from dotenv import load_dotenv
import torch
from PIL import Image
import requests
from transformers import MllamaForConditionalGeneration, AutoProcessor
from transformers import BitsAndBytesConfig
import gradio as gr
from huggingface_hub import login

# Load environment variables
load_dotenv()

# Hugging Face login
huggingface_token = os.getenv('HUGGINGFACE_TOKEN')
if not huggingface_token:
    raise ValueError("HUGGINGFACE_TOKEN not found in environment variables")

login(token=huggingface_token)

# Configure model
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16
)

model_id = "meta-llama/Llama-3.2-11B-Vision-Instruct"

# Load model and processor
model = MllamaForConditionalGeneration.from_pretrained(
    model_id,
    quantization_config=bnb_config
)
processor = AutoProcessor.from_pretrained(model_id)

def process_image_and_text(image, text_prompt):
    # Prepare input
    messages = [
        {"role": "user", "content": [
            {"type": "image"},
            {"type": "text", "text": text_prompt}
        ]}
    ]
    input_text = processor.apply_chat_template(messages, add_generation_prompt=True)
    inputs = processor(image, input_text, return_tensors="pt").to(model.device)

    # Generate output
    output = model.generate(**inputs, max_new_tokens=100)
    return processor.decode(output[0])

# Create Gradio interface
iface = gr.Interface(
    fn=process_image_and_text,
    inputs=[
        gr.Image(type="pil"),
        gr.Textbox(label="Enter your prompt")
    ],
    outputs="text",
    title="Llama 3.2 Vision Model Demo",
    description="Upload an image and enter a prompt to generate a response."
)

iface.launch()