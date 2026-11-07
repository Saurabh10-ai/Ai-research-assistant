
import os
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from tools import web_search, scrap_url



load_dotenv()

api_key = os.getenv("OLLAMA_API_KEY")

if not api_key:
    raise ValueError("OLLAMA_API_KEY is missing from .env")

llm = ChatOpenAI(
    model="beam:cloud",
    base_url="https://ollama.com/v1",
    api_key=api_key,
    temperature=0.7
)

# Research agents
def build_search_agent():
    return create_agent(model=llm, tools=[web_search])


def build_read_agent():
    return create_agent(model=llm, tools=[scrap_url])


# Writer chain

writer_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert research writer. Write clear, structured and insightful reports."),
    (("human", """Write a detailed research report on the topic below.

Topic: {topic}

Research Gathered:
{research}

Structure:
- Introduction
- Key Findings (minimum 3 points)
- Conclusion
- Sources

List every website URL provided in the research.
For each source, show its title and clickable URL using:
- [Website Title](https://example.com)

Do not invent URLs."""))
])

writer_chain = writer_prompt | llm | StrOutputParser()





critic_prompt = ChatPromptTemplate.from_messages([
     ("system", "You are a sharp and constructive research critic. Be honest and specific."),
    ("human", """Review the research report below and evaluate it strictly.

    Report:
    {report}

    Respond in this exact format:

    Score: X/10

Strengths:
    - ...
    - ...

    Areas to Improve:
    - ...
    - ...

    One line verdict:
    ..."""),
])

critic_chain = critic_prompt | llm | StrOutputParser()

