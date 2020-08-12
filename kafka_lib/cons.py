from kafka import KafkaConsumer
import json
def cons(topicName):
    servers=["localhost:9092"]
    topicName=topicName
    consumer=KafkaConsumer(topicName, group_id="user5", bootstrap_servers=servers, auto_offset_reset="earliest"
    )
    for msg in consumer:
    data=json.loads(msg.value)
    print(data)