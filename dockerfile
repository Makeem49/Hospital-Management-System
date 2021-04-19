FROM python:3.7.5-slim-buster
MAINTAINER Moshood Akeem Olayinka <makeemtech@gmail.com>

ENV INSTALL_PATH /hms
RUN mkdir -p $INSTALL_PATH

COPY requirements.txt requirements.txt 
RUN pip install -r requirements.txt 

COPY . .
# RUN pip install -editable .

CMD gunicorn -b 0.0.0.0:7000 --access-logfile - "snakeeyes.app:create_app()"