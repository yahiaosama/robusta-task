FROM ubuntu:16.04

RUN apt-get update -y && \
    apt-get install -y software-properties-common


RUN apt-get update -y && \
    add-apt-repository ppa:deadsnakes/ppa

RUN apt-get update -y && \
    apt-get install -y python3.7 python3.7-dev python3-pip  

RUN mkdir -p /usr/src/robusta-task

RUN export PATH=${PATH}:/usr/bin/python3.7/bin

RUN python3.7 -m pip install pip

WORKDIR /usr/src/robusta-task

COPY ./requirements.txt /usr/src/robusta-task/requirements.txt

COPY . /usr/src/robusta-task


RUN python3.7 -m pip install -r requirements.txt

ENTRYPOINT ["python3.7"]

CMD ["cli_application.py"]
