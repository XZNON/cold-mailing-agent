from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from config.initiation import model,parser
from config.generateSummary import genereateSummary,toTxt
import os

load_dotenv()


#generate the mail body
def generateContent(company_name : str,title:str,job_role:str,resume_path :str):
    resume_summary = "resumeSummary.txt"
    if not os.path.exists(resume_summary):
        toTxt(resume_path)
        genereateSummary()


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