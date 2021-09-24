from fastapi import FastAPI, Path
from pydantic import BaseModel 

app = FastAPI()

@app.get("/")
def home():
    return {"Data":"Testing"}

@app.get("/about")
def about():
    return {"Data":"about"}

inventory = {
        1:{
            "name":"Milk",
            "price":2.99,
            "brand":"Regular"
        }
}

@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(None,description="asdfasdfdasf")):
    return inventory[item_id]


@app.post("/crerate-item")
def create_item():
    
    return 