import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv(""))

messages = []

def completion(message):
    global messages

    messages.append({
        "role": "user",
        "content": message
    })

    chat_completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )

    reply = chat_completion.choices[0].message.content
    print("Nova:", reply)

    messages.append({
        "role": "assistant",
        "content": reply
    })


if __name__ == "__main__":
    print("Nova is ready! (type 'exit' to quit)\n")

    while True:
        user_question = input("You: ")

        if user_question.lower() in ["exit", "quit"]:
            print("Nova: Goodbye ")
            break

        completion(user_question)