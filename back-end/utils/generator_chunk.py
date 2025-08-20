from langchain.text_splitter import CharacterTextSplitter

def generate_chunks(text: str, chunk_size: int = 1000, chunk_overlap: int = 200) -> list[str]:
    text_splitter = CharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks