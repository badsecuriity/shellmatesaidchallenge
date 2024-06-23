FROM python:3.8-slim-buster

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev curl

WORKDIR /app
COPY ./app .
RUN pip3 install -r requirements.txt

RUN chmod -R 555 /app

CMD [ "python3","app.py" ]
