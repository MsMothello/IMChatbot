
import os
from groq import Groq

client = Groq(api_key=os.getenv('GROQ_API_KEY'))

# Keep conversation history
messages = []

while True:
    answer = input("User prompt: ")
    
    if answer == 'quit':
        break
    
    # Add user message to history
    messages.append({
        "role": "user",
        "content": answer
    })

    completion = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful AI assistant."
            }
        ] + messages,
        temperature=1,
        max_completion_tokens=8192,
        top_p=1,
        reasoning_effort="medium",
        stream=False,
        stop=None
    )
    
    # Add assistant response to history
    response = completion.choices[0].message.content
    messages.append({
        "role": "assistant",
        "content": response
    })
    
    print(f"Assistant: {response}")
