import os
import chromadb
from sentence_transformers import SentenceTransformer
from procesar_pdf import extraer_texto, chunking

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CHROMA_PATH = os.path.join(BASE_DIR, "..", "chroma_db")
PDF_PATH = os.path.join(BASE_DIR, "..", "docs", "Manual_Taekwondo_Graduacion_Combate.pdf")

modelo_embeddings = SentenceTransformer('all-MiniLM-L6-v2')
client = chromadb.PersistentClient(path=CHROMA_PATH)
coleccion = client.get_or_create_collection(name="taekwondo")

def indexar():
    texto = extraer_texto(PDF_PATH)
    chunks = chunking(texto)
    embeddings = modelo_embeddings.encode(chunks).tolist()
    ids = [f"chunk_{i}" for i in range(len(chunks))]
    coleccion.add(documents=chunks, embeddings=embeddings, ids=ids)
    print(f"{len(chunks)} chunks indexados en Chroma")

if __name__ == "__main__":
    indexar()