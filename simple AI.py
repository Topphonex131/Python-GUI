import time
import random
# simulated thinking delay
def think():
    print("Thinking...", end="")
    for _ in range(3):
        time.sleep(0.5)
        print(".",ends="",
              flush=True)
        print("\n")

# AI Responses
responses = {
"hello": "Hi there! how can i help you?",
"who are you,what are you":"i'm a simple python AI that is being developed by you",
"how are you":"i'm okay,though i'm just an AI built from code",
"what can you do":"i can do a lot of things i could even make code or ai for you but for that you would have to upgrade me",
"bye":"bye be sure to leve a good review,haha just joking but goodye",
"it's night":"have a good sleep and then we can do coding tommorow, bye" } 
def simple_ai():
    print("AI: enter q to quit")
    while True:
        user_input = input("you: ").lower()
        think()
        found = False
        for key in responses:
            if key in user_input:
                print(f"AI:{responses[key]}")
                found = True
                break
            if not found:
                print("AI: Hmm... looks like you haven't added this as a resonse in the code")
            if "q" in user_input:
                break      
# Run The AI
simple_ai()                