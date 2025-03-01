from kafka import KafkaConsumer
import json

# Kafka consumer configuration
consumer = KafkaConsumer(
    "student_results",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    value_deserializer=lambda v: json.loads(v.decode("utf-8"))
)

print("Waiting for student results data...")

# Consuming messages from Kafka
for message in consumer:
    print(f"Received Student Statistics: {message.value}")