# 1, 4
print("Q-1, 4")
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_status(self):
        return "PASS" if self.score >= 70 else "FAIL"



student_1 = Student("Harry Potter", 90)
student_2 = Student("Hermione Granger", 95)
student_3 = Student("Ron Weasley", 90)
student_4 = Student("Emma", 60)
student_5 = Student("John", 50)
student_6 = Student("Bob", 40)


# 2
print("\nQ-2")
all_students = [student_1, student_2, student_3, student_4, student_5, student_6]
print(f"Total students : {len(all_students)}")

# 3
print("\nQ-3")
for student in all_students:
    print(f"Student Name : {student.name}\nScore : {student.score}\n")


# 5
print("\nQ-5")
for student in all_students:
    print(f"Student Name : {student.name}\nScore Status : {student.get_status()}\n")


# 6
print("\nQ-6")
students_with_high_score = [student for student in all_students if student.get_status() == "PASS"]
for student in students_with_high_score:
    print(f"Student Name : {student.name}\nScore : {student.score}\n")

