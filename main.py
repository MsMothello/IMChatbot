
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv('GROQ_API_KEY'))

while True:
    answer = input("User prompt: ")
    
    if answer == 'quit':
        break
    
    print(answer)

    completion = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
      {
        "role": "user",
        "content": answer
      }
    ],
    temperature=1,
    max_completion_tokens=8192,
    top_p=1,
    reasoning_effort="medium",
    stream=False,
    stop=None
)

#for chunk in completion:
#   print(chunk.choices[0].delta.content or "", end="")
    
    print(completion.choices[0].message.content)