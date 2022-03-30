# Dockerfile for Producer 

# FROM ubuntu:18.04

# RUN apt-get update -y && \
#     apt-get install -y python3-pip python3-dev

# COPY ./requirements.txt /producer/requirements.txt

# WORKDIR /producer

# RUN pip3 install pika && \
#     pip3 install -r requirements.txt

# COPY . /producer

# # ENTRYPOINT [ "python3" ]

# CMD [ "python3", "producer.py" ]

# EXPOSE 6000

FROM ubuntu:18.04

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev

COPY ./requirements.txt /producer/requirements.txt

WORKDIR /producer

RUN pip3 install pika && \
    pip3 install -r requirements.txt

COPY . /producer

ENTRYPOINT [ "python3" ]

CMD [ "producer.py" ]