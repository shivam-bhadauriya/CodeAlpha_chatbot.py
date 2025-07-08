def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hi!👋"
    elif "how are you" in user_input:
        return "I'm fine, thanks! "
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day! 😊"
    else:
        return "Sorry, I didn't understand that. 😕"

def start_chat():
    print("🤖 Chatbot: Hello! Type something to chat. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print("🤖 Chatbot:", response)

        if "bye" in user_input.lower():
            break
        
start_chat()
