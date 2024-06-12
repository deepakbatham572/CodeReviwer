from langchain.prompts import PromptTemplate
from langchain_community.llms import HuggingFaceEndpoint


def getLLMResponse(data,api_key):

    llm = HuggingFaceEndpoint(repo_id='mistralai/Mistral-7B-Instruct-v0.2' , huggingfacehub_api_token = api_key)    

    #Template for building the PROMPT
    template ="""
    You are a code review assistant. 
    Provide detailed suggestions to improve the given {file} code with proper indent in coding language
    
    \n\n
    Review Code:
    
    """
  
    #Creating the final PROMPT
    prompt = PromptTemplate(
    input_variables=["file"],
    template=template
    )

    #Generating the response using LLM
    #Last week langchain has recommended to use 'invoke' function for the below please :)
    response=llm.invoke(prompt.format(file = data))
    print(response)
    return response



