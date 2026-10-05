# 1
print("Q-1")
def calculate_total(numbers):
    total = 0
    for n in numbers:
        total += n
    return total

nums = [1,2,3,4]
total = calculate_total(nums)
print(f"Sum of list nums : {total}")
print()

# 2
print("Q-2")
def count_even(numbers):
    count = 0
    for n in numbers:
        if n % 2 == 0:
            count += 1
    return count

even_nums = [1, 2, 3, 4, 5, 6, 7]
count = count_even(even_nums)
print(f"Total even numbers : {count}")
print()

# 3
print("Q-3")
def get_long_words(words, minimum_length):
    long_words = []
    for word in words:
        if len(word) >= minimum_length:
            long_words.append(word)
    return long_words

names = ["Harry Potter", "Ron Weasley", "Hermione Granger", "Draco", "Ginny Weasly", "Luna", "Emma"]
longer_names = get_long_words(names, 5)
print(longer_names)
print()

# 4
print("Q-4")

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
        "name" : "Draco",
        "score" : 75,
        "active" : True
    },
    {
        "name" : "Ginny Weasly",
        "score" : 60,
        "active" : False
    },
    {
        "name" : "Luna",
        "score" : 55,
        "active" : False
    }
]

def find_student(students, name):
    for student in students:
        if student["name"] == name :
            return student
    return None

available_name = find_student(students, "Harry Potter")
unavailable_name = find_student(students, "Emma Watson")
print(available_name)
print(unavailable_name)
print()

# 5
print("Q-5")
def average_score(students):
    total = 0
    for student in students:
        total = total + student["score"]
    total_students = len(students)
    average = total / total_students
    return average
average = average_score(students)
print(average)
print()

# 6
print("Q-6")
def get_active_users(users):
    active_users = []
    for student in users:
        if student["active"]:
            active_users.append(student)
    return active_users

active_users = get_active_users(students)
print(active_users)
print()
