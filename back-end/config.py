import os
from dotenv import load_dotenv
from langchain_openai import AzureOpenAIEmbeddings
from langchain_openai import AzureChatOpenAI
from pinecone import Pinecone

load_dotenv()

def get_llm():
    llm = AzureChatOpenAI(
        openai_api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
        api_key=os.getenv("AZURE_OPENAI_API_KEY")
    )
    return llm

def get_embeddings():
    embeddings = AzureOpenAIEmbeddings(
        deployment=os.getenv("AZURE_EMBEDDINGS_DEPLOYMENT"),
        model=os.getenv("AZURE_EMBEDDINGS_MODEL_NAME"),
        openai_api_version=os.getenv("AZURE_EMBEDDINGS_API_VERSION"),
        azure_endpoint=os.getenv("AZURE_EMBEDDINGS_ENDPOINT"),
        api_key=os.getenv("AZURE_EMBEDDINGS_API_KEY")
    )
    return embeddings

def get_vectorStore_pinecone():
    pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
    index = pc.Index(os.getenv("PINECONE_NAME_INDEX"))
    return index