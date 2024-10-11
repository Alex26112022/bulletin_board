### Создайте файл .env в корне проекта и заполните его по шаблону .env.sample
### Создайте БД с необходимыми настройками и установите зависимости (requirements.txt)
### Варианты запуска проекта локально:
1. Без запуска контейнера:
   - в файле .env -> ENV_TYPE=local
   - python manage.py migrate
   - python manage.py runserver
   - python manage.py csu # создание суперпользователя
2. С помощью Docker:
   - docker-compose build
   - docker-compose up -d
   - docker-compose exec web python manage.py migrate --noinput
   - docker-compose exec web python manage.py collectstatic --noinput
   - docker-compose exec web python manage.py csu # создание суперпользователя
### Запуск тестов:
   - pytest
   - pytest --cov # посмотреть покрытие
   - pytest --cov-report term-missing # сгенерировать отсчет в терминал
   - pytest --cov-report=html # сгенерировать отчет о покрытии в HTML-формате