from llama_index.core import SimpleDirectoryReader
from config import DATA_DIR


def load_documents_from_directory():
    return SimpleDirectoryReader(DATA_DIR).load_data()