# Used to select random responses
import random 
# Used to show current time
from datetime import datetime 

# Main chatbot function
def chatbot():
    print(" SmartBot: Hello! What's your name?")
    
    name = input("You: ")  # Take user's name

    # List of random greeting responses
    greetings = ["Hello!", "Hi there!", f"Hey {name}! "]
    
    # List of random mood responses
    moods = ["I'm great!", "Doing awesome!", "All good "]

    while True:
        user = input(f"{name}: ").lower()  # User input in lowercase

        # Greeting condition
        if "hi" in user or "hello" in user:
            print("Bot:", random.choice(greetings))  # Random greeting

        # Asking how bot is
        elif "how are you" in user:
            print("Bot:", random.choice(moods))  # Random mood reply

        # Show current time
        elif "time" in user:
            print("Bot:", datetime.now().strftime("%H:%M:%S"))

        # Tell a joke
        elif "joke" in user:
            print("Bot: Why do Python programmers prefer dark mode? Because light attracts bugs 😄")

        # Recall user's name
        elif "my name" in user:
            print(f"Bot: Your name is {name} ")

        # Exit chatbot
        elif "bye" in user:
            print(f"Bot: Goodbye {name}! ")
            break

        # Default response
        else:
            print("Bot: Hmm... I’m still learning ")

# Run the chatbot
chatbot()