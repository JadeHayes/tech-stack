FROM python:3.6-slim

EXPOSE 8080
ENV FLASK_APP=__init__.py
ENV FLASK_DEBUG=1

RUN mkdir /app
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY routes /app/routes
COPY . /app/
COPY __init__.py /app/__init__.py

CMD ["flask", "run", "-h", "0.0.0.0", "-p 8080"]
