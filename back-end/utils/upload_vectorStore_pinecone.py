from config import get_vectorStore_pinecone
import uuid

def upload_vectorStore_pinecone(embeddings):
    """Upload básico de embeddings para Pinecone"""
    
    index = get_vectorStore_pinecone()
    
    # Preparar dados para upsert
    vectors = []
    for i, embedding in enumerate(embeddings):
        vectors.append({
            'id': f"doc_{i}_{uuid.uuid4()}",  # ID único
            'values': embedding,              # embedding já é lista de floats
            'metadata': {}                    # adicione metadados se tiver
        })
    
    # Upload
    index.upsert(vectors=vectors)
    
    return len(embeddings)
