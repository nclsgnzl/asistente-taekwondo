# 🥋 Asistente RAG - Taekwondo

Sistema de preguntas y respuestas sobre reglamento, poomsae y técnicas de combate 
de Taekwondo, usando arquitectura RAG (Retrieval-Augmented Generation) con la API 
de Claude (Anthropic).

## 🏗️ Arquitectura

PDF (manual técnico)
→ extracción de texto (pypdf)
→ chunking con overlap
→ generación de embeddings (sentence-transformers)
→ indexado en base de datos vectorial (ChromaDB)
→ retrieval semántico (búsqueda por similitud)
→ generación de respuesta contextualizada (Claude API)


El sistema no depende del conocimiento general del modelo sobre Taekwondo: 
cada respuesta se construye a partir de los fragmentos más relevantes 
recuperados del manual técnico específico, y el modelo está instruido para 
declarar explícitamente cuando la información solicitada no se encuentra 
en el documento fuente.

## 🛠️ Stack técnico

- **Backend:** Python, FastAPI
- **LLM:** Claude (Anthropic API)
- **Embeddings:** sentence-transformers (`all-MiniLM-L6-v2`)
- **Vector store:** ChromaDB
- **Frontend:** HTML/JS vanilla
- **Seguridad:** autenticación por API key + rate limiting (slowapi)

## 🔒 Decisiones de diseño

- **Prompt anti-alucinación:** el modelo responde únicamente con base en el 
  contexto recuperado del documento, evitando completar con conocimiento 
  general no verificado.
- **Chunking con overlap:** fragmentos de 800 caracteres con 100 de 
  solapamiento entre ellos, para evitar cortar ideas o instrucciones técnicas 
  a la mitad entre dos fragmentos consecutivos.
- **Rate limiting:** máximo 10 requests por minuto por dirección IP, para 
  prevenir abuso del endpoint y controlar el consumo de la API de Claude.
- **Autenticación por API key propia:** el endpoint principal valida un 
  header `X-API-Key` antes de procesar cualquier solicitud.
- **Separación backend/frontend:** el backend (con la lógica sensible y 
  las credenciales de la API de Claude) corre en Render; el frontend 
  estático se sirve por separado en Vercel.

## 📁 Estructura del proyecto

asistente-taekwondo/
├── docs/ # Documento fuente (PDF del manual)
├── src/
│ ├── procesar_pdf.py # Extracción de texto y chunking
│ ├── vector_store.py # Generación de embeddings e indexado en Chroma
│ ├── rag.py # Lógica de retrieval + generación de respuesta
│ └── api.py # API REST con FastAPI (auth + rate limiting)
├── index.html # Interfaz de usuario
├── requirements.txt
└── README.md


## 🚀 Cómo correrlo localmente

Clona el repositorio e instala las dependencias:

```bash
git clone https://github.com/TU-USUARIO/asistente-taekwondo.git
cd asistente-taekwondo
python -m venv venv
venv\Scripts\activate      # Windows
pip install -r requirements.txt
```

Crea un archivo `.env` en la raíz con:

ANTHROPIC_API_KEY = tu_key_de_anthropic
APP_API_KEY = una_clave_propia_que_definas

Indexa el documento (solo la primera vez, o si cambias el PDF):

```bash
python src/vector_store.py
```

Levanta el servidor:

```bash
cd src
uvicorn api:app
```

Abre `index.html` en el navegador para interactuar con el asistente.

## 📌 Autor

Nicolás Abarca — Full Stack Developer & AI Engineer  
[LinkedIn](https://www.linkedin.com/in/nabarcac)

