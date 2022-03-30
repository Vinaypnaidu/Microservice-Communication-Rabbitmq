# Dockerfile for database consumer

# Dockerfile for ride matching consumer

# FROM ubuntu:18.04

# RUN apt-get update -y && \
#     apt-get install -y python3-pip python3-dev

# COPY . /dbconsumer

# RUN pip3 install pika && \
#     pip3 install -r /dbconsumer/requirements.txt

# CMD [ "python3", "/dbconsumer/database_consumer.py" ]

# Dockerfile for database consumer

FROM ubuntu:18.04

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev

COPY ./requirements.txt /dbconsumer/requirements.txt

WORKDIR /dbconsumer

RUN pip3 install pika && \
    pip3 install -r requirements.txt

COPY . /dbconsumer

ENTRYPOINT [ "python3" ]

CMD [ "database_consumer.py" ]