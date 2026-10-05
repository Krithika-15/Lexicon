# 1
print("Q-1")
names =["Harry Potter", "Hermione", "John", "Ron", "Emma"]
scores = [85, 90, 60, 78, 95]

for name, score in zip(names, scores):
    print(f"{name} - {score}")


# 2
print("\nQ-2")
student_scores = dict(zip(names, scores))
print(student_scores)


# 3
print("\nQ-3")
products = ["Ikea Cot", "Table", "Curtains", "Blinds"]
prices = [4000, 2500, 1000, 1500]
stocks = [50, 20, 100, 200]
product_status = list(zip(products, prices, stocks))
print(product_status)


# 4
print("\nQ-4")
product_1 = ["Ikea Cot", "Table", "Curtains", "Blinds", "Kids Kitchen Set"]
price_1 = [4000, 2500, 1000, 1500, 1025]
stock_1 = [50, 20, 100, 200]
product_status_1 = list(zip(product_1, price_1, stock_1))
print(f"Products : {product_status_1}, \n when lists doesn't match value is silently ignored")


# 5
print("\nQ-5")
print("product_status = [('Ikea Cot', 4000, 50), ('Table', 2500, 20), ('Curtains', 1000, 100), ('Blinds', 1500, 200)]")
for name, cost, availability in product_status:
    print(f"Product name : {name}")
    print(f"Price : {cost} kr")
    print(f"Availability : {availability}\n")


# 6
print("\nQ-6")
student = "Harry"
another_student = "John"
print(f"Before : \nStudent : {student} \nAnother Student: {another_student}")
another_student, student = student, another_student
print(f"After : \nStudent : {student} \nAnother Student: {another_student}")
print("""
Notes :
Python works out the right side and packs it into a tuple.
When values are separated by a comma, Python makes a tuple from them. It reads the current values => ("Harry", "John")
another_student gets assigned as "Harry" first, then student gets "John" second
""")


