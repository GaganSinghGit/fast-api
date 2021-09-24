from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def home():
    return {"Data":"Testing"}

@app.get("/abput")
def about():
    return {"Data":"about"}