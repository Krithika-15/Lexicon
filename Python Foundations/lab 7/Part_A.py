# 1
print("Q-1")
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

book1 = Book("Clean Code", "Robert C. Martin", 464)
book2 = Book("The Pragmatic Programmer", "David Thomas and Andrew Hunt", 352)
book3 = Book("Think Python", "Allen B. Downey", 292)
book4 = Book("Grokking Algorithms", "Aditya Bhargava", 256)

for book in [book1, book2, book3, book4]:
    print(f"Book Title : {book.title}\nAuthor : {book.author}\nPages : {book.pages}\n")

# 2
print("\nQ-2")
class Laptop:
    def __init__(self, brand, model, ram_gb, price):
        self.brand = brand
        self.model = model
        self.ram_gb = ram_gb
        self.price = price

laptop1 = Laptop("Apple", "MacBook Air M3", 16, 14990)
laptop2 = Laptop("Lenovo", "ThinkPad X1 Carbon", 32, 21990)
laptop3 = Laptop("Dell", "XPS 13", 16, 17490)

for laptop in [laptop1, laptop2, laptop3]:
    print(f"Brand : {laptop.brand}\nModel : {laptop.model}\nRam : {laptop.ram_gb}\nPrice : {laptop.price}\n")

print(f"Dell Price Before : {laptop3.price}")
laptop3.price = 15990
print(f"Dell Price After : {laptop3.price}")

# 3
print("\nQ-3")
laptop4 = Laptop("HP", "Pavilion 15", 8, 8990)
laptop5 = Laptop("HP", "Pavilion 15", 8, 8990)
print(f"Laptop 4 : {laptop4}\nLaptop 5 : {laptop5}")
print(f"laptop4 is laptop5 : {laptop4 is laptop5}")

# 4
print("\nQ-4")
class Student:
    def __init__(self, name, score, active=True):
        self.name = name
        self.score = score
        self.active = active

student1 = Student("Harry", 95)
student2 = Student("Emma", 75, False)

for student in [student1, student2]:
    print(f"Student Name : {student.name}\nScore : {student.score}\nActive : {student.active}\n")

# 5
print("\nQ-5")
student5 = Student("Ron", active=False, score=85)
print(f"Student Name : {student5.name}\nScore : {student5.score}\nActive : {student5.active}\n")
