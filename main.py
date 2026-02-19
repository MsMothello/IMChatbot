
import os

api_key = os.environ.get("GROQ_API_KEY")
if not api_key:
  raise RuntimeError("Please set the GROQ_API_KEY environment variable")

_client = None
def get_client():
  global _client
  if _client is not None:
    return _client
  try:
    import importlib
    groq = importlib.import_module("groq")
    Groq = getattr(groq, "Groq")
  except Exception:
    raise RuntimeError("Missing required package 'groq'. Install dependencies with: pip3 install -r requirements.txt")
  _client = Groq(api_key=api_key)
  return _client

def ask_groq(prompt: str) -> str:
  client = get_client()
  completion = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[{"role": "user", "content": prompt}],
    temperature=1,
    max_completion_tokens=8192,
    top_p=1,
    reasoning_effort="medium",
    stream=False,
    stop=None,
  )
  # Safely extract content from the response
  try:
    return completion.choices[0].message.content
  except Exception:
    try:
      return str(completion)
    except Exception:
      return "(no response)"


def main():
  while True:
    try:
      answer = input("What do you want? ")
    except (EOFError, KeyboardInterrupt):
      print("\nExiting.")
      break

    if answer is None:
      continue

    answer = answer.strip()
    if not answer:
      # ignore empty input and prompt again
      continue

    if answer.lower() == "quit":
      break

    try:
      response = ask_groq(answer)
      print(response, flush=True)
    except Exception as e:
      print("Error calling Groq API:", e)


if __name__ == "__main__":
  main()