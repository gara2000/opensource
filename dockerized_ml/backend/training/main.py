from fastapi import FastAPI

# Create an instance of the FastAPI class
app = FastAPI()

# Define a route with a GET method
@app.get("/api/training/")
def read_root():
    return {"message": "Hello, from training microservice"}

# Define a route with a GET method that takes a parameter
@app.get("/api/training/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}