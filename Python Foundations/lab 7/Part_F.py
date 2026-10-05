class Teacher:
    def __init__(self, name):
        self.name = name


class Student:
    def __init__(self, name, score):
        self.name = name
        if score < 0 or score > 100:
            raise ValueError(f"Score must be between 0 and 100, got {score}")
        self.score = score

    def get_status(self):
        return "PASS" if self.score >= 70 else "FAIL"


class Course:
    def __init__(self, course_name, teacher):
        self.course_name = course_name
        self.teacher = teacher
        self.students = []

    def add_student(self,student):
        self.students.append(student)

    def student_count(self):
        return len(self.students)

    def passed_students(self):
        return [student for student in self.students if student.get_status() == "PASS"]


student_1 = Student("Harry", 85)
student_2 = Student("Hermione", 90)
student_3 = Student("Ron", 95)
student_4 = Student("Emma", 60)
student_5 = Student("Grace", 50)
student_6 = Student("Alice", 85)

try:
    student7 = Student("Emily", -1)
except ValueError as e:
    print(f"Error : {e}")

try:
    student8 = Student("Emily", 101)
except ValueError as e:
    print(f"Error : {e}")

teacher_1 = Teacher("John")
teacher_2 = Teacher("Bob")

course_1 = Course("Python", teacher_1)
course_2 = Course("SQL", teacher_1)
course_3 = Course("Java", teacher_2)

course_1.add_student(student_1)
course_1.add_student(student_2)
course_1.add_student(student_3)
course_1.add_student(student_4)
course_3.add_student(student_5)
course_3.add_student(student_6)


for course in [course_1, course_2, course_3]:
    print()
    print(f"Course Name : {course.course_name}\nTeacher : {course.teacher.name}\nNo of students : {course.student_count()}\nPassed Students : ")
    for student in course.passed_students():
        print(f"Student Name : {student.name}\nScore : {student.score}")

