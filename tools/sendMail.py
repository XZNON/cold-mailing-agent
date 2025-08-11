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
def readExcel(file_path : str):
    '''
    This tools reads the excel file and takes the name, email,company name, title 
    and sends it to the next tool.
    '''
    if not file_path or not os.path.exists(file_path):
        return "Excel file path not found"
    

    df = pd.read_excel(file_path)
    return df.to_dict(orient='records')


@tool
def send_mail(recieverMail : str, title: str, company:str,resume_path : str,job_role : str = "Software developer"):
    '''
    This tools gets the name,recievers mail the content of the mail, and sends the mail to the reciever.
    '''
    body = generateContent(company,title,job_role,resume_path)   #add params

    yg = yagmail.SMTP(SENDER,PASS)

    try:
        yg.send(
            to  = recieverMail,
            subject = f"Seeking a job as {job_role} at your company",
            contents=body,
            attachments=resume_path
        )
    except Exception as e:
        print("error while seinding the mail: ", e)

