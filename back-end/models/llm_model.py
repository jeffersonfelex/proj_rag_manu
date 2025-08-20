from langchain.schema import HumanMessage, SystemMessage
from config import get_llm
import os 

prompt = os.getenv("PROMPT_MESTRE")
