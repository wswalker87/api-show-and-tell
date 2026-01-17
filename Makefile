# Run reset
reset:
	docker-compose down -v
	docker-compose up -d --build
	docker-compose logs -f

# Run migrations
migrate:
	python manage.py migrate --fake-initial

# Optional: Combine reset and migrate into one command
full-reset: reset
	@echo "Waiting 5 seconds for Docker Postgres to start..."
	@sleep 5
	python manage.py migrate