import openai
# import gradio
import tiktoken
import os
import sys

# simple function to count token usage
def token_num(string: str, encoding_name: str) -> int:
    encoding = tiktoken.encoding_for_model(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens

try:
  openai.api_key = os.environ['OPENAI_API_KEY']
except KeyError:
  sys.stderr.write("Your OpenAI api key is not set up correctly, check Secrets tab to make sure you have set up your key correctly")
  exit(1)

messages = []
sys_msg = input("What type of chatbot would you like to create?\n")
messages.append({"role": "system", "content": f"{sys_msg} in 100 words or less"})
print("Your new assistant is ready to chat!") 

while input != "quit()":
    message = input("user input: ")
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        max_tokens=150,
        messages=messages
    )
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant"})
    reply_token_num = token_num(reply, "gpt-3.5-turbo")
    
    print("\n" + reply + "\n")
    print(f"token usage: {reply_token_num}")