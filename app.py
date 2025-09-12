from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Define the input data model
class JobData(BaseModel):
    job: str
    repo: str

# Create FastAPI app
app = FastAPI()

# Define the API endpoint
@app.post("/submit-job")
async def submit_job(data: JobData):
    # You can add processing logic here
    return {
        "message": "Job submitted successfully!",
        "received_data": {
            "job": data.job,
            "repo": data.repo
        }
    }
