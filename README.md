# langchain_tutorial

#  10시에 뵙겠습니다
- pip install langchain langchain-openai
- pip freeze > requirements.txt

# 임베딩 보충 설명
- 자연어 처리의 역사?
## 초기
"I love you"
-> 숫자로 바꾸기 -> 벡터로 만들자
I : [1, 0 ,0 ,0]
love : [0, 1, 0, 0]
you : [0, 0, 1, 0]
me : [0, 0, 0, 1]
I love you -> vector [[1, 0, 0, ,],[0, 1, 0, 0],[0, 0, 1, 0],[0, 0, 0, 1]]
you love me  -> vector [[0, 0, 1],[0, 1, 0],[0, 0, ?]]