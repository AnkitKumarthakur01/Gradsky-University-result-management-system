
---

# *🎓 GradsKey: University Result Management System*  

### *📌 An end-to-end Big Data project to manage student results using Spark, Hadoop, Kafka, and NoSQL.*  

![Big Data Workflow](https://miro.medium.com/max/1400/1*-aAOM6S-69UKOrCPqYehAA.png)  

---

## *📖 Table of Contents*
- [🔍 Overview](#-overview)
- [🚀 Features](#-features)
- [🛠 Technologies Used](#-technologies-used)
- [⚙ Architecture Diagram](#-architecture-diagram)
- [📂 Project Structure](#-project-structure)
- [🔧 Setup & Installation](#-setup--installation)
- [📊 Running the Project](#-running-the-project)
- [📜 Sample Outputs](#-sample-outputs)
- [📢 Future Enhancements](#-future-enhancements)
- [📩 Contact](#-contact)

---

## *🔍 Overview*
The *GradsKey Result Management System* is designed to handle large-scale student data efficiently.  
It utilizes *Big Data technologies* to:
- *Process* student marks using Spark & Hadoop  
- *Stream* results to the Head of Department (HoD) via Kafka  
- *Store* feedback in a NoSQL database  
- *Analyze* student feedback sentiment using Machine Learning  
- *Visualize* statistics on a *Flask Dashboard*  

---

## *🚀 Features*
✅ *Generate & Process Student Marks* – 10,000 students, 6 subjects  
✅ *Apache Spark & MapReduce* – Perform statistical analysis on marks  
✅ *Real-time Streaming with Kafka* – Send results to HoD dynamically  
✅ *NoSQL Database (MongoDB/Cassandra)* – Store student feedback  
✅ *Sentiment Analysis* – Classify feedback as *Positive* or *Negative*  
✅ *Flask Dashboard* – Interactive UI for result analysis  

---

## *🛠 Technologies Used*
| Technology      | Purpose |
|---------------|--------------------------------|
| *Apache Hadoop* | Distributed storage (HDFS) & processing (MapReduce) |
| *Apache Spark* | Fast processing of student marks |
| *Apache Kafka* | Real-time streaming of results |
| *MongoDB / Cassandra* | NoSQL storage for student feedback |
| *Python* | Core programming language |
| *Flask / Streamlit* | Web-based dashboard |
| *TextBlob / NLTK* | Sentiment analysis for feedback |

---

## *⚙ Architecture Diagram*
Below is a *high-level architecture* of how the system works:  


+-----------------+     +----------------+     +----------------+     +------------------+
| Student Data    | --> | Spark Processing | --> | Kafka Producer | --> | HoD (Consumer)  |
| (CSV/Database)  |     | (Compute Stats)  |     | (Send Results) |     | (Receives Stats)|
+-----------------+     +----------------+     +----------------+     +------------------+
         |                                                          |
         |                                                          v
         |                                             +----------------------+
         |                                             | Students (View Marks) |
         |                                             | + Give Feedback       |
         |                                             +----------------------+
         |
         v
+----------------+       +--------------+       +----------------------+
| Hadoop HDFS    | <-->  | NoSQL DB      | <-->  | ML Sentiment Analysis |
| (Raw Data)     |       | (Feedback)    |       | (Analyze Responses)   |
+----------------+       +--------------+       +----------------------+



---

## *📂 Project Structure*

result-management-system/
│── data/
│   ├── generate_students.py  # Generate random student data
│
│── hadoop_spark_processing/
│   ├── marks_processing.py    # Spark processing script
│   ├── mapreduce_analysis.py  # Hadoop MapReduce processing
│
│── kafka_streaming/
│   ├── producer.py            # Kafka producer for results
│   ├── consumer.py            # Kafka consumer for HoD
│   ├── student_feedback_producer.py  # Kafka feedback producer
│   ├── student_feedback_consumer.py  # Kafka feedback consumer
│
│── nosql_feedback/
│   ├── store_feedback.py      # Store feedback in MongoDB/Cassandra
│   ├── analyze_feedback.py    # Perform sentiment analysis
│
│── dashboard/
│   ├── app.py                 # Flask dashboard to visualize results
│   ├── templates/
│       ├── index.html          # Dashboard UI
│
│── README.md                   # Project documentation
│── requirements.txt             # Dependencies
│── setup.sh                     # Setup script


---

## *🔧 Setup & Installation*
### *1️⃣ Install Required Dependencies*
sh
chmod +x setup.sh
./setup.sh


### *2️⃣ Start Kafka & Zookeeper*
sh
zookeeper-server-start.sh config/zookeeper.properties
kafka-server-start.sh config/server.properties


### *3️⃣ Create Kafka Topics*
sh
kafka-topics.sh --create --topic student_results --bootstrap-server localhost:9092
kafka-topics.sh --create --topic student_feedback --bootstrap-server localhost:9092


---

## *📊 Running the Project*
### *1️⃣ Generate Student Data*
sh
python data/generate_students.py


### *2️⃣ Process Marks with Spark*
sh
python hadoop_spark_processing/marks_processing.py


### *3️⃣ Run MapReduce Analysis*
sh
python hadoop_spark_processing/mapreduce_analysis.py data/student_marks.csv


### *4️⃣ Start Kafka Producer & Consumer*
sh
python kafka_streaming/producer.py  # Send results
python kafka_streaming/consumer.py  # HoD receives results


### *5️⃣ Start Feedback System*
sh
python kafka_streaming/student_feedback_producer.py  # Send feedback
python kafka_streaming/student_feedback_consumer.py  # Receive feedback


### *6️⃣ Run Sentiment Analysis*
sh
python nosql_feedback/analyze_feedback.py


### *7️⃣ Start Flask Dashboard*
sh
python dashboard/app.py


---

## *📜 Sample Outputs*
### *📌 Kafka Consumer Receiving Student Results*

Received Student Statistics: {'average_electronics': 75, 'max_programming': 98, 'min_database': 35, 'total_students': 10000}


### *📌 Kafka Consumer Receiving Student Feedback*

Received Feedback: {'student_id': 101, 'feedback': 'I am satisfied with my results!'}


### *📌 Sentiment Analysis Output*

Feedback: "I am satisfied with my results!" | Sentiment: Positive


---

## *📢 Future Enhancements*
🔹 Add *AI-powered feedback summarization*  
🔹 Implement *Distributed Database Sharding*  
🔹 Integrate *Realtime Result Notification System*  
🔹 Enhance *Dashboard UI with Data Visualization*  

---

## *📩 Contact*
💡 If you have any suggestions or issues, feel free to *raise an issue* or *contribute* to this project!  
🚀 Happy Learning & Coding!  

---
