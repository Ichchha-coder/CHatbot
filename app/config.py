#Stores configuration settings like the collection name, embedding model, and document directory path along with the api key

import os
COLLECTION_NAME = "my_documents"
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
DATA_DIR = "./documents"
os.environ["GOOGLE_API_KEY"] = "Please enter your API key."
