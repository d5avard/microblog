# microblog

## first iteration - initialize front
First iteration setups a docker network with an container application. The setup works with docker compose and with dev container approach in vscode.

To launch the setup with dev container approach type shift + command + p Dev , type **Containers: Open Folder in Container** and select the folder that contains the application.

See references:
- https://code.visualstudio.com/remote/advancedcontainers/connect-multiple-containers
- https://fastapi.tiangolo.com/deployment/docker/

## second iteration - initialize post
Second iteration setups a new docker network for the services and initialize the new service post. 

## third iteration - setup dev
Third iteration setups multiple devcontainers, use python slim package, update versions of FastApi stack and create a first version of Makefile.

## fouth iteration - add nginx load blancer
Fouth iteration setups an nginx load balancer and add a new endpoint 'info' in the front service.

## fifth iteration - add post service
Add post service.

## sixth iteration - add a first route
Add a new route, a post message '/' that route trough front->post->entry-store.

A test example:
```bash
curl -H "Content-Type: application/json" \
    --request POST \
    -d '{"post":"entry","user":"alice", "text":"curiouser and couriouser"}' \
    http://localhost/
```
## seventh iteration - add a bd and create a first entry
Develop entry-store, now we can create a post entry. Add new network for the database, add .env file and environment variables.
