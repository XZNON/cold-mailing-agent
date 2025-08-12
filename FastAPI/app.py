from fastapi import FastAPI,HTTPException,File,UploadFile,Form
from fastapi.responses import JSONResponse
import shutil
import os
from Agent.agent import agent_executor
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change to your frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message":"This is home"}

@app.post("/send_mail")
async def send_mail(job_role = Form(default=None,description="The job role that the person is applying for."),
                    file : UploadFile = File(...,description="Excel file with recepient details [Name,Email,Company Name]"),
                    resume : UploadFile = File(...,description="The resume of te applicant.")):
    # tempFile = f"temp_{file.filename}"
    uploadDir = "uploaded_files"
    os.makedirs(uploadDir,exist_ok=True)
    file_path = os.path.join(uploadDir,f"temp_{file.filename}")

    resume_path = os.path.join(uploadDir,f"temp_{resume.filename}")

    try:
        with open(resume_path,"wb") as rf:
            shutil.copyfileobj(resume.file,rf)
    except Exception as e:
        raise HTTPException(status_code=405,detail=f"Unable to laod the resume file : {e}")

    try:
        os.environ["RESUME_FILE_PATH"] = resume_path
    except Exception as e:
        return HTTPException(status_code=403,detail=f"Unable to store the resume in local storage.")
    
    try:
        with open (file_path,"wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    except Exception as e:
        raise HTTPException(status_code=401,detail=f"Unable to load the excel file : {e}")
    
    try:
        os.environ["EXCEL_FILE_PATH"] = file_path
    except Exception as e:
        return HTTPException(status_code=403,detail=f"Unable to store the file in local storage.")
    
    try:
        agent_executor.invoke({"input":f"Send the mails from the provided excel file located at '{os.path.abspath(file_path)}' with job role {job_role} and the resume at {os.path.abspath(resume_path)} "})
    except Exception as e:
        raise HTTPException(status_code=403,detail=f"Unable to execute the agent : {e}")
    
    os.remove(file_path)
    os.remove(resume_path)
    os.remove('resumeSummary.txt')
    os.remove('resume.txt')
    return JSONResponse(status_code=200,content={"Message":"Emails sent successfully"})
    

    