
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from dotenv import load_dotenv

load_dotenv()

llm_chat_model = ChatOpenAI()
chat_history = []
chat_template = ChatPromptTemplate([
    ('system','You are helpful customer support assistant'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human','{user_input}')
])

with open('chat_history.txt') as f:
    chat_history.extend(f.readlines())

#llm_chat_model.invoke('chat_history':chat_history,'input_prompt':'Any update on discount') 
print(chat_history) 
#chat_template.invoke({'chat_history':chat_history,'input_prompt':'Any update on discount?'})
#print(f"chat_template is : {chat_template}") 

while True:
    user_input = input('You:')
    chat_history.append(HumanMessage(content=user_input))
    if user_input == 'exit':
        break
    resp = llm_chat_model.invoke(chat_history)
    chat_history.append(AIMessage(content=resp.content))
    print('AI: ',resp.content)

print(chat_history)