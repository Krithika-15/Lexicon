# 1
print("Q-1")
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def is_long(self):
        return self.pages > 300

book1 = Book("Clean Code", "Robert C. Martin", 464)
book2 = Book("The Pragmatic Programmer", "David Thomas and Andrew Hunt", 352)
book3 = Book("Think Python", "Allen B. Downey", 292)
book4 = Book("Grokking Algorithms", "Aditya Bhargava", 256)

for book in [book1, book2, book3, book4]:
    print(f"Book Title : {book.title}\nAuthor : {book.author}\nPages : {book.pages}\nLong Book : {book.is_long()}\n")


# 2
print("\nQ-2")
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError(f"Cannot withdraw {amount}, balance is only {self.balance}")
        else:
            self.balance -= amount


account_holder1 = BankAccount("Harry", 5000)
account_holder2 = BankAccount("John", 1000)


for account_holder in [account_holder1, account_holder2]:
    print(f"Account holder : {account_holder.owner}")
    print(f"Current Balance : {account_holder.balance}")
    account_holder.deposit(1000)
    print(f"Updated Balance : {account_holder.balance}\n")


# 3
print("\nQ-3")
account_holder3 = BankAccount("Ron", 5000)
try:
    account_holder3.withdraw(5100)
except ValueError as e:
    print(f"Error : {e}")

account_holder4 = BankAccount("Emma", 6000)
print(f"Old Balance : {account_holder4.balance}")
account_holder4.withdraw(5100)
print(f"New Balance : {account_holder4.balance}")


# 4
print("\nQ-4")
class Task:
    def __init__(self, title, completed=False):
        self.title = title
        self.completed = completed

    def complete(self):
        self.completed = True

    def reopen(self):
        self.completed = False

task1 = Task("Submit Attendance")
task2 = Task("Complete Lab")

print("Tasks:")
for task in [task1, task2]:
    print(f"Task : {task.title}\nStatus : {task.completed}\n")

print("After complete()")
task1.complete()
task2.complete()
for task in [task1, task2]:
    print(f"Task : {task.title}\nStatus : {task.completed}\n")

print("After task 2 reopen()")
task2.reopen()
for task in [task1, task2]:
    print(f"Task : {task.title}\nStatus : {task.completed}\n")



# 5
print("\nQ-5")
task3 = Task("Register Course")
task4 = Task("Complete Payment")

print("Course Registration")
for task in [task3, task4]:
    print(f"Task : {task.title}\nStatus : {task.completed}\n")

print("After complete()")
task3.complete()
task4.complete()
for task in [task3, task4]:
    print(f"Task : {task.title}\nStatus : {task.completed}\n")

print("After reopen register")
task3.reopen()
for task in [task3, task4]:
    print(f"Task : {task.title}\nStatus : {task.completed}\n")





