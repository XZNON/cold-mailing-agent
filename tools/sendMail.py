from langchain_google_genai import GoogleGenerativeAI
from langchain_core.tools import tool,InjectedToolArg
import pandas as pd
import yagmail
from config import generateMail 
from dotenv import load_dotenv
import os 

load_dotenv()

SENDER = os.getenv("SENDERS_MAIL")
PASS = os.getenv("APP_PASS")

# llm = GoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.2)

@tool
def send_mail(name : str,recieverMail : str, title: str, company:str):
    '''
    This tools gets the name,recievers mail the content of the mail, and sends the mail to the reciever.
    '''
    reciever = recieverMail
    body = generateMail()   #add params

    yg = yagmail.SMTP(SENDER,PASS)
    yg.send(
        to  = recieverMail,
        subject = "Seeking a job as {job_role} at your company",
        contents=body
    )
