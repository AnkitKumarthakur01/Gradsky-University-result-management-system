from kafka import KafkaProducer
import json

# Kafka producer configuration for student feedback
producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

# Sample student feedback
feedback_data = {
    "student_id": 101,
    "feedback": "I am satisfied with my results!"
}

# Sending feedback to Kafka
topic = "student_feedback"
print(f"Sending student feedback to Kafka topic: {topic}")
producer.send(topic, feedback_data)

# Flush and close producer
producer.flush()
print("Student feedback successfully sent!")