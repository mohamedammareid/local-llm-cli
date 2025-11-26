# 🤖 Local LLM Chatbot

A professional, terminal-based chat interface for local Large Language Models (LLMs), built with **Python**, **LangChain**, and **Ollama**.

## ✨ Features

-   **Local Privacy**: Runs entirely on your machine using Ollama.
-   **Streaming Responses**: Real-time text generation for a smooth chat experience.
-   **Customizable Personas**: Set the system prompt to change the bot's behavior.
-   **Model Switching**: Easily switch between installed Ollama models via CLI.
-   **Memory Management**: Sliding window context to prevent memory overflows.

## 🚀 Prerequisites

1.  **Python 3.8+** installed.
2.  **[Ollama](https://ollama.com/)** installed and running.

## 📦 Installation

1.  Clone this repository or download the files.
2.  Install the required Python packages:

```bash
pip install -r requirements.txt
```

3.  Ensure you have a model pulled in Ollama (default is `gpt-oss:20b`, but you can use others):

```bash
ollama pull gpt-oss:20b
# OR for a smaller/faster model:
ollama pull qwen2.5-coder:1.5b
```

## 🎮 Usage

Start the chatbot with the default settings:

```bash
python main.py
```

### Command Line Options

You can customize the bot's behavior using arguments:

| Argument | Description | Default |
| :--- | :--- | :--- |
| `--model` | The Ollama model to use. | `gpt-oss:20b` |
| `--system` | The system prompt (persona). | "You are a helpful AI..." |
| `--history-limit` | Number of message pairs to remember. | `10` |

### Examples

**Use a different model:**
```bash
python main.py --model llama3
```

**Set a custom persona (e.g., a coding expert):**
```bash
python main.py --system "You are a senior Python engineer. Answer concisely."
```

**Increase memory context:**
```bash
python main.py --history-limit 20
```

## 🛠️ Troubleshooting

-   **Connection Refused**: Make sure Ollama is running (`ollama serve`).
-   **Model Not Found**: Run `ollama list` to see installed models and use the exact name with `--model`.
