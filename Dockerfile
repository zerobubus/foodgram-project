FROM python:3.8.5


WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD gunicorn foodgram.wsgi:application --bind 0.0.0.0:8000
