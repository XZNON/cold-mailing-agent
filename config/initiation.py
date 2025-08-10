from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = GoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.2)
parser = StrOutputParser()
