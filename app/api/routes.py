from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from openai import OpenAI
from app.core.retriever import retrieve

router = APIRouter()
client = OpenAI()              # reads OPENAI_API_KEY from env

class AskRequest(BaseModel):
    question: str

@router.post("/ask")
async def ask(data: AskRequest):
    ctx = retrieve(data.question)
    prompt = (
        "You are a helpful assistant. "
        "Use ONLY the context below. "
        "If context is insufficient, say you don't know.\n\n"
        f"Context:\n{ctx}\n\nQuestion: {data.question}\nAnswer:"
    )
    try:
        res = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
        )
        return {"answer": res.choices[0].message.content.strip()}
    except Exception as e:
        raise HTTPException(500, str(e))
