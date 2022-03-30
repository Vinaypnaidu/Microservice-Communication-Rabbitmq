# Dockerfile for ride matching consumer

# FROM ubuntu:18.04

# RUN apt-get update -y && \
#     apt-get install -y python3-pip python3-dev

# COPY . /rmconsumer

# RUN pip3 install pika && \
#     pip3 install -r /rmconsumer/requirements.txt

# CMD [ "python3", "/rmconsumer/ride_matching_consumer.py" ]

FROM ubuntu:18.04

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev

COPY ./requirements.txt /rmconsumer/requirements.txt

WORKDIR /rmconsumer

RUN pip3 install pika && \
    pip3 install -r requirements.txt

COPY . /rmconsumer

ENTRYPOINT [ "python3" ]

CMD [ "ride_matching_consumer.py" ]