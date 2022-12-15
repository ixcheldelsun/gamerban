migrate: 
	echo "Making migrations..."
	do'cker-compose run --rm gamerban python manage.py makemigrations
	echo "Migrating..."
	docker-compose run --rm gamerban python manage.py migrate

run_api: 
	echo "Running API..."
	docker-compose run --rm --service-ports gamerban python manage.py runserver 0.0.0.0:8000

pytest: 
	echo "Running tests..."
	docker-compose run --rm gamerban pytest

deploy:
	docker-compose -f docker-compose.yml -f docker-compose.prod.yml up --build
