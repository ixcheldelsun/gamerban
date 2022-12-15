migrate: 
	echo "Making migrations..."
	docker-compose run --rm gamerban python manage.py makemigrations
	echo "Migrating..."
	docker-compose run --rm gamerban python manage.py migrate

run_api: 
	echo "Running API..."
	docker-compose run --rm --service-ports gamerban python manage.py runserver 0.0.0.0:8000