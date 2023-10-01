.DEFAULT_GOAL := run-dev

run: clean
	docker compose -f docker-compose.yml -f docker-compose.devcontainer.yml up -d --no-deps --build
	
stop:
	docker compose -f docker-compose.yml -f docker-compose.devcontainer.yml down --rmi 'local'

clean:
	find . -name __pycache__ -type d -exec rm -dR {} +