import argparse
import sys
from typing import List, Dict, Any

from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage, BaseMessage

def parse_arguments() -> argparse.Namespace:
    """Parses command-line arguments."""
    parser = argparse.ArgumentParser(description="Local LLM Chatbot using Ollama and LangChain.")
    parser.add_argument(
        "--model", 
        type=str, 
        default="gpt-oss:20b", 
        help="Name of the Ollama model to use (default: gpt-oss:20b)"
    )
    parser.add_argument(
        "--system", 
        type=str, 
        default="You are a helpful AI assistant running locally using Ollama.", 
        help="System prompt to define the assistant's behavior."
    )
    parser.add_argument(
        "--history-limit", 
        type=int, 
        default=10, 
        help="Number of message pairs to keep in history (default: 10)"
    )
    return parser.parse_args()

def handle_conversation():
    """Main loop for handling the chat conversation."""
    args = parse_arguments()
    
    print(f"Initializing model: {args.model}...")
    try:
        llm = OllamaLLM(model=args.model)
    except Exception as e:
        print(f"Error initializing model: {e}")
        return

    # Prompt Template Setup
    prompt = ChatPromptTemplate.from_messages([
        ("system", args.system),
        MessagesPlaceholder(variable_name="history"), 
        ("human", "{question}"),
    ])

    # Create the chain
    chain = prompt | llm

    # Memory Management
    chat_history: List[BaseMessage] = []
    
    print(f"\n* Local AI ({args.model}) is ready!")
    print(f"- System: {args.system}")
    print("Type 'exit' or 'quit' to end the session.\n")

    while True:
        try:
            user_input = input("You: ").strip()
        except KeyboardInterrupt:
            print("\nExiting...")
            break
            
        if not user_input:
            continue

        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye! -")
            break
        
        try:
            # Streaming response
            print("Bot: ", end="", flush=True)
            full_response = ""
            
            # Use chain.stream for a better user experience
            for chunk in chain.stream({
                "history": chat_history,
                "question": user_input
            }):
                print(chunk, end="", flush=True)
                full_response += chunk
            
            print() # Newline after response

            # Update Memory
            chat_history.append(HumanMessage(content=user_input))
            chat_history.append(AIMessage(content=full_response))
            
            # Sliding Window Truncation
            if len(chat_history) > args.history_limit * 2: # limit is pairs, list has individual messages
                chat_history = chat_history[-(args.history_limit * 2):]
                
        except Exception as e:
            print(f"\n! Error: {e}")
            print("Tip: Ensure Ollama is running (`ollama serve`) and the model is pulled.")

if __name__ == "__main__":
    handle_conversation()