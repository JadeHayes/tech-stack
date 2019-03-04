FROM python:3.6-slim

EXPOSE 5000
ENV FLASK_APP=__init__.py
ENV FLASK_DEBUG=1

RUN mkdir /app
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY server.py /app/server.py
COPY . /app/
COPY __init__.py /app/__init__.py

CMD ["flask", "run", "-h", "0.0.0.0", "-p 5000"]