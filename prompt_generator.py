
from langchain_core.prompts import PromptTemplate

template = PromptTemplate(template="""
You are a helpful travel itinerary assistant.

Create a detailed travel plan based on the following inputs:

Destination: {destination_input}
Travel Type: {travel_type_input} (e.g., adventure, family & fun, relaxation)
Number of Days: {days_input}
Budget        : {budget_input}

Instructions:
- Provide a day-by-day itinerary
- Include activities, places to visit, and food suggestions
- Match the travel type preference
- Keep it practical and realistic (travel time, pacing)
- Add brief tips if helpful

Output format:

Day 1:
- Morning:
- Afternoon:
- Evening:

Day 2:
...

Final Tips:                          
""",
input_variables=['destination_input', 'travel_type_input','days_input','budget_input'],
validate_template=True)

template.save('template.json')