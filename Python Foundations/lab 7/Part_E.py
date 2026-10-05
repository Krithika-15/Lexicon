# 1
print("Q-1")
class Teacher:
    def __init__(self, name):
        self.name = name

instructor_1 = Teacher("John")

# 2
print("\nQ-2, 3, 4, 5, 6, 7")
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

class Course:
    def __init__(self, course_name, teacher):
        self.course_name = course_name
        self.teacher = teacher
        self.students = []

    def add_student(self,student):
        self.students.append(student)

coursedata_1 = Course("Python",instructor_1)
coursedata_2 = Course("SQL",instructor_1)

student_1 = Student("harry", 90)
student_2 = Student("emma", 80)
student_3 = Student("ron", 60)

coursedata_1.add_student(student_1)
coursedata_1.add_student(student_2)
coursedata_1.add_student(student_3)
coursedata_2.add_student(student_2)
coursedata_2.add_student(student_3)

for course in [coursedata_1, coursedata_2]:
    print()
    print(f"Course Name : {course.course_name}\nTeacher : {course.teacher.name}")
    for student in course.students:
        print(f"Student Name : {student.name}\nScore : {student.score}")
