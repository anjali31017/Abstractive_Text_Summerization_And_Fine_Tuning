from fastapi import FastAPI
from pydantic import BaseModel
from summerization_model import summarize

app = FastAPI(title="News Summarizer API")

# Input schema
class NewsArticle(BaseModel):
    text: str

@app.get("/")
def root():
    return {"message": "Welcome to News Summarizer API"}

@app.post("/summarize")
def summarize_article(article: NewsArticle):
    summary = summarize(article.text)
    return {"summary": summary}
