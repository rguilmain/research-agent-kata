import gradio as gr
from .config import settings


def main():
    demo = gr.load_chat(
        "https://api.perplexity.ai",
        model="sonar-pro",
        token=settings.perplexity_api_key,
    )
    demo.launch()


if __name__ == "__main__":
    main()
