from pypdf import PdfReader

def extraer_texto(ruta_pdf):
    reader = PdfReader(ruta_pdf)
    texto_completo = ""
    for pagina in reader.pages:
        texto_completo += pagina.extract_text() + "\n"
    return texto_completo

def chunking(texto, tamano_chunk = 800, overlap = 100):
    chunks = []
    inicio = 0
    while inicio < len(texto):
        fin = inicio + tamano_chunk
        chunks.append(texto[inicio:fin])
        inicio += tamano_chunk - overlap
    return chunks

