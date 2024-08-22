# Chat with your document

This project is a document-based chatbot that helps you find information. It uses a embedding model for understanding text and the Gemini model for responses. 

## Setup and Configuration

1. Clone the repository:
   ```
   git clone https://github.com/Ichchha-coder/CHatbot
   cd chatbot
   ```

2. Build the Docker image:
   ```
   docker build chatbot.
   ```

3. Run the Docker container:
   ```
   docker run chatbot
   ```

# Usage Instruction
Interact with document once the containerization is done.

# Modules
main.py: Start flow of application.
config.py: Centralizes configuration settings.
processor.py: Handles loading and optional chunking of documents from the specified directory.
indexing.py: Creates a vector-based index of documents using embeddings and a vector store.
chat_engine.py: Sets up the chatbot engine with memory and retrieval capabilities for generating responses.
ingestion.py: Manages the ingestion of documents from various sources for further processing.

# Vector Database SetUp
Manage the vector database client and vector_store in indexing.py 
Qdrant in this case, follow the same for other database

# Embedding Model Replacement 
Replace the embedding model in "config.py" and make necessary installations in case of necessity and update in requirements.txt.

# PS:
There are virtual environment file in folder venv. Incase of use of dockerization ,ignore it. If you don't use docker then you have to install the dependencies using pip install -r requirements.txt

