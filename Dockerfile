FROM python:3.12

LABEL maintainer="JamariusTaylor"

WORKDIR /main

COPY requirements.txt /main/requirements.txt

RUN mkdir app

WORKDIR /app

COPY app.py /app

RUN pip install --no-cache-dir --upgrade -r /main/requirements.txt

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]