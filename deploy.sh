sudo docker-compose stop
sudo docker system prune -a -f
sudo docker-compose build
sudo docker-compose up -d
sudo docker-compose exec web python manage.py migrate --noinput
sudo docker-compose exec web python manage.py collectstatic --noinput