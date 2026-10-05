# 1
print("Q-1")
words = ["Python", "C", "c++", "C#", "SQL", "JavaScript", "TypeScript"]
sorting = sorted(words, key=len)
print(f"Before sorting : {words}")
print(f"After sorting : {sorting}")

# 2
print("\nQ-2")
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
    },
    {
        "name" : "Emily",
        "score" : 60,
        "active" : True
    }
]

scores_low_to_high = sorted(students, key= lambda student: student["score"])
print(f"Scores low to high")
for student in scores_low_to_high:
    print(f"{student['name']} - {student['score']}")

scores_high_to_low = sorted(students, key= lambda student: student["score"], reverse=True)
print(f"\nScores high to low :")
for student in scores_high_to_low:
    print(f"{student['name']} - {student['score']}")


# 3
print("\nQ-3")
products = {"Ikea cot": 4500, "Kids Kitchen set":1025, "curtains" : 1000, "Blinds": 2500}
sort_products = sorted(products.items(), key=lambda product: product[1])
for p in sort_products:
    print(f"{p[0]} - {p[1]} kr")

# 4
print("\nQ-4")
people = [
    {
        "first_name" : "Harry",
        "last_name" : "Potter"
    },
    {
        "first_name" : "Hermione",
        "last_name" : "Granger"
    },
    {
        "first_name" : "Ron",
        "last_name" : "Weasley"
    }
]
sort_people = sorted(people, key= lambda person: person["last_name"])
print(sort_people)


# 5
print("\nQ-5")
books = [
    {"title": "The Hobbit", "author": "Tolkien", "pages": 310, "year": 1937},
    {"title": "Matilda", "author": "Dahl", "pages": 240, "year": 1988},
    {"title": "Dune", "author": "Herbert", "pages": 612, "year": 1965},
    {"title": "Coraline", "author": "Gaiman", "pages": 162, "year": 2002},
    {"title": "Wonder", "author": "Palacio", "pages": 315, "year": 2012},
]

def book_pages(book):
    return book["pages"]

print("1 - Sorting Books")
sorting_book_pages = sorted(books, key=book_pages)
print("Sorting based on book pages using function")
for book in sorting_book_pages:
    print(f"{book['title']} - {book['pages']} ")

sort_book_pages = sorted(books, key=lambda book: book["pages"])
print("\nSorting based on book pages using lambda")
for book in sort_book_pages:
    print(f"{book['title']} - {book['pages']} ")
print("Final comparison : lambda also looks simpler and understandable")

# sort by average of the two exams from list of student dicts
students = [
    {"name": "Harry", "house": "Gryffindor", "exam_1": 72, "exam_2": 88},
    {"name": "Hermione", "house": "Gryffindor", "exam_1": 98, "exam_2": 99},
    {"name": "Draco", "house": "Slytherin", "exam_1": 85, "exam_2": 80},
    {"name": "Luna", "house": "Ravenclaw", "exam_1": 90, "exam_2": 76},
    {"name": "Cedric", "house": "Hufflepuff", "exam_1": 81, "exam_2": 89},
]

def avg_score(student):
    total = student["exam_1"] + student["exam_2"]
    average =  total/2
    return average

student_avg_score = sorted(students, key=avg_score)
print("\n2 - Student Average Score")
print("Using normal function")
for stu_score in student_avg_score:
    print(f"{stu_score['name']} - {avg_score(stu_score)}")

student_avg_score_1 = sorted(students, key=lambda student: (student["exam_1"] + student["exam_2"])/2)
print("\nUsing lambda - Unable to print the average score as lambda function used")
for student_score in student_avg_score_1:
    print(f"{student_score['name']}")

print("Final comparison : lambda looks simpler but not easily understandable. Normal function is clear stating average score")

print("\n3 - Sorting emails by domain ")
emails = [
    "ron.weasley@hogwarts.edu",
    "Emma@gmail.com",
    "john.smith@Outlook.com",
    "kid_coder@yahoo.com",
    "harry@hogwarts.edu",
]

print("Using lambda")
by_domain = sorted(emails, key= lambda email: (email.strip().lower().split("@"))[1])
print(by_domain)

print("\nUsing normal function")
def email_domain(email):
    email = email.strip().lower()
    parts = email.split("@")
    return parts[1]

by_domain_1 = sorted(emails, key=email_domain)
print(by_domain_1)
print("\nFinal comparison : \nIn lambda, normalizing, splitting and indexing is in same line. \nIn the def, normalizing, splitting and indexing are on separate lines, which might be easy for other developer to understand about code")

print("Overall comparison : I'd pick lambda when I don't want that function later in my code, and would pick def when I want to reuse at some other parts of code like average score, also for code readability")
