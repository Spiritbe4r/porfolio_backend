# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.9

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

WORKDIR /myportfolio
COPY . /myportfolio

RUN pip install pip --upgrade && \
    pip install -r requirements.txt 
