from config import get_embeddings

def generate_embeddings(chunks: list[str]) -> list[list[float]]:
    embeddings = get_embeddings()
    generated_embeddings = [embeddings.embed_query(chunk) for chunk in chunks]
    
    return generated_embeddings
