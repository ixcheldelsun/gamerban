migrate: 
	echo "Making migrations..."
	docker-compose run --rm gamerban python manage.py makemigrations
	echo "Migrating..."
	docker-compose run --rm gamerban python manage.py migrate