
def chatbot(user_input):
    user_input = user_input.lower()  # Convert input to lowercase for case-insensitive matching

    if "hi" in user_input or "hello" in user_input:
        print("Chatbot: Hi!")
    elif "how are you" in user_input:
        print("Chatbot: I'm fine, thanks!")
    elif "bye" in user_input:
        print("Chatbot: Goodbye!")
    else:
        print("Chatbot: I don't understand this phrase. Can you repeat?")

def main():
    while True:
        user_input = input("User: ")
        if "bye" in user_input.lower():
            chatbot(user_input)
            break
        chatbot(user_input)

if __name__ == "__main__":
    main()
