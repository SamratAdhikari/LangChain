import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    groq_api_key=groq_api_key,
    model_name="llama-3.1-8b-instant"
)





def generate_resturant_name_and_items(nationality):
    
    prompt_template_name = PromptTemplate(
        input_variables = ['nationality'],
        template = "I want to open a restaurant for {nationality} food. Suggest a fancy name for the restaurant. Give me just a name."
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="resturant_name")


    prompt_template_items = PromptTemplate(
        input_variables = ['resturant_name'],
        template = "Make up some menu items for {resturant_name}. Return it as a comma seperated list and do not add any other information."
    )

    items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="menu_items")
    
    chain = SequentialChain(chains = [name_chain, items_chain],
                              input_variables = ['nationality'], 
                              output_variables = ['resturant_name', "menu_items"])

    response = chain.invoke({"nationality": nationality})
    
    
    return response




if __name__ == "__main__":
    print(generate_resturant_name_and_items("Nepali"))