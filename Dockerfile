FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /coding-challenge
COPY requirements.txt requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
COPY . /coding-challenge
EXPOSE 8000