.DEFAULT_GOAL := run-dev

run-dev: clean
	docker compose -f docker-compose.yml -f docker-compose.devcontainer.yml up -d --no-deps --build
	
run-prod: clean
	docker compose up -d --no-deps --build -f docker-compose.yml

stop:
	docker compose down

clean:
	find . -name __pycache__ -type d -exec rm -dR {} +