import openai
import os

openai.api_key = "OpenAI_API_Key goes here"

class virtualAssisstant:
    def __init__(self):
        pass

    def chat_with_gpt(self, prompt):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
        )
        return response['choices'][0]['message']['content'].strip()
    
    def get_response(self, user_input):
        return self.chat_with_gpt(user_input)


def chat():
    print("Welcome to Hamza Virtual Assistant!")
    print("To Exit, type 'exit' \n")

    myChatbot = virtualAssisstant()
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Thank you for using Hamza Virtual Assistant, Goodbye!")
            break
        response = myChatbot.get_response(user_input)
        print("Chatbot: ", response)

if __name__ == "__main__":
    chat()

