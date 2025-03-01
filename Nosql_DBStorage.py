from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["university"]
collection = db["feedback"]

# Store feedback
feedback = {"student_id": 1, "feedback": "I am happy with the results!"}
collection.insert_one(feedback)

print("Feedback stored successfully!")