from fastapi import FastAPI
from routes.posts import post_router
class App(FastAPI):
    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs)

app = App()
app.include_router(post_router)

@app.get("/ping")
def ping():
    return {"ping": "pong"}
