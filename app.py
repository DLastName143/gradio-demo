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

os.environ["GRADIO_TEMP_DIR"] = "/tmp"
os.environ["GRADIO_FLAGGING_DIR"] = "/tmp/flagged"
def greet(name):
    logging.info(f"Function called with input: {name}")
    return f"Hello, {name}!"

logging.info("Initializing Gradio Interface...")

demo = gr.Interface(fn=greet, inputs="text", outputs="text", flagging_dir=os.environ["GRADIO_FLAGGING_DIR"], concurrency_limit=1)

# ✅ Ensures the app doesn't exit immediately
if __name__ == "__main__":
    logging.info("Launching Gradio app...")
    demo.launch(
        server_name="0.0.0.0",
        server_port=7860,
        show_error=True,
        share=False

    )