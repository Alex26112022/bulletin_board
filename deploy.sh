docker-compose stop
docker system prune -a -f
docker-compose build
docker-compose up -d
docker-compose exec web python manage.py migrate --noinput
docker-compose web python manage.py collectstatic --noinput