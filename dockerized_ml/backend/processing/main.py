from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import json
import pandas as pd
from io import StringIO

class Job(BaseModel):
    info: str
    # data: str

# Create an instance of the FastAPI class
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

# Define a route with a GET method
@app.get("/api/processing/")
def read_root():
    print("hello from read_root")
    return {"message": "Hello, from preprocessing microservice"}

# Define a route with a GET method that takes a parameter
@app.get("/api/processing/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.post("/api/processing/")
async def createJob(job: Job):
    info = json.loads(job.info)
    name = info["name"]
    data = info["data"]

    df = pd.read_csv(StringIO(data))

    print("Data: ", df)

    return {"Job": info}