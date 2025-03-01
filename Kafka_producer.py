from kafka import KafkaProducer
import json
import time

# Kafka producer configuration
producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

# Sample statistics to send
stats = {
    "average_electronics": 75,
    "max_programming": 98,
    "min_database": 35,
    "total_students": 10000
}

# Sending the message to the Kafka topic
topic = "student_results"
print(f"Sending statistics to Kafka topic: {topic}")
producer.send(topic, stats)

# Flush and close producer
producer.flush()
time.sleep(2)
print("Statistics successfully sent!")