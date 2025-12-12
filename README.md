# Perplexity Chat Interface

This project demonstrates Gradio's OpenAI API chat compatible `load_chat()` interface with Perplexity's Sonar Pro model. Settings use an extensible config module.

## Prerequisites

- Python 3.12 or higher
- [uv](https://docs.astral.sh/uv/) package manager
- Perplexity AI API key

## Installation

1. Clone the repository:

```bash
git clone git@github.com:rguilmain/research-agent-kata.git
cd research-agent-kata
```

2. Create a `.env` file with your Perplexity API key:

```bash
PERPLEXITY_API_KEY=your_api_key_here
```

3. Install dependencies using uv:

```bash
uv sync
```

## Running the Application

Start the chat interface:

```bash
uv run research-agent-kata
```

The application will launch a web interface in your default browser where you can interact with Perplexity AI.
