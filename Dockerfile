FROM python:3.9

RUN mkdir /myportfolio

WORKDIR /myportfolio

COPY . /myportfolio/

RUN pip install pip --upgrade && \
    pip install -r requirements.txt 

# FROM python:3.9

# # copy your local files to your
# # docker container
# COPY . /app

# # update your environment to work
# # within the folder you copied your 
# # files above into
# WORKDIR /app

# # /opt: reserved for the installation of add-on application software packages.
# # We'll use this to create & store our virtual environment

# # Create a virtual environment in /opt
# RUN python3 -m venv /opt/venv

# # Install requirments to new virtual environment
# # requirements.txt must have gunicorn & django

# RUN /opt/venv/bin/pip install pip --upgrade && \
#     /opt/venv/bin/pip install -r requirements.txt 
    #&& \ chmod +x entrypoint.sh

# entrypoint.sh will be discussed later.
# CMD [ "/app/entrypoint.sh" ]



# FROM python:3.9

# RUN mkdir /myportfolio

# WORKDIR /myportfolio

# COPY . /myportfolio/

# RUN pip install -r requirements.txt