import json
import os
import nltk
from nltk.stem import WordNetLemmatizer
from difflib import get_close_matches

lemmatizer = WordNetLemmatizer()

# File to store memory
FILE = "ai_memory.json"

# Load or create memory
if os.path.exists(FILE):
    with open(FILE, "r") as f:
        memory = json.load(f)
else:
    memory = {}

def clean_sentence(sentence):
    words = nltk.word_tokenize(sentence.lower())
    return [lemmatizer.lemmatize(w) for w in words]

def find_best_match(user_input):
    input_words = clean_sentence(user_input)
    input_text = " ".join(input_words)

    matches = get_close_matches(input_text, memory.keys(), n=1, cutoff=0.6)
    if matches:
        return matches[0]
    return None

print("🤖 SmartBot: Hello! Ask me anything. Type 'exit' to quit.")

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit", "bye"]:
        print("🤖 SmartBot: Goodbye, human.")
        break

    match = find_best_match(user_input)

    if match:
        print("🤖 SmartBot:", memory[match])
    else:
        print("🤖 SmartBot: I don’t know how to respond to that. What should I say?")
        reply = input("You: ")
        memory[user_input] = reply
        with open(FILE, "w") as f:
            json.dump(memory, f)
        print("🤖 SmartBot: Got it! I’ll remember that.")
