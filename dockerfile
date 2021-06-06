FROM python:3.7.5-slim-buster
MAINTAINER Moshood Akeem <Makeemtech@gmail.com.com>

RUN apt-get update && apt-get install -qq -y \
  build-essential libpq-dev --no-install-recommends


ENV INSTALL_PATH /hms
RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

RUN pip install --upgrade pip

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
RUN pip install --editable .

CMD gunicorn -b 0.0.0.0:7000 --access-logfile - "hms.app:create_app()"
