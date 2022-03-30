# Use this file to setup the database consumer that stores the ride information in the database

import json
import pika
from pymongo import MongoClient
import time

time.sleep(10)

client = MongoClient()

client = MongoClient("mongodb://mongodb")

# Access database
mydatabase = client['database']

# Access collection of the database
mycollection = mydatabase["ridetable"]

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="rabbitmq"))
    channel = connection.channel()
    channel.queue_declare(queue='database')

    def callback(ch, method, properties, body):
        ride = json.loads(body.decode('utf-8'))
        sleeptime = ride['time']
        rec = mydatabase.myTable.insert_one(ride)
        for i in mydatabase.myTable.find():
            print(i)

    channel.basic_consume(queue = 'database', on_message_callback = callback, auto_ack = True)

    print('Database consumer is up and running')
    channel.start_consuming()

if __name__ == '__main__':
    main()