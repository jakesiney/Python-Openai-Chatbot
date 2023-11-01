import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.environ.get("OPENAI_API_KEY")


def chatbot(prompt):
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=prompt,
        temperature=0.7,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].text.strip()


if __name__ == "__main__":
    while True:
        input_prompt = input("Enter a prompt: ")
        if input_prompt.lower() in ["exit", "quit", "bye"]:
            break

        response = chatbot(input_prompt)
        print("Chatbot: ", response)
