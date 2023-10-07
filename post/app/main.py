from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from contextlib import asynccontextmanager
from starlette.background import BackgroundTask
import httpx
import socket
from mb import MessageBroker

class Post(BaseModel):
    post: str
    user: str
    text: str

@asynccontextmanager
async def lifespan(app: FastAPI):
    client = httpx.AsyncClient(base_url='http://microblog-entry-store-1:8080')
    app.state.client = client
    app.state.mb = MessageBroker()
    app.state.mb.open()
    yield
    client = app.state.client
    await client.aclose()
    app.state.mb.close()

app = FastAPI(lifespan=lifespan)

async def _proxy(request: Request):
    client = request.app.state.client
    url = httpx.URL(path=request.url.path, query=request.url.query.encode('utf-8'))
    req = client.build_request(
        request.method, url, headers=request.headers.raw, content=request.stream()
    )
    r = await client.send(req, stream=True)
    return StreamingResponse(
        r.aiter_raw(),
        status_code=r.status_code,
        headers=r.headers,
        background=BackgroundTask(r.aclose)
    )

@app.get('/')
def root():
	return "success"

@app.get('/info')
def info(request: Request):

	resp = {
		'connecting_ip': request.headers['X-Real-IP'],
		'proxy_ip': request.headers['X-Forwarded-For'],
		'host': request.headers['Host'],
		'containe_id': socket.gethostname(),
		'user-agent': request.headers['User-Agent']
	}

	return resp

@app.post('/')
async def post_message(request: Request):
    client = request.app.state.client
    url = httpx.URL(path=request.url.path, query=request.url.query.encode('utf-8'))
    req = client.build_request(
        request.method, url, headers=request.headers.raw, content=request.stream()
    )
    r = await client.send(req, stream=True)
    if (r.status_code == 200):
        app.state.mb.publish("a message")
    return StreamingResponse(
        r.aiter_raw(),
        status_code=r.status_code,
        headers=r.headers,
        background=BackgroundTask(r.aclose)
    )
    

@app.get('/health-check')
def flask_health_check():
	return "success"

app.add_route('/{path:path}', _proxy, ['POST'])
