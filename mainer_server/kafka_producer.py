from confluent_kafka import Producer
import json
from create_response import create_response

def delivery_report(err, msg):
    """ Called once for each message produced to indicate delivery result.
        Triggered by poll() or flush(). """
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

# Set up Kafka configuration
conf = {
    'bootstrap.servers': '34.125.37.209:9092',  # Replace with your broker's IP and port
    'client.id': 'python-producer'
}

# Create Producer instance
p = Producer(**conf)

data = create_response()
json_data = json.dumps(data)
p.produce('test', value=json_data, callback=delivery_report)

# Wait for any outstanding messages to be delivered and delivery reports to be received.
p.flush()