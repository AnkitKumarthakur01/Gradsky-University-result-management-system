from kafka import KafkaConsumer
import json

# Kafka consumer configuration for student feedback
consumer = KafkaConsumer(
    "student_feedback",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    value_deserializer=lambda v: json.loads(v.decode("utf-8"))
)

print("Waiting for student feedback...")

# Consuming messages from Kafka
for message in consumer:
    print(f"Received Feedback: {message.value}")