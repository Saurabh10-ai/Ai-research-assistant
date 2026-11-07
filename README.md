# 🤖 AI Research Assistant – Multi-Agent Research System

An intelligent AI-powered research assistant designed to automate web research, information extraction, content analysis, and report generation using a Multi-Agent AI architecture.

Built using **Python, LangChain, Streamlit, and Large Language Models (LLMs)**, this application simplifies the research process by dividing complex research tasks among specialized AI agents. It searches for relevant information, extracts meaningful content from websites, analyzes findings, and generates structured research reports.

## 🎯 Project Overview

The AI Research Assistant takes a user's research topic as input and executes an automated research workflow. Instead of manually searching multiple websites and organizing information, users can leverage AI agents to perform different research tasks collaboratively.

## ✨ Key Features

- **Automated Web Research:** Searches the internet to find relevant and up-to-date information about a given topic.
- **Multi-Agent Architecture:** Uses specialized AI agents to divide and manage research tasks.
- **Web Scraping:** Extracts and processes website content using BeautifulSoup.
- **Content Analysis:** Analyzes collected information and identifies important insights.
- **AI Report Generation:** Creates structured, detailed, and easy-to-understand research reports.
- **Report Evaluation:** Uses a Critic Agent to review generated reports and provide quality feedback.
- **Token Usage Tracking:** Monitors prompt tokens, completion tokens, and total token consumption.
- **Interactive UI:** Provides a user-friendly interface built with Streamlit.

## 🧠 Multi-Agent Workflow

The system consists of four specialized agents:

1. **Search Agent:** Finds relevant information and research sources from the internet.
2. **Reader Agent:** Extracts website content and reads the collected information.
3. **Writer Agent:** Converts research findings into detailed and structured reports.
4. **Critic Agent:** Evaluates the generated report and provides feedback to improve its quality.

## 🛠️ Technology Stack

- **Programming Language:** Python
- **AI Framework:** LangChain
- **Agent Architecture:** ReAct Agents
- **LLM Integration:** AIML API / OpenAI-compatible LLM APIs
- **Web Scraping:** BeautifulSoup
- **Frontend:** Streamlit
- **Workflow:** LangChain Expression Language (LCEL)

## ⚙️ How It Works

1. User enters a research topic.
2. Search Agent collects relevant information.
3. Reader Agent extracts and processes website content.
4. Writer Agent generates a comprehensive research report.
5. Critic Agent evaluates the report.
6. The final research output is presented through the Streamlit interface.

## 💡 Project Objective

The main objective is to explore the practical implementation of Generative AI, autonomous AI agents, tool integration, and multi-agent collaboration to build an intelligent research automation system.

## 🚀 Future Improvements

- Add PDF and document export functionality.
- Integrate additional search engines and research sources.
- Implement persistent conversation memory.
- Add source citations and reference management.
- Improve report accuracy through iterative agent feedback.
- Add support for downloading research reports.

## 👨‍💻 Author

Developed as a hands-on Generative AI project to explore multi-agent systems, LLM integration, web scraping, and automated research workflows.
