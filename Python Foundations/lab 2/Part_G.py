# Part G - Stretch challenges

# 1
print("Q-1")
list_1 = ["Elena", "Henry", "John", "Bob", "Sam", "Dennis", ]
list_2 = ["Elena", "Henry", "John", "Karan",  "Harry"]
print(set(list_1) & set(list_2))  # & intersection works only on sets and not on lists, this gives values available in both
unique_1 = set(list_1) ^ set(list_2) # ^(symmetric difference) unique values in both sets
print(unique_1)
print(set(list_1) | set(list_2)) # all values from both sets
print(set(list_1) - set(list_2)) # unique values from first set
print(set(list_2) - set(list_1)) # unique values from second set
print()


# 2
print("Q-2")
online_course_platform = [
    {
        "name" : "Python",
        "teacher" : "Aladdin",
        "students" : ["john", "bob", "alice"],
        "topics" : ["Python fundamentals", "Object Oriented Programming", "Data Structures"]
    },
    {
        "name": "JavaScript",
        "teacher": "Haithem",
        "students": ["alice", "karan", "elena"],
        "topics": ["DOM", "Events", "Async"],
    },
    {
        "name": "Java",
        "teacher": "Genie",
        "students": ["bob", "henry"],
        "topics": ["Classes", "Collections", "Streams"],
    },
]
print()


# 3
print("Q-3")
inventory = {
    "Keyboard": 25,
    "Mouse": 40,
    "Monitor": 12,
    "USB Cable": 100,
    "Webcam": 8,
}
print()

# using loop
count = 0
for values in inventory.values():
    count = count + values
print(f"Total in stock (before): {count}")

# using built in function
inventory["Webcam"] = 10
inventory["Mouse"] = 50
print(f"Total in stock (after): {sum(inventory.values())}")
print()


#  4
print("Q-4")
print("""
List :
Eg : [1,2,3]
- Ordered, indexable, allows duplicates, mutable.
- use when order matters and items may be added/removed/changed.
- BEST FIT : to-do list

Tuple :
Eg : (10, 20)
- Ordered, indexable, allows duplicates, IMMUTABLE (cannot be changed).
- Use for a fixed group of values that belong together and must
- BEST FIT : (x, y) coordinate, RGB Color (255, 165, 0).

Set :
Eg : {1,2,3}
- unordered, not indexable, NO Duplicates, mutable
- Fast membership tests ("python in courses")
- only sets has & ^ | -
- BEST FIT: collecting the unique tags on a blog post, or checking which usernames appear in two lists.

Dictionary :
Eg : {"name": "Ada", "age": 25}
- Key, Value pairs, Keys are unique, fast lookup by key, mutable
- Use when each value needs a label instead of position number.
- BEST FIT : One product's details (brand, price, stock)

""")
