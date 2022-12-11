# Dockerfiel, Image, Container
FROM python:3.9-alpine

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

# ENTRYPOINT FLASK_APP=/main.py flask run --host=0.0.0.0 --port=8080

# CMD ["python", "./main.py"]

ENTRYPOINT [ "python" ]

CMD ["view.py" ]