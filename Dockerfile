FROM python:3.9

RUN mkdir /myportfolio

WORKDIR /myportfolio

COPY . /myportfolio/

RUN pip install -r requirements.txt