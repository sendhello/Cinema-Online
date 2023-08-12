from kafka import KafkaProducer
from time import sleep


producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

future = producer.send(
    topic='views',
    value=b'1611039931',
    key=b'500271+tt0120338',
)
print(f"{future=}")

sleep(1)



from kafka import KafkaConsumer


consumer = KafkaConsumer(
    'views',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    group_id='echo-messages-to-stdout',
)

for message in consumer:
    print(f"{message.value=}")
