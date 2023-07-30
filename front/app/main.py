from fastapi import FastAPI, Request
import socket

app = FastAPI()

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

@app.get('/health-check')
def flask_health_check():
	return "success"