from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage

load_dotenv()

llm_obj = ChatOpenAI(model='gpt-4')

chat_messages = []

chat_messages.append(SystemMessage(content='You are helpful AI chatbot assisstant'))

while True:
    user_input = input('You:')
    chat_messages.append(HumanMessage(content=user_input))
    if user_input == 'exit':
        break
    resp = llm_obj.invoke(chat_messages)
    chat_messages.append(AIMessage(content=resp.content))
    print('AI: ',resp.content)

print(chat_messages)