from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()
# 1. Instantiate the model
# You can specify the model name and other parameters like temperature (creativity)
model = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

# 2. Define a prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "{text}")
])

# 3. Define an output parser to get a string response
output_parser = StrOutputParser()

# 4. Chain them together
# This creates a simple translation chain
chain = prompt | model | output_parser

# 5. Invoke the chain
response = chain.invoke({"text": "Hello world! How are you"})
print(response)
