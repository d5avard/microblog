
import pika

connection = None
channel = None

class MessageBroker:
    
    def open(self):
        credentials = pika.PlainCredentials('guest', 'guest')
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters('microblog-message-broker-1', 5672, '/', credentials))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='post')

    def publish(self, str):
        self.channel.basic_publish(exchange='', routing_key='post', body=str)    
        print(" [post] Sent '{str}'")

    def close(self):
        self.connection.close()