FROM ubuntu:latest
USER root
COPY . .

RUN apt-get -y update &&  \
    apt-get install -y python && \
    apt-get install -y python-pip && \
    apt-get install  -y virtualenv && \
    virtualenv piaibot && \
    piaibot="piaibot/bin/activate" && \
    pip install python-telegram-bot
#add new bot
CMD [ "python", "main.py"]
