from fastapi import FastAPI

# Create an instance of the FastAPI class
app = FastAPI()

# Define a route with a GET method
@app.get("/api/processing/")
def read_root():
    print("hello from read_root")
    return {"message": "Hello, from preprocessing microservice"}

# Define a route with a GET method that takes a parameter
@app.get("/api/processing/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}