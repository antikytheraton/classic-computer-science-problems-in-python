FROM python:3.7
ENV PYTHONUNBUFFERED 1
WORKDIR /code
COPY requirements.txt .
RUN pip install --upgrade pip;\
    pip install -r requirements.txt
