import os
from dotenv import load_dotenv
import pika
from pika.exceptions import AMQPConnectionError

# Load environment variables from .env file
load_dotenv()

# RabbitMQ connection parameters
RABBITMQ_HOST = os.getenv('RABBITMQ_HOST')
RABBITMQ_PORT = int(os.getenv('RABBITMQ_PORT', 5672))
RABBITMQ_USER = os.getenv('RABBITMQ_USER')
RABBITMQ_PASSWORD = os.getenv('RABBITMQ_PASSWORD')

def get_rabbitmq_connection():
    """
    Establishes connection to RabbitMQ server and returns the connection object.
    """
    credentials = pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASSWORD)
    parameters = pika.ConnectionParameters(host=RABBITMQ_HOST, port=RABBITMQ_PORT, credentials=credentials)
    try:
        return pika.BlockingConnection(parameters)
    except AMQPConnectionError:
        print("Failed to connect to RabbitMQ.")
        return None

def send_message(queue_name, message):
    """
    Sends a message to the specified RabbitMQ queue.
    """
    connection = get_rabbitmq_connection()
    if connection is not None:
        channel = connection.channel()
        channel.queue_declare(queue=queue_name, durable=True)
        channel.basic_publish(exchange='', routing_key=queue_name, body=message)
        print(f"Sent '{message}' to queue '{queue_name}'")
        connection.close()

def listen_queue(queue_name, callback):
    """
    Listens to the specified RabbitMQ queue and processes messages using the provided callback function.
    """
    connection = get_rabbitmq_connection()
    if connection is not None:
        channel = connection.channel()
        channel.queue_declare(queue=queue_name, durable=True)

        def on_message_callback(ch, method, properties, body):
            callback(body)
            ch.basic_ack(delivery_tag=method.delivery_tag)

        channel.basic_qos(prefetch_count=1)
        channel.basic_consume(queue=queue_name, on_message_callback=on_message_callback)
        print(f"Listening on queue '{queue_name}'. To exit press CTRL+C")
        try:
            channel.start_consuming()
        except KeyboardInterrupt:
            channel.stop_consuming()
        finally:
            connection.close()
