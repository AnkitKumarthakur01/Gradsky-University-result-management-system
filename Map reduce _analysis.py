from mrjob.job import MRJob

class MarksAnalysis(MRJob):
    def mapper(self, _, line):
        fields = line.split(',')
        if fields[0] != "student_id":  # Skip header
            for i in range(1, 7):  # 6 subjects
                yield fields[i], int(fields[i + 1])

    def reducer(self, subject, marks):
        marks_list = list(marks)
        yield subject, {
            "average": sum(marks_list) / len(marks_list),
            "max": max(marks_list),
            "min": min(marks_list)
        }

if _name_ == "_main_":
    MarksAnalysis.run()