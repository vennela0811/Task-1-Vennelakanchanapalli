# The brain of the bot - 0(1) lookup, no if-elif ladder
#---Knowledge base (Hash map / Dictionary)---
responses = {
    "hello":    "Hi there! How can I help you today?",
    "hi":       "Hey! Welcome to DecodeLabs AI.",
    "hey":      "Hello! What's on your mind?",
    "how are you":  "I'm running at 100% efficiency! How about you?",
    "what is ai":   "AI is the simulation of human intelligence by machines.",
    "what can you do":  "I can answer questions, greet you, and have basic conversations!",
    "what is project 1":    "Project 1 is the foundational Rule-Based AI Chatbot focused on Control Flow and Logic.",
    "who are you":  "I'm your friendly DecodeLabs AI Chatbot, here to assist you with your Learning Journey.",
    "bye":              "Goodbye! Keep building great things.",
    "thanks":           "You're welcome! Always here to help.",
    "help":             "Try asking: hello, what is ai, how are you, bye",
    "exit":             "Shutting down... See you next time!"          
}

#---Phase 1: Sanitization---
def sanitize(raw_input):
    return raw_input.strip().lower()

#---Phase 2: Logic engine (0(1)Loopkup)---
def get_response(clean_input):
    return responses.get(clean_input, "I do not understand. Type 'help' to see what I can do.")

#---Phase 3: Heartbeat loop---
def run_chatbot():
    print("=" * 40)
    print("     DecodeLabs AI Chatbot   -   Online")
    print("     Type 'exit' to shut down")
    print("=" * 40)

    while True:
        raw = input("\nUser: ")
        clean = sanitize(raw)
        response = get_response(clean)
        print(f"Bot: {response}")
        if clean == "exit":
            break


#---Entry point---
if __name__ == "__main__":
    run_chatbot()