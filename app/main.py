# Handles chatbot opeartion
from llama_index.llms.gemini import Gemini
from document_processor import load_documents_from_web, load_documents_from_directory
from indexer import create_index
from chatbot import create_chat_engine

def main():
    llm =Gemini()
    
    documents = load_documents_from_directory()
    
    # Create index
    index = create_index(documents, llm)
    
    # Create chat engine
    chat_engine = create_chat_engine(index, llm)
    
    print("Hey ready for the talk! Type 'Pause' if you want to stop.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'pause':
            break
        
        response = chat_engine.chat(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()