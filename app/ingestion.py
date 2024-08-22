#Chunking the document
from llama_index.core import SimpleDirectoryReader
from config import DATA_DIR


def load_documents_from_directory(chunk_size=500):
    reader = SimpleDirectoryReader(DATA_DIR)
    documents = reader.load_data()
    
    # Chunk the documents
    chunked_documents = []
    for document in documents:
        text = document['text']
        chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
        for chunk in chunks:
            chunked_documents.append({'text': chunk})
    
    return chunked_documents
