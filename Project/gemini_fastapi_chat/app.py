from fastapi import FastAPI,Request,Form
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
load_dotenv()

app=FastAPI(
    title="gemini-fastapi-demo",
    description="langchain+gemini UI example",
    version="1.0"
)
app.mount("/static",StaticFiles(directory="static"),name="static")


#template
templates=Jinja2Templates(directory="templates")

#LLM
llm=ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=1.0
)

#HOME UI

@app.get("/",response_class=HTMLResponse)
def home(
    request:Request
):
    return templates.TemplateResponse(
        "index.html",
        {"request":request,"answer":None}
    )


#handle form submit
@app.post("/ask",response_class=HTMLResponse)
def ask_question(
    request:Request,
    question:str=Form(...)
):
    result=llm.invoke(question)
    
    return templates.TemplateResponse(
        "index.html",
        {
            "request":request,
            "question":question,
            "answer":result.content
        }
    )