from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/ping")
def ping():
    return {"ping": "pong"}

# {
# 	post: 'entry',
# 	user: 'alice',
# 	text: 'curiouser and couriouser'
# }
class Post(BaseModel):
    post: str
    user: str
    text: str
    
@app.post('/')
def post_entry(entry:Post):
    return entry