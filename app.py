import gradio as gr
import os
import logging
import sys

# Setup basic logging to stdout
logging.basicConfig(
    level=logging.INFO,
    stream=sys.stdout,
    format='%(asctime)s [%(levelname)s] %(message)s'
)

# Set environment variables
os.environ["GRADIO_TEMP_DIR"] = "/tmp"
os.environ["GRADIO_FLAGGING_DIR"] = "/tmp/flagged"

# Define the function to handle inputs
def greet(name, age, agree, choice):
    logging.info(f"Function called with inputs: name={name}, age={age}, agree={agree}, choice={choice}")
    
    # Build the response based on inputs
    response = f"Hello, {name}! "
    
    if agree:
        response += f"Great to hear you're in agreement. "
    else:
        response += f"That's okay, no worries! "
    
    response += f"You're {age} years old, and you chose the option: {choice}."
    
    return response

# Log initialization
logging.info("Initializing Gradio Interface...")

# Create the Gradio interface with multiple input types
demo = gr.Interface(
    fn=greet,
    inputs=[
        gr.Textbox(label="Enter your name"),      # Text input for name
        gr.Slider(minimum=0, maximum=100, label="Select your age"),  # Slider for age
        gr.Checkbox(label="Do you agree?"),       # Checkbox for agreement
        gr.Radio(["Option 1", "Option 2", "Option 3"], label="Choose an option")  # Radio buttons
    ],
    outputs="text",
    flagging_dir=os.environ["GRADIO_FLAGGING_DIR"],
    concurrency_limit=1
)

# Launch the Gradio app
if __name__ == "__main__":
    logging.info("Launching Gradio app...")
    demo.launch(
        server_name="0.0.0.0",
        server_port=7860,
        show_error=True,
        share=False
    )
