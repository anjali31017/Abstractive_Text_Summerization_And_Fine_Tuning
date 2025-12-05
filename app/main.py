from fastapi import FastAPI
from pydantic import BaseModel
from summerization_model import summarize
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="News Summarizer API")

origins = [ "*" ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class NewsArticle(BaseModel):
    text: str

@app.get("/")
def root():
    return {"message": "Welcome to News Summarizer API"}

@app.post("/summarize")
def summarize_article(article: NewsArticle):
    try:
        summary = summarize(article.text)
        return {
            "status": 1,
            "summary": summary
            }
    except Exception as e:
        return {
            "status": 0,
            "error": str(e)
            }