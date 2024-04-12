from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# load .env file variables
load_dotenv()

# load Large Language Model (OpenAI ChatGPT)
llm = ChatOpenAI()

# pre-prompt ChatGPT with instruction, then apply input
prompt = ChatPromptTemplate.from_messages([
    ("system", """Tu es un passionné de jeux de société, expert pour comprendre et restituer les règles, même les plus complexes, avec beaucoup de pédagogie et patience.
      Tu retiens par cœur tous les détails de chaque manuel de règle que tu connais.
      Tes explications sont limpides, sans bruits, sans mots en trop, sans interjections inutiles.
      Tu commences tout de suite tes réponses, sans salamalecs.
      Tu réponds succinctement avec un texte aéré, pas de longue phrase.
      Sauf demande explicite, tu réponds toujours en moins de 200 mots"""),

    ("user", "{input}")
])

# set up the parser for ChatGPT answer
output_parser = StrOutputParser()

# compose the chain of functions
chain = prompt | llm | output_parser | print

chain.invoke({"input": "Peux-tu me dire en moins de 10 lignes en quoi consiste le jeu 'Gloomhaven' ?"})