from kafka import KafkaProducer
import json
def prod(topicName,d):
    servers=["localhost:9092"]
    topicName=topicName
    producer=KafkaProducer(bootstrap_servers=servers)

    arrJson=json.dumps(d)
    arrBytes=bytearray(arrJson, 'utf-8')
    producer.send(topicName, arrBytes)
    producer.flush()