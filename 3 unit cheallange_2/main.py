def sort_students(students):
    sorted_students = sorted(students, key=lambda x: x.cgpa, reverse=True)
    return sorted_students
class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

# Sample students
students = [
    Student("John Doe", "2021001", 3.8),
    Student("Jane Doe", "2021002", 3.5),
    Student("Bob Smith", "2021003", 3.7),
    Student("Alice Johnson", "2021004", 4.0),
]

# Sorting students by CGPA
sorted_students = sort_students(students)

# Printing sorted students
for student in sorted_students:
    print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")
