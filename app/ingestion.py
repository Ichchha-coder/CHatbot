import os

# QDRANT_HOST = os.getenv("QDRANT_HOST", "localhost")
# QDRANT_PORT = int(os.getenv("QDRANT_PORT", 6333))
COLLECTION_NAME = "my_documents"
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
DATA_DIR = "./documents"
os.environ["GOOGLE_API_KEY"] = "AIzaSyAld7eOoQK142jd_sWxvKfy7asIdk1MAYw"