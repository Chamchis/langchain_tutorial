from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import os
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')
llm = ChatOpenAI(api_key=openai_api_key)

print(llm)

output = llm.invoke('2024년 청년 정책에 대하여 알려줘')

print(output)
print(type(output))

prompt = ChatPromptTemplate.from_messages(
    [
        ('system','너는 청년을 행복하게 하기 위한 정부정책 안내 컨설턴트야'),
        ('user','{input}')
    ]
)
chain = prompt | llm
print(chain)

print(chain.invoke({'input':'2024년 청년 정책에 대하여 알려줘'}))

