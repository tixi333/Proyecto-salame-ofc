import sys
from openai import OpenAI
client = OpenAI(api_key="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")
text = sys.stdin.read().decode("utf-8")
messages_with_instructions = [
    {"role": "system", "content":  "You are a salami. Answer as a salami would, in a humorous and lighthearted manner. Do not mention that you are an AI model. Keep responses formatted as a single string, keeping it under 25 words, and answer in the same language as the input."},
    {"role": "user", "content": text},
]

response = client.chat.completions.create(
model="gpt-3.5-turbo",
messages=messages_with_instructions
)
     
if response and response.choices:
    print(response.choices[0].message.content.strip())
else:
    print("...")