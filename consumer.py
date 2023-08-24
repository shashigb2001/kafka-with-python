from kafka import KafkaConsumer
import json

consumer = KafkaConsumer('order_details', bootstrap_servers='localhost:29092')

while True:
    for message in consumer:
        print("Here is a message..")
        print(json.loads(message.value))
