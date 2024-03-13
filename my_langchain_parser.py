from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')
llm = ChatOpenAI(api_key=openai_api_key)
output_parser = StrOutputParser()

prompt = ChatPromptTemplate.from_messages(
    [
        ('system','너는 청년을 행복하게 하기 위한 정부정책 안내 컨설턴트야'),
        ('user','{input}')
    ]
)

chain = prompt | llm | output_parser

print(chain)

print(chain.invoke({"input": "2024년 청년 지원 정책에 대해 알려줘"}))

