# Llama 3.2 Vision UI Project

## Introduction
Welcome to the Llama 3.2 Vision UI Project, brought to you by [Kno2gether](https://www.youtube.com/@Kno2gether). This project demonstrates how to set up and use the Llama 3.2 Vision model with a simple user interface.

## Video Tutorial
For a detailed walkthrough of this project, check out our YouTube video:

[![How to Use Llama 3.2 Vision Model](https://img.youtube.com/vi/HbVOL72btlc/0.jpg)](https://www.youtube.com/watch?v=HbVOL72btlc)

## Prerequisites
- Ubuntu server
- Python 3.7 or higher
- pip (Python package installer)
- A Hugging Face account and API token

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/your-username/llama-3.2-vision-ui.git
   cd llama-3.2-vision-ui
   ```

2. Set up a virtual environment:
   ```
   python3 -m venv llama_env
   source llama_env/bin/activate
   ```

3. Install the required packages:
   ```
   pip install torch transformers accelerate bitsandbytes huggingface_hub gradio pillow requests python-dotenv
   ```

4. Create a `.env` file in the project directory and add your Hugging Face token:
   ```
   echo "HUGGINGFACE_TOKEN=your_token_here" > .env
   ```
   Replace `your_token_here` with your actual Hugging Face token.

## Usage

1. Ensure you're in the virtual environment:
   ```
   source llama_env/bin/activate
   ```

2. Run the script:
   ```
   python llama_vision_ui.py
   ```

3. Open the provided URL (usually `http://127.0.0.1:7860`) in your web browser.

4. Upload an image and enter a text prompt in the interface.

5. Click "Submit" to generate a response from the Llama 3.2 model.

## Troubleshooting

If you encounter any issues, please check the following:
- Ensure your Hugging Face token is correctly set in the `.env` file.
- Verify that you have sufficient GPU memory to run the model.
- Check your internet connection, as the script needs to download the model.

For more detailed troubleshooting, refer to the video tutorial or leave a comment on the YouTube video.

## Contributing

We welcome contributions! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.

## Acknowledgments

- Thanks to Meta for releasing the Llama 3.2 model.
- Hugging Face for providing the model hosting and APIs.
- The Gradio team for their excellent UI framework.

## IMPORTANT: FOR SOLOPRENUR

If you're looking to become a soloprenur or dream to launch your SaaS/MicroSaaS, You can checkout my new course on creating SaaS Faster using AI. The Course is designed to force you take action.
[Check details from here](https://knolabs.biz/upsell-saas-course-2139-9605)


---

Don't forget to like, subscribe, and hit the notification bell on [Kno2gether](https://www.youtube.com/@Kno2gether) for more AI and machine learning content!