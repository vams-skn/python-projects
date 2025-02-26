# Gemini Chatbot  

This is a simple AI-powered chatbot that uses Google's Gemini API. It maintains a conversation history and responds based on previous inputs, providing a more natural chat experience.

## How to Use

1. Install Dependencies:  
   ```Python
   pip install google-generativeai
   ```

2. Set up Your API Key:
    - Go to [Google Cloud Console](https://console.cloud.google.com) and sign in with your Google Account (or create one if you don’t have it).
    - Enable the Gemini API by visiting [Google AI Studio.](https://aistudio.google.com/)
    - Click on "Get API Key" and follow the setup instructions.
    - Copy the API Key provided.
   - Replace `"YOUR_API_KEY"` in the script with your actual Google Gemini API Key.

3. Run the Script:
   ```Python
   python chatbot.py
   ```

4. Chat with Gemini!
   - Type your messages, and the chatbot will respond.  
   - Type `'quit'` to exit the chat.  