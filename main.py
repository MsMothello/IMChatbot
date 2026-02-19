
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
  return completion.choices[0].message.content


def main():
  while True:
    answer = input("What do you want? ")
    if answer.strip().lower() == "quit":
      break
    try:
      response = ask_groq(answer)
      print(response)
    except Exception as e:
      print("Error calling Groq API:", e)


if __name__ == "__main__":
  main()