import openai
import os
import sys
  
try:
  openai.api_key = os.environ['OPENAI_API_KEY']
except KeyError:
  sys.stderr.write("Your OpenAI api key is not set up correctly, check Secrets tab to make sure you have set up your key correctly")
  exit(1)

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "user", "content": "Who won the world cup in 2018"}
    ]
)

print(response['choices'][0]['message']['content'])