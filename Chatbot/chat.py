import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")
print("Hello! I'm your Gemini chatbot. Type 'quit' to exit.")
model = genai.GenerativeModel("gemini-1.5-flash")
conversation_history = []
    
while True:
    user_input = input("You: ")

    if user_input.lower() == "quit":
        print("Goodbye!")
        conversation_history = []
        exit()
        
    conversation_history.append(user_input)
    prompt = "\n".join(conversation_history) 

    response = model.generate_content(prompt)
        
    print(f"Gemini: {response.text}")
    conversation_history.append(response.text)