# PyStart
This project serves as an example for a project using DevContainers

# Setup
Start by forking the project 
![](./docs/images/project-fork.png?raw=true)

Once the project is in your account, there are different ways you can set up this project. We will cover how you can set it up in [GitHub Codespaces](https://github.com/features/codespaces) and in VS Code on your local machine.

## GitHub Codespaces
You can set up this project to develop in [GitHub Codespaces](https://github.com/features/codespaces), where you can code, debug, and run your app remotely in a codespace. A codespace provides a fully configured development environment hosted in the cloud, eliminating the need for local setup. This environment includes your project's dependencies, tools, and extensions, ensuring a consistent and reproducible development experience. It streamlines collaboration by providing real-time editing, integrated version control, and easy access to debugging and testing tools, all while maintaining the security and reliability of your project.
# PyStart

This project serves as an example for working with DevContainers and includes a small command-line chatbot example that demonstrates calling the Groq API.

## Setup

Start by forking the project and opening it in your development environment (Codespaces or local VS Code).

You can develop in GitHub Codespaces or locally in VS Code. The repository includes information and images in `docs/images/` to guide Codespaces usage.

### Locally in VS Code

Requirements and recommendations:

- Python 3.11
- Use `venv` or `conda` to isolate your environment
- Recommended VS Code extensions: Python, Pylance, Black/Formatter, Ruff

Follow the DevContainer documentation if you choose to work inside a containerized dev environment.

## Running the example FastAPI app

To run the FastAPI server (if present), use:

```bash
uvicorn main:app --reload
```

## IMChatbot (Groq) — Command-line chatbot

This repository contains `main.py`, a simple CLI chatbot that calls the Groq API in a loop until you type `quit`.

Steps to run the chatbot:

1. Install dependencies:

```bash
pip3 install -r requirements.txt
```

2. Set your Groq API key (replace with your real key):

```bash
export GROQ_API_KEY="your_real_groq_key_here"
```

3. Run the chatbot:

```bash
python3 main.py
```

Usage:

- Type a question and press Enter; the app will send it to the Groq API and print the response.
- Type `quit` to exit.

If you want, add a `.env` file and export the environment variable from your shell profile for convenience.

---

File: [main.py](main.py)
