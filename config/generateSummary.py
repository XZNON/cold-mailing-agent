from langchain_core.prompts import PromptTemplate
from langchain_community.document_loaders import PyPDFLoader
from initiation import model,parser
from dotenv import load_dotenv


load_dotenv()

resume = 'resume.json'
summary = 'resumeSummary.json'

#convert pdf to str
def toJson():
    loader = PyPDFLoader("Shivalik_Singh_AI_ML.pdf")    #add the resume of the
    pages = []

    try :
        for page in loader.lazy_load():
            pages.append(page)
    except Exception as e:
        print("Error while reading the resume", e)
    
    pageContent = ""
    for page in pages:
        pageContent += page.page_content
    
    with open ("resume.txt","w",encoding="utf-8") as f:
        f.write(pageContent)

toJson()

def genereateSummary():
    #convert the json resume to the summary
    template = PromptTemplate()