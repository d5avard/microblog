import pika

# connection = None
# channel = None

# def open():
#     credentials = pika.PlainCredentials('guest', 'guest')
#     connection = pika.BlockingConnection(
#         pika.ConnectionParameters('microblog-message-broker-1', 5672, '/', credentials))
#     channel = connection.channel()
#     channel.queue_declare(queue='post')

# def publish(str):
#     channel.basic_publish(exchange='', routing_key='post', body=str)    
#     print(" [post] Sent '{str}'")

# def close():
#     connection.close()
    
# open()
# publish('message')
# close()

#!/usr/bin/env python
import pika

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(
    pika.ConnectionParameters('microblog-message-broker-1', 5672, '/', credentials))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()