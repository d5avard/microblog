from fastapi import APIRouter, HTTPException
from models.posts import Post
from database.database import (
    fetch_one_post,
    fetch_all_posts,
    create_post,
    remove_post
)

post_router = APIRouter()

@post_router.get("/")
async def get_todo():
    response = await fetch_all_posts()
    if response:
        return response
    raise HTTPException(400, "Something went wrong")

@post_router.get("/{text}", response_model=Post)
async def get_todo_by_title(text):
    response = await fetch_one_post(text)
    if response:
        return response
    raise HTTPException(404, f"There is no post with the text {text}")

@post_router.post("/", response_model=Post)
async def post(post: Post):
    response = await create_post(post.dict())
    if response:
        return response
    raise HTTPException(400, "Something went wrong")

@post_router.delete("/{text}")
async def delete_post(text):
    response = await remove_post(text)
    if response:
        return "Successfully deleted post"
    raise HTTPException(404, f"There is no post with the text {text}")