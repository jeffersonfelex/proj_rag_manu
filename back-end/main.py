from upLoad_data import upLoad_data_VectorStore
from utils.upload_vectorStore_pinecone import upload_vectorStore_pinecone

print("Iniciando pipeline de MD -> Embeddings -> Pinecone\n")

embeddings_gerado = upLoad_data_VectorStore()

if embeddings_gerado:
    enviados = upload_vectorStore_pinecone(embeddings_gerado)
    print(f"\n Embeddings enviados para Pinecone: {enviados}")
else:
    print("\n Nenhum embedding gerado.")
