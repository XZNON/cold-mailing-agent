from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from initiation import model,parser
from generateSummary import genereateSummary,toTxt
import os

load_dotenv()

resume = "resume.txt"
resumeSummary = "resumeSummary.txt"

if os.path.exists(resume) and not os.path.exists(resumeSummary):
    try:
        genereateSummary()
    except Exception as e:
        print("Error while generating summary in generateMail.py" , e)

if not os.path.exists(resume) and not os.path.exists(resumeSummary):
    try:
        toTxt()
        genereateSummary()
    except Exception as e:
        print("Error while converting to text and/or generating summary in generateMail.py" , e)

#fetch the resume summary if it exists already
resumeSummary = ""
with open("resumeSummary.txt","r") as f:
    data = f.read()
    resumeSummary += data

#generate the mail body
def generateContent(company_name : str,title:str,job_role:str,resume_summary = resumeSummary):
    prompt1 = PromptTemplate(
    template=(
        "You are an experienced job applicant. "
        "Write a professional and concise job application email body for a company named {company_name}. "
        "The recipient’s title is {title}, and the role you are applying for is {job_role}. "
        "You will also be given a brief summary of the applicant’s resume: {resume_summary}. "
        "Tailor the email content to highlight the applicant’s relevant strengths, skills, and experience. "
        "Use HTML formatting for readability, with short paragraphs and bullet points where relevant. "
        "The tone should be formal, confident, and polite. "
        "Do NOT include greetings (like 'Dear...') or signatures — only the main body content inside <p> or <ul>/<li> tags."
    ),
    input_variables=['company_name', 'title', 'job_role', 'resume_summary']
    )

    
    chain = prompt1 | model | parser
    
    content = chain.invoke({"company_name":company_name,"title":title,"job_role":job_role,"resume_summary":resume_summary})

    return content

# print(generateContent("microsoft","hr","SDE-1"))