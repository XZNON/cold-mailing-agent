from fastapi import FastAPI,HTTPException,File,UploadFile,Form
from fastapi.responses import JSONResponse
import shutil
import os
from Agent.agent import agent_executor
# from Agent.agent import agent_executor

app = FastAPI()

@app.get("/")
def home():
    return {"message":"This is home"}

@app.post("/send_mail")
async def send_mail(job_role = Form(default=None),file : UploadFile = File(...,description="Excel file with recepient details [Name,Email,Company Name]")):
    # tempFile = f"temp_{file.filename}"
    uploadDir = "uploaded_files"
    os.makedirs(uploadDir,exist_ok=True)
    file_path = os.path.join(uploadDir,f"temp_{file.filename}")


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
        agent_executor.invoke({"input":f"Send the mails from the provided excel file located at '{os.path.abspath(file_path)}' with job role {job_role} "})
    except Exception as e:
        raise HTTPException(status_code=403,detail=f"Unable to execute the agent : {e}")
    
    os.remove(file_path)
    return JSONResponse(status_code=200,content={"Message":"Emails sent successfully"})
    

    