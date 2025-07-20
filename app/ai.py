from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
import os

def model() :
    api_key = os.getenv("API_KEY")
    try:
        llm = ChatGroq(temperature=0, groq_api_key=api_key, model_name="llama-3.3-70b-versatile")
        return llm
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


class AiChatAgent :
    def __init__(self) :
        self.model = model()

        if not self.model:
            raise ValueError("Failed to initialize the AI model. Please check your API key and model configuration.")

    def ask(self, query) :
        try:
            prompt = PromptTemplate.from_template(
                """
                You are a helpful AI assistant. Answer the following question in short:
                {query}

                Note :- Make sure the answer is concise and to the point, and short 
                (NO PREAMBLE, NO CONCLUSION, NO FILLER TEXT, JUST ANSWER THE QUESTION DIRECTLY).
                """
            )
            response = self.model.invoke(prompt.format(query=str(query))).content
            
            if not response:
                raise ValueError("Received an empty response from the AI model.")
    
            return response
        except Exception as e:
            print(f"An error occurred while chatting: {e}")
            return None