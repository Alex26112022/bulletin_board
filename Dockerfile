FROM python:latest

LABEL authors="Алексей Денисенко"
LABEL org.opencontainers.image.authors="AlexeyDenisenko2703@yandex.ru"

RUN mkdir -p /home/app

ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/static
RUN mkdir $APP_HOME/media
WORKDIR $APP_HOME

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY requirements.txt ./
RUN pip install --no-cache --default-timeout=100 -r requirements.txt

COPY . .

RUN addgroup app
RUN useradd -g app app
RUN chown -R app:app $APP_HOME
USER app

#CMD ["sh", "-c", "python manage.py migrate --noinput && python manage.py collectstatic --noinput && python manage.py runserver 0.0.0.0:8000"]