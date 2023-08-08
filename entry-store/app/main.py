from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.database import (
    fetch_one_post,
    fetch_all_posts,
    create_post,
    # update_post,
    remove_post
)
from app.model import Post

app = FastAPI()

@app.get("/ping")
def ping():
    return {"ping": "pong"}
    
@app.get("/")
async def get_todo():
    response = await fetch_all_posts()
    if response:
        return response
    raise HTTPException(400, "Something went wrong")

@app.get("/{text}", response_model=Post)
async def get_todo_by_title(text):
    response = await fetch_one_post(text)
    if response:
        return response
    raise HTTPException(404, f"There is no post with the text {text}")

@app.post("/", response_model=Post)
async def post(post: Post):
    response = await create_post(post.dict())
    if response:
        return response
    raise HTTPException(400, "Something went wrong")

@app.delete("/{text}")
async def delete_post(text):
    response = await remove_post(text)
    if response:
        return "Successfully deleted post"
    raise HTTPException(404, f"There is no post with the text {text}")