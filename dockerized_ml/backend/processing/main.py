from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import json
import pandas as pd
from io import StringIO
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson import ObjectId

uri = "mongodb://172.1.0.5:27017"

client = MongoClient(uri, server_api=ServerApi('1'))

def toDataFrame(data):
    return pd.read_csv(StringIO(data))

class Job(BaseModel):
    name: str
    data: str

# Create an instance of the FastAPI class
app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:46417"],
#     allow_credentials=True,
#     allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
#     allow_headers=["*"],
# )

# Define a route with a GET method
@app.get("/api/processing/")
def read_root():
    print("hello from read_root")
    return {"message": "Hello, from preprocessing microservice"}

@app.get("/api/processing/jobs")
def getJobs():
    try:
        print("Getting all the jobs")
        jobs = client.mlops.jobs.find()
        res = [{k: str(v) if isinstance(v, ObjectId) else v for k, v in job.items()} for job in jobs]
        return res
    except Exception as e:
        print(e)
        return e

@app.post("/api/processing/")
async def createJob(job: Job):
    print("hello in creating a job", job)
    # info = json.loads(job.info)
    # df = toDataFrame(info["data"])
    doc = {"name": job.name, "data": job.data}
    print(doc)

    try:
        jobsCollection = client.mlops.jobs
        res = jobsCollection.insert_one(doc)
        print("Job inserted successfully")
        return {"Result": "Success"}
    except Exception as e:
        print("Failed to add job to database: ", e)
        return {"Result": "Failure"}