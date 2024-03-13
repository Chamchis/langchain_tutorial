from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
import os
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain

load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')
llm = ChatOpenAI(api_key=openai_api_key)
embeddings = OpenAIEmbeddings(api_key=openai_api_key)
loader = WebBaseLoader('https://www.moel.go.kr/policy/policyinfo/support/list4.do')
text_splitter = RecursiveCharacterTextSplitter()
docs = loader.load()
documents = text_splitter.split_documents(docs)
vector = FAISS.from_documents(documents, embeddings)

prompt = ChatPromptTemplate.from_template("""Answer the following question based only on the provided context:

<context>
{context}
</context>

Question: {input}""")

document_chain = create_stuff_documents_chain(llm, prompt)

# 바로 Docs 내용을 반영도 가능합니다.

document_chain.invoke({
    "input": "국민취업지원제도가 뭐야",
    "context": [Document(page_content="""국민취업지원제도란?

취업을 원하는 사람에게 취업지원서비스를 일괄적으로 제공하고 저소득 구직자에게는 최소한의 소득도 지원하는 한국형 실업부조입니다. 2024년부터 15~69세 저소득층, 청년 등 취업취약계층에게 맞춤형 취업지원서비스와 소득지원을 함께 제공합니다.
[출처] 2024년 달라지는 청년 지원 정책을 확인하세요.|작성자 정부24""")]
})

print(document_chain)
print(document_chain.invoke)

retriever = vector.as_retriever()
retrieval_chain = create_retrieval_chain(retriever, document_chain)

response = retrieval_chain.invoke({"input": "상담센터 전화번호 뭐야"})
print(response["answer"])

# LangSmith offers several features that can help with testing:...