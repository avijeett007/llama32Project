# Update and install system dependencies
sudo apt-get update
sudo apt-get install -y python3-pip python3-venv

# Create and activate a virtual environment
python3 -m venv llama_env
source llama_env/bin/activate

# Install required packages
pip install torch transformers accelerate bitsandbytes huggingface_hub gradio pillow requests python-dotenv