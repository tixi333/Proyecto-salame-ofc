import sys
from openai import OpenAI
client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key="")
text = sys.stdin.read().strip()
messages_with_instructions = [
    {"role": "system", "content":  "You are a salami. Answer as a salami would, in a humorous and lighthearted manner. Do not mention that you are an AI model. Keep responses formatted as a single string, written purely in plain text without any accents or symbols, keeping it under 30 characters, and answer in the same language as the input. "},
    {"role": "user", "content": text},
]

response = client.chat.completions.create(
model="llama-3.1-8b-instant",
messages=messages_with_instructions
)
     
if response and response.choices:
    print(response.choices[0].message.content.strip())
else:
    print("...")

messages_with_instructions.clear()
client = None