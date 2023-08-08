from pydantic import BaseModel

class Post(BaseModel):
    post: str
    user: str
    text: str