from utils.generator_chunk import generate_chunks
from utils.generator_embeddings import generate_embeddings
from utils.upload_vectorStore_pinecone import upload_vectorStore_pinecone

input_diretorio = "seu diretorio aqui"

def upLoad_data_VectorStore():
    arquivos_md = input_diretorio

    if not arquivos_md:
        print("Nenhum arquivo .md encontrado!")
        return

    print(f"{len(arquivos_md)} arquivos .md encontrados.")

    # Lê e junta o conteúdo de todos os arquivos
    textos = []
    for arquivo in arquivos_md:
        try:
            with open(arquivo, "r", encoding="utf-8") as f:
                textos.append(f.read())
        except Exception as e:
            print(f"Erro ao ler {arquivo}: {e}")

    texto_gerado = "\n".join(textos)

    # Gera chunks
    chunk_gerado = generate_chunks(texto_gerado)
    print(f"{len(chunk_gerado)} chunks gerados com sucesso!")

    # Gera embeddings
    embeddings_gerado = generate_embeddings(chunk_gerado)
    print(f"{len(embeddings_gerado)} embeddings gerados com sucesso!")
    
    # Manda para o pinecone
    enviados = upload_vectorStore_pinecone(embeddings_gerado)
    print(f"Foram enviados: {enviados} embeddings para o Pinecone.")
    
    return embeddings_gerado
