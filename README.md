# Langchain_Prompts practice code

Have gone through the theory concepts of Langchain Prompts(PromptTemplate) and for hands on experience created sample Langchain OpenAI code to
invoke OpenAI LLMs and get responses from them.

#Concepts covered

1) Simple static Prompt from UI screen (Travel Assisstant tool)
2) Simple dynamic prompt using PromptTemplate from langchain (using simple chatbot style)

## Features
1) Created simple "Travel Assistant tool" where user will provide inputs like destination,holiday type(adventours,fun...),no of days and budget
    and these will be passed to static template and then invoke the LLM to proide the response.
2) Created simple in -terminal chatbot where user will ask questions and LLM model will provide response, here created 3 different types of messages to store as chat_history
     a) System Message
     b) Human Message
     c) AI Message
     

#Technologies used
1) Langchain
2) Python
3) OpenAI LLMs
4) PromptTemplate from langchain_core
