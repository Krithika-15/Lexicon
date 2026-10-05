# 1
print("Q-1")
numbers = [[1,5], [50, 30], [-1,0], [45, 30]]

simple_nums_list = []
for num_pair in numbers:
    for num in num_pair:
        simple_nums_list.append(num)
print(simple_nums_list)

print("Using list comprehenshion")
sim_nums_list = [no for no_pair in numbers for no in no_pair]
print(sim_nums_list)


# 2
print("\nQ-2")
# Outer comprehension makes one row per number, inner comprehension fills that row
table = [[row * col for col in range(1, 11)] for row in range(1, 6)]
# print(table)

for row in table:
    print(row)

# proper alignment
for row in table:
    print(" ".join(f"{n:3}" for n in row))

# Good readability two levels of nesting with clear names (row, col) is still easy to follow.
# If it needed a third level or an extra if-condition, a normal nested loop would be clearer.

# 3
print("\nQ-3")
names = ["Harry", "Emma", "Ron", "Hermione", "John"]
scores = [72, 45, 88, 91, 38]
PASS_MARK = 50

passing_students = [
    {"name": name, "score": score}
    for name, score in zip(names, scores)
    if score >= PASS_MARK
]

for student in passing_students:
    print(student)

# 4
print("\nQ-4")
scores = [72, 45, 88, 91, 38, 100]

# Using loop to find if anyone failed ie, score is below 50
anyone_failed = False
for score in scores:
    if score < 50:
        anyone_failed = True
print("Anyone failed (loop):", anyone_failed)

# Using any() to find if anyone failed ie, score is below 50
print("Anyone failed (any):", any(score < 50 for score in scores))


# using loop to find if everyone passed with score 50 or higher
everyone_passed = True
for score in scores:
    if score < 50:
        everyone_passed = False
print("Everyone passed (loop):", everyone_passed)

# using all()
print("Everyone passed (all):", all(score >= 50 for score in scores))

# 5
print("\nQ-5")
# 1: list comprehension
numbers = [1, 2, 3, 4]

# Long way
doubled = []
for n in numbers:
    doubled.append(n * 2)
print(doubled)

# Short way
doubled = [n * 2 for n in numbers]
print(doubled)


# 2: enumerate
fruits = ["apple", "banana", "cherry"]

# Long way
for i in range(len(fruits)):
    print(i + 1, fruits[i])

# Short way
for number, fruit in enumerate(fruits, start=1):
    print(number, fruit)


# 3: zip
names = ["Anna", "Chen"]
ages = [25, 30]

# Long way
for i in range(len(names)):
    print(names[i], ages[i])

# Short way
for name, age in zip(names, ages):
    print(name, age)


# 4: swap two variables

# Long way
a = 1
b = 2
temp = a
a = b
b = temp
print(a, b)

# Short way
a = 1
b = 2
a, b = b, a
print(a, b)


# 5: f-string
name = "Anna"
age = 25

# Long way
print("My name is " + name + " and I am " + str(age) + " years old")

# Short way
print(f"My name is {name} and I am {age} years old")
