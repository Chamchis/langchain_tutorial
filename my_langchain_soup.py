from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
import os
from langchain_community.document_loaders import WebBaseLoader

load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')
embeddings = OpenAIEmbeddings(api_key=openai_api_key)
loader = WebBaseLoader('https://www.moel.go.kr/policy/policyinfo/support/list4.do')
print(loader)

docs = loader.load()
print(docs)