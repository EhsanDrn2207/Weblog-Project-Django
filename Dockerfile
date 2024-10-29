FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE 1 
ENV PYTHONBUFFERD 1


WORKDIR /code

COPY requirments.txt /code/
RUN pip install -r requirments.txt

COPY . /code/
