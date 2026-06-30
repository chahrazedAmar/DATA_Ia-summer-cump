from groq import Groq


from dotenv import load_dotenv 

import os
load_dotenv()  # Load environment variables from .env file

with open('context.txt', 'r') as f:
    context = f.read()  # Read the content of context.txt into a variable

    with open('remarques.txt' , 'r') as f:
        remarques = f.read()  # Read the content of instruction.txt into a variable
#cle API creer sur le site groq.ai

API_KEY = os.getenv("API_KEY")  #  your actual API key
client = Groq(api_key=API_KEY) #notre variable client est notre instance de l'API Groq, qui nous permet d'interagir avec le modèle de langage.

chat_completion = client.chat.completions.create(
    messages=[
        # Set an optional system message. This sets the behavior of the
        # assistant and can be used to provide specific instructions for
        # how it should behave throughout the conversation.
        {
            "role": "system",  # personnalité
            "content": context,
        },
        # Set a user message for the assistant to respond to.
        {
            "role": "user",#utilisateur
            "content": remarques,
        }
    ],

    # The language model which will generate the completion.

    model="llama-3.3-70b-versatile"
)

# Print the completion returned by the LLM.
print(chat_completion.choices[0].message.content)