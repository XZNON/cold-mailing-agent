from langchain_core.tools import tool,InjectedToolArg
import pandas as pd
import yagmail
from config.generateMail import generateContent
from dotenv import load_dotenv
import os 

load_dotenv()

SENDER = os.getenv("SENDERS_MAIL","").strip()
PASS = os.getenv("APP_PASS","").strip()

@tool
def readExcel():
    '''
    This tools reads the excel file and takes the name, email,company name, title 
    and sends it to the next tool.
    '''
    df = pd.read_excel("demo.xlsx")
    return df.to_dict(orient='records')


@tool
def send_mail(recieverMail : str, title: str, company:str,job_role : str = "Software developer"):
    '''
    This tools gets the name,recievers mail the content of the mail, and sends the mail to the reciever.
    '''
    reciever = recieverMail
    body = generateContent(company,title,job_role)   #add params

    yg = yagmail.SMTP(SENDER,PASS)
    yg.send(
        to  = recieverMail,
        subject = f"Seeking a job as {job_role} at your company",
        contents=body,
        attachments="Shivalik_Singh_AI_ML.pdf"
    )
