import pika
url = "amqp://localhost:5672"
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='hello')


def callback(ch, method, properties, body):
    print(str(body))


channel.basic_consume('hello', callback, auto_ack=True)
channel.start_consuming()
connection.close()
