import os
import sys
import time
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

# Initialize the model
model = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite", 
    google_api_key=os.getenv("GEMINI_API_KEY")
)

print("AI Chatbot Initialized! Type 'exit' or 'quit' to end the conversation.\n")

# Start an interactive loop
while True:
    # 1. Take input from the user
    user_prompt = input("You: ")
    
    # 2. Check if the user wants to break out of the loop
    if user_prompt.lower() in ['exit', 'quit']:
        print("Goodbye!")
        break
        
    # Skip empty inputs
    if not user_prompt.strip():
        continue

    print("AI: ", end="")
    
    # 3. Stream the output based on user input
    for chunk in model.stream(user_prompt):
        text_content = chunk.text if hasattr(chunk, 'text') else str(chunk.content)
        
        sys.stdout.write(text_content)
        sys.stdout.flush()
        time.sleep(0.12) # Slightly faster delay for smoother text flow
        
    print("\n" + "-"*40 + "\n") # Print a divider after the response
