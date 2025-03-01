from textblob import TextBlob
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["university"]
collection = db["feedback"]

for feedback in collection.find():
    analysis = TextBlob(feedback["feedback"])
    sentiment = "Positive" if analysis.sentiment.polarity > 0 else "Negative"
    print(f"Feedback: {feedback['feedback']} | Sentiment: {sentiment}")