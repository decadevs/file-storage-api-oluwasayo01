FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1
WORKDIR myapp/
COPY . .

RUN pip install -r requirements.txt

CMD python manage.py runserver 0.0.0.0:8000