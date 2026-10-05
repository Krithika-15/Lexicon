class Teacher:
    organization = "Lexicon"
    max_courses = 3
    # all staff work for same organization
    # all the staff has staffing policy to not run more than 3 courses.

    def __init__(self, name):
        self.name = name

class Student:
    pass_mark = 70
    # pass mark is a rule that applies to all the students equally.
    # storing it per student would mean same n no of identical copies.
    # when the pass mark rule changes then need to edit every object instead of one line

    def __init__(self, name, score):
        self.name = name
        if score < 0 or score > 100:
            raise ValueError(f"Score must be between 0 and 100, got {score}")
        self.score = score

    def get_status(self):
        return "PASS" if self.score >= self.pass_mark else "FAIL"

    def update_score(self, new_score):
        if new_score < 0 or new_score > 100:
            raise ValueError(f"Score must be between 0 and 100, got {new_score}")
        self.score = new_score


class Course:
    platform = "Udemy"
    # all courses belong to 1 common platform so instead of re-writing for every object. All object share the same class attribute
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

    def students_above_score_threshold(self, score):
        return [student for student in self.students if student.score >= score]


# creating student object
student_1 = Student("Harry", 85)
student_2 = Student("Hermione", 90)
student_3 = Student("Ron", 95)
student_4 = Student("Emma", 60)
student_5 = Student("Grace", 50)
student_6 = Student("Alice", 85)

# check student object score validation error
try:
    student7 = Student("Emily", -1)
except ValueError as e:
    print(f"Error : {e}")

try:
    student8 = Student("Emily", 101)
except ValueError as e:
    print(f"Error : {e}")


# creating teach object
teacher_1 = Teacher("John")
teacher_2 = Teacher("Bob")


# creating course object
course_1 = Course("Python", teacher_1)
course_2 = Course("SQL", teacher_1)
course_3 = Course("Java", teacher_2)

# adding student object to the course object
course_1.add_student(student_1)
course_1.add_student(student_2)
course_1.add_student(student_3)
course_1.add_student(student_4)
course_3.add_student(student_5)
course_3.add_student(student_6)


for course in [course_1, course_2, course_3]:
    print()
    print(f"Course Name : {course.course_name}\nTeacher : {course.teacher.name}\nNo of students : {course.student_count()}")
    for student in course.students:
        print(f"Student Name : {student.name}\nScore : {student.score}")

# updating the score
student_1.update_score(95)
student_3.update_score(65)

print("=========================================================================")
print("\ncheck update score validation")
try:
    student_2.update_score(105)
except ValueError as e:
    print(f"Error : {e}")

try:
    student_4.update_score(-1)
except ValueError as e:
    print(f"Error : {e}")

print("=========================================================================")

print("\nAfter updating student score in course python")
for course in [course_1, course_2, course_3]:
    print()
    print(f"Course Name : {course.course_name}\nTeacher : {course.teacher.name}\nNo of students : {course.student_count()}")
    for student in course.students:
        print(f"Student Name : {student.name}\nScore : {student.score}")

print("=========================================================================")

print("\nClass Attribute")
print(f"Course Platform : {Course.platform}")
print(f"Student pass mark : {Student.pass_mark}")
print(f"Teacher Belong to Organization : {Teacher.organization}")
print(f"Max courses allowed per teacher : {Teacher.max_courses}")


print("=========================================================================")

print("Check above threshold method in course class")

print(f"Above 90 : {[s.name for s in course_1.students_above_score_threshold(90)]}")
print(f"Above 50 : {[s.name for s in course_1.students_above_score_threshold(50)]}")

print("=========================================================================")

print("Modifying the Class Attribute")
print("students passed with old rule")
print(f"{[s.name for s in course_1.passed_students()]}")

print("\nstudents passed with new rule")
Student.pass_mark = 60
print(f"{[s.name for s in course_1.passed_students()]}")
