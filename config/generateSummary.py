from langchain_core.prompts import PromptTemplate
from langchain_community.document_loaders import PyPDFLoader
from config.initiation import model,parser
from dotenv import load_dotenv


load_dotenv()

resume = 'resume.txt'
summary = 'resumeSummary.txt'

#convert pdf to str
def toTxt():
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

def genereateSummary():
    resume_text = ""

    try:
        with open ("resume.txt",'r') as f:
            data = f.read()
            resume_text += data
    except Exception as e:
        print("Error while reading from resume text" , e)

    #convert the json resume to the summary
    template = PromptTemplate(
        template=(
            "You are given the full text of a candidate's resume.\n"
            "Analyze the content and generate a concise, professional summary highlighting:\n"
            "- Key skills and areas of expertise\n"
            "- Notable work experience and achievements\n"
            "- Relevant education or certifications\n\n"
            "The summary should be clear, well-structured, and no longer than 4-5 sentences.\n"
            "Avoid unnecessary repetition and focus only on the most important details.\n\n"
            "Resume:\n{resume_text}"
        ),
        input_variables=['resume_text']
    )
    try:
        chain = template | model | parser
        content = chain.invoke({"resume_text":resume_text})
    except Exception as e:
        print("Error while generating resume summary", e)
    
    try:
        with open("resumeSummary.txt","w",encoding="utf-8") as f:
            f.write(content)
    except Exception as e:
        print("Error while creating resume summary text file", e)
