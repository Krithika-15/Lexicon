# Part C - Sets
# 1
print("Q-1")
courses = ["Python", "SQL", "Python", "Git", "SQL", "Python", "Testing"]
print(f"Courses : {courses}, Length : {len(courses)}")
original_courses = set(courses)
print(f"Without Duplicates : {original_courses}, Length : {len(original_courses)}")
print()


# 2
print("Q-2")
dev_a = {"Python", "SQL", "Git", "Docker", "Linux"}
dev_b = {"Python", "JavaScript", "Git", "AWS", "React"}
print(f"Skills both developers share : {dev_a & dev_b}")
print(f"Skills of developer a : {dev_a - dev_b}")
print(f"Skills of developer b : {dev_b - dev_a}")
print(f"Skills of both developers : {dev_b | dev_a}")
print()


# 3
print("Q-3")
courses = {"Python", "SQL", "Git"}
print(courses)
courses.add("JavaScript")
print(courses)
courses.remove("Git")
print(courses)
courses.discard("Ruby")
print("Remove crashes when the value is not present, whereas discard doesn't crash if value is not available")
print(courses)
print("Python" in courses) #case sensitive
print("PYTHON" in courses)
print("ruby" in courses)
print()


# 4
print("Q-4")
print("""
Set is better to stop duplicates.
Set is faster than list.
Set is unordered and unique, whereas list is odered and duplicates are accepted.
Sets are useful in collecting unique visitor IPs to a website, tracking which student IDs have submitted an assignment,
unique tags on blog post, email addresses on a mailing list.
""")
