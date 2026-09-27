# Rule-Based AI Chatbot

responses = {
    "hello": "Hi there! How can I help you?",
    "hi": "Hello! How can I assist you today?",
    "hey": "Hey! What can I do for you?",
    "how are you": "I'm doing well, thank you for asking!",
    "how do you do": "I'm doing great! Thanks for asking!",
    "what is your name": "I'm RuleBot, a simple rule-based chatbot.",
    "who are you": "I am RuleBot, here to help you with basic queries.",
    "help": "I can answer simple questions like greetings, how I am, or my name. Just type your query!",
    "what can you do": "I can respond to greetings, answer questions about myself, and help with basic queries.",
    "bye": "Goodbye! It was nice talking to you!",
    "goodbye": "Goodbye! Have a great day!",
    "see you": "See you later! Take care!",
    "thank you": "You're welcome! Happy to help!",
    "thanks": "No problem! Anything else?",
    "what is python": "Python is a high-level programming language known for its simplicity and readability.",
    "who created python": "Python was created by Guido van Rossum and first released in 1991.",
    "what is ai": "AI stands for Artificial Intelligence - the simulation of human intelligence by machines.",
    "what is machine learning": "Machine Learning is a subset of AI that enables systems to learn from data.",
    "tell me a joke": "Why do programmers prefer dark mode? Because light attracts bugs!",
    "joke": "What do you call a fake noodle? An impasta! Ha ha!",
    "what time is it": "I'm just a simple rule-based chatbot, I don't have access to real-time info.",
    "date": "I don't have access to the current date. Check your system clock!",
    "weather": "I don't have access to real-time weather data."
}

def chatbot():
    """Main chatbot function with continuous loop."""
    
    print("====================================")
    print("     RULE-BASED AI CHATBOT")
    print("====================================")
    print("Bot: Hello! How can I help you?")
    print("Bot: Type 'exit' to quit.\n")

    
    while True:
        # Get user input and sanitize
        user_input = input("You: ").lower().strip()

        if user_input == "exit":
            print("Bot: Goodbye!")
            break

     
        if not user_input:
            print("Bot: I didn't catch that. Could you please repeat?")
            continue

        reply = responses.get(user_input, "I'm sorry, I don't understand that. Try asking about greetings, help, or type 'exit' to quit.")

        
        print(f"Bot: {reply}")

if __name__ == "__main__":
    chatbot()