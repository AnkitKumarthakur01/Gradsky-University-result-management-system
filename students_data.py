import pandas as pd
import random
from faker import Faker

fake = Faker()

# Generate student profiles
num_students = 10000
students = [{"student_id": i, "name": fake.name(), "age": random.randint(18, 25)} for i in range(1, num_students + 1)]

# Subjects
subjects = ["Electronics", "Programming", "Database", "Data Science", "Mathematics", "DSA"]

# Generate marks
marks = [{"student_id": i, **{sub: random.randint(30, 100) for sub in subjects}} for i in range(1, num_students + 1)]

# Save data
pd.DataFrame(students).to_csv("data/student_profiles.csv", index=False)
pd.DataFrame(marks).to_csv("data/student_marks.csv", index=False)

print("Student data generated successfully!")