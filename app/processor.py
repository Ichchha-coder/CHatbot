#Document loading 

from llama_index import SimpleDirectoryReader
from config import DATA_DIR

def load_documents_from_directory():
    reader = SimpleDirectoryReader(DATA_DIR)
    return reader.load_data()
