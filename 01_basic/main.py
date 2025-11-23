from fastapi import FastAPI

app=FastAPI()


@app.get("/")

def home():
    return {"msg":"Hello world"}


@app.get("/about")

def about():
    return {"name":"Ultra","learning":"Fastapi","day":1}

