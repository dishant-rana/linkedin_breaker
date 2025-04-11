from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from third_parties.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent

load_dotenv()

"""information = 
  Elon Reeve Musk (/ˈiːlɒn mʌsk/; born June 28, 1971) is a businessman known for his key roles in Tesla, Inc., SpaceX, and X, formerly Twitter (which he has owned since 2022). Since 2025, he has been a senior advisor to President Donald Trump and head of the Department of Government Efficiency (DOGE). Musk is the wealthiest person in the world; as of February 2025, Forbes estimates his net worth to be US$384 billion.

Musk was born to an affluent South African family in Pretoria before immigrating to Canada, acquiring Canadian citizenship via his mother. He moved to California in 1995 to attend Stanford University, and with his brother Kimbal co-founded the software company Zip2, which was acquired by Compaq in 1999. That same year, Musk co-founded X.com, a direct bank, that later formed PayPal. In 2002, Musk acquired U.S. citizenship, and eBay acquired PayPal. Using the money he made from the sale, Musk founded SpaceX, a spaceflight services company, in 2002. In 2004, Musk was an early investor in electric vehicle manufacturer Tesla and became its chairman and later CEO. In 2018, the U.S. Securities and Exchange Commission (SEC) sued Musk for fraud, alleging he falsely announced that he had secured funding for a private takeover of Tesla; he stepped down as chairman and paid a fine. Musk was named Time magazine's Person of the Year in 2021. In 2022, he acquired Twitter, and rebranded the service as X the following year. In January 2025, he was appointed head of Trump's newly created DOGE. 
"""

def ice_break_with(name:str)->str:
    linkedin_username=linkedin_lookup_agent(name=name)
    linkedin_data=scrape_linkedin_profile(linkedin_profile_url=linkedin_username,mock=False)
    summary_template = """
        given the Linkedin information {information} about a person I want you to create:
        1. A short summary
        2. two interesting facts about them
  """
    print(linkedin_data)
    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )
    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
    # llm = ChatOllama(model="llama3")

    chain = summary_prompt_template | llm | StrOutputParser()
    
    res = chain.invoke(input={"information": linkedin_data})

    print(res)

if __name__ == "__main__":
    print("Executing the Command: ")
    ice_break_with(name="Dishant Rana Antwalk")