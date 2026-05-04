from langchain_openai import ChatOpenAI
from dotenv  import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate,load_prompt

load_dotenv()

llm_obj = ChatOpenAI(model='gpt-4')

st.header("Travel Assistant")

destination_input = st.selectbox( "Select Destination Location", ["Dubai", "SriLanka", "IceLand", "Masai Mara"] )

travel_type_input = st.selectbox( "Select Travel Type", ["Adventours", "Family & Fun"] ) 

days_input = st.selectbox( "Select No of days", ["Short (1-2 days)", "Medium (3-5 days)", "Long (7-9 days)"] )

budget_input = st.text_input("Enter your budget range in indian rupee")

template = load_prompt('template.json')


if st.button('Plan Iternary'):
 chain = template | llm_obj
 result = chain.invoke(
  {
   'destination_input': destination_input,
   'travel_type_input':travel_type_input,
   'days_input':days_input,
   'budget_input':budget_input
  }
 )
 st.write(result.content)
   