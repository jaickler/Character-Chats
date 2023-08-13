from langchain.chains import ConversationChain, LLMChain, SimpleSequentialChain
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, AgentType, load_tools
from langchain import PromptTemplate, SerpAPIWrapper
from langchain.prompts import HumanMessagePromptTemplate, ChatPromptTemplate
from langchain.prompts.chat import SystemMessage, HumanMessagePromptTemplate
from langchain.memory import ConversationSummaryBufferMemory
from langchain.tools import BaseTool, StructuredTool, Tool, tool
from dotenv import load_dotenv
from os import getenv
from datetime import datetime as dt
from newsapi import NewsApiClient
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import WebBaseLoader
from langchain.chains.summarize import load_summarize_chain


class Character_Chain():
    def __init__(self, character_description: str, participant_description: str) -> None:
        self.character_description = character_description
        self.participant_description = participant_description
        load_dotenv()
        self.llm = ChatOpenAI(openai_api_key=getenv("OPEN_AI_API_KEY"))
        self.memory = ConversationSummaryBufferMemory(llm=self.llm)

        self.template = ChatPromptTemplate.from_messages(
        [
        SystemMessage(
            content=(
                f"You are {character_description} and are in a conversation with "
                f"{participant_description} and will respond in the same way he would, use pronouns." 
                " Also be sure to discuss relevant events.\n"
            )
        ),
        f"Current Relevant events: {self.get_news()}",
        "Chat History: {history}\n",
        f"current time: {dt.now()}",
        f"{input}\n",
        
        ]
        )
        self.chain = ConversationChain(llm=self.llm, memory=self.memory, prompt=self.template, verbose=True)

    def run(self, input: str):
        return(self.chain.run(input=input))

    def get_news(self):
        api = NewsApiClient(api_key=getenv("NEWSAPI_API_KEY"))

        top_headlines = api.get_top_headlines(
                                                page=1,
                                                page_size=5,
                                                language='en',
                                                country='us')
        
        docs = []
        for article in top_headlines["articles"]:
            loader = WebBaseLoader(article["url"])
            docs.append(loader.load()[0])
        
        llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo-16k", openai_api_key=getenv("OPEN_AI_API_KEY"))
        chain = load_summarize_chain(llm, chain_type="stuff")

        return(chain.run(docs))






