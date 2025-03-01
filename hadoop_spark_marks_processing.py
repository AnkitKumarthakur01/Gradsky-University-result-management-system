from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, max, min

# Initialize Spark session
spark = SparkSession.builder.appName("StudentMarksProcessing").getOrCreate()

# Load data
df = spark.read.csv("data/student_marks.csv", header=True, inferSchema=True)

# Compute statistics
stats_df = df.select(
    avg("Electronics").alias("avg_electronics"),
    max("Programming").alias("max_programming"),
    min("Database").alias("min_database")
)

# Show statistics
stats_df.show()

# Save processed results
stats_df.write.csv("output/processed_results.csv", header=True)
print("Marks processing completed and saved.")