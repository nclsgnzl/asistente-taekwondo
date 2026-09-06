import os
from dotenv import load_dotenv
from anthropic import Anthropic
import chromadb
from sentence_transformers import SentenceTransformer

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CHROMA_PATH = os.path.join(BASE_DIR, "..", "chroma_db")

load_dotenv()
client_claude = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
modelo_embeddings = SentenceTransformer('all-MiniLM-L6-v2')
#client_chroma = chromadb.PersistentClient(path="chroma_db")
client_chroma = chromadb.PersistentClient(path=CHROMA_PATH)
coleccion = client_chroma.get_collection(name="taekwondo")

def buscar_contexto(pregunta, n_resultados=3):
    embedding_pregunta = modelo_embeddings.encode([pregunta]).tolist()
    resultados = coleccion.query(query_embeddings=embedding_pregunta, n_results=n_resultados)
    return resultados["documents"][0]

def responder(pregunta):
    chunks_relevantes = buscar_contexto(pregunta)
    contexto = "\n\n".join(chunks_relevantes)
    prompt = f"""Basándote únicamente en el siguiente contexto sobre Taekwondo, responde la pregunta.
Si la respuesta no está en el contexto, dilo claramente.

Contexto:
{contexto}

Pregunta: {pregunta}"""
    response = client_claude.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.content[0].text

if __name__ == "__main__":
    while True:
        pregunta = input("\nPregunta sobre Taekwondo (o 'salir'): ")
        if pregunta.lower() == "salir":
            break
        print("\n" + responder(pregunta))