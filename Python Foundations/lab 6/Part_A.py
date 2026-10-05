# 1
print("Q-1")
squares = []
for n in range(1,21):
    squares.append(n ** 2)
print(squares)

#using list comprehension
sq_nums = [n ** 2 for n in range(1,21)]
print(sq_nums)


# 2
print("\nQ-2")
even_nums = [n for n in range(1,101) if n % 2 == 0]
print(even_nums)


# 3
print("\nQ-3")
names = ["harry potter", " ron weasley ", " Hermione granger", "  Emma", "  john  "]
normalizing = [name.strip().title() for name in names]
print(f"Before : {names}")
print(f"After : {normalizing}")


# 4
print("\nQ-4")
pass_mark = 75
scores = [40, 50, 60, 80, 90, 45, 75]
passing_scores = [s for s in scores if s>=pass_mark]
print(f"All : {scores}")
print(f"Passed : {passing_scores}")


# 5
print("\nQ-5")
scores = [40, 50, 60, 80, 90, 45, 75]
labels = ["PASS" if s >= pass_mark else "FAIL" for s in scores]
print(f"Scores : {scores}")
print(f"Label : {labels}")


# 6
# From Lab 3 Part C
print("\nQ-6")
words = ["Python", "C", "C++", "C#", "SQL", "JavaScript", "TypeScript"]
long_words = []
for word in words:
    if len(word) > 5:
        long_words.append(word)
print(long_words)

# Refactoring
longer_words = [word for word in words if len(word) > 5]
print(longer_words)

# from lab 4 Part D
students = [
    {
        "name" : "Harry Potter",
        "score" : 85,
        "active" : True
    },
    {
        "name" : "Ron Weasley",
        "score" : 75,
        "active" : True
    },
    {
        "name" : "Hermione Granger",
        "score" : 95,
        "active" : True
    },
    {
        "name" : "Luna",
        "score" : 55,
        "active" : False
    }
]

def get_active_users(users):
    active_users = []
    for student in users:
        if student["active"]:
            active_users.append(student)
    return active_users

active_list = get_active_users(students)
print(active_list)

# Refactoring

def active_users(users):
    return [student for student in users if student["active"]]
active_students = active_users(students)
print(active_students)

# from lab 4 Part F
def student_participants(partpnts):
    student_participants = []
    for participant in partpnts:
        if participant["student"]:
            student_participants.append(participant["name"])
    return student_participants

participants = [
    {'name': 'john', 'age': 18, 'student': True, 'fee': 100},
    {'name': 'bob', 'age': 17, 'student': True, 'fee': 0},
    {'name': 'alice', 'age': 22, 'student': False, 'fee': 500}
]
student_participant_list = student_participants(participants)
print(f"Student participants list : {student_participant_list}")


# Refactoring
def student_participant(partpnts):
    return [p["name"] for p in partpnts if p["student"]]

print(f"Participated students : {student_participant(participants)}")
