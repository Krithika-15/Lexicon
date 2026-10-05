# Part E - Nested Collections
# 1
print("Q-1")
books = [
    {"title": "The Pragmatic Programmer", "author": "Hunt & Thomas", "pages": 352, "available": True},
    {"title": "Clean Code",               "author": "Robert C. Martin", "pages": 464, "available": False},
    {"title": "Fluent Python",            "author": "Luciano Ramalho", "pages": 792, "available": True},
    {"title": "Automate the Boring Stuff","author": "Al Sweigart", "pages": 504, "available": True},
    {"title": "Introduction to Algorithms","author": "Cormen et al.", "pages": 1312, "available": False},
]
for book in books:
    print(book)
print()

# 2
print("Q-2")
print(f"Third book title : {books[2]["title"]}")
print("Using Conditional expression found following : ")
print(f"Last book is {'Available' if books[-1]["available"] else 'Not Available'}")
print(f"First book is {'Available' if books[0]["available"] else 'Not Available'}")
print()


# 3
print("Q-3")
books[-1]["available"] = True
books[1]["Publication Year"] = 2008
print(books[-1])
print(books[1])
print()


# 4
print("Q-4")
departments = {
    "Engineering": ["John", "Bob", "Sam", "Dennis"],
    "Marketing":   ["Priya", "Tom", "Sofia"],
    "Sales":       ["Karan", "Elena", "Henry", "Harry"],
    "HR":          ["Max", "Ben"],
}
for k,v in departments.items():
    print(k , ":", v)
print()


# 5
print("Q-5")
courses = [
    {
        "name": "Python Foundations",
        "teacher": "Ada Lovelace",
        "topics": ["variables", "lists", "dictionaries", "functions"],
    },
    {
        "name": "Web Development",
        "teacher": "Tim Berners-Lee",
        "topics": ["HTML", "CSS", "JavaScript", "HTTP"],
    },
    {
        "name": "Databases",
        "teacher": "Edgar Codd",
        "topics": ["tables", "SQL joins", "indexes", "transactions"],
    },
]

print(courses[1]["topics"][2])  #chained indexing

for course in courses :
    print(course["topics"][0]) #chained indexing

