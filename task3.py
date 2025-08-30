import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    ["hi|hello", ["Hello!", "Hi there!"]],
    ["how are you?", ["I'm good, thanks!", "Doing great!"]],
    ["what is your name?", ["I am a Python Chatbot."]],
    ["quit", ["Bye! Take care."]]
]

print("Chatbot is ready! Type 'quit' to exit.")
chat = Chat(pairs, reflections)
chat.converse()