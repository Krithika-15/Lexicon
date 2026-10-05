# 1
print("Q-1")
def greet():
    print("Welcome")

def show_course_name():
    return("Python")

def print_separator():
    return "\n"

greet()
print(greet()) # first prints "Welcome" then prints None as greet doesn't return

show_course_name() # doesn't print anything as I'm not storing it in variable and not using print as well
print(show_course_name())

print(f"Welcome! {print_separator()}Have a Nice day")
print(f"See you soon!{print_separator()}Bye")

print()

# 2
print("Q-2")
def greet_person(name):
    print(f"Welcome to the course {name}!")

def introduce(name, city):
    return(f"Hi {name}, Welcome to {city}")

greet_person("John")
greet_person("Harry")
print(introduce("Alice", "Stockholm"))
print(introduce("John", "Gothenburg"))
print()

# 3
print("Q-3")
def add(a, b):
    return(a + b)

def subtract(a, b):
    return(a - b)

def multiply(a, b):
    return(a * b)

def divide(a, b):
    return(a / b)

sum_1 = add(2, 5)
word = add("Harry", " Potter")
print(f"Sum : {sum_1}")
print(f"Sum of words : {word}")

sub_1 = subtract(10, 3)
print(f"Subtract : {sub_1}")

multiply_1 = multiply(5, 3)
multiply_2 = multiply("hi", 3)
print(f"Multiplication : {multiply_1}")
print(f"Multiplication of words : {multiply_2}")

division = divide(100, 2)
print(f"Division : {division}")

print()

# 4
print("Q-4")
print("""
In the above functions like add, subtract, multiply, divide
variable name described inside bracket is called parameter for eg (a, b)
values that are passed while calling the functions is called argument for eg (2, 5)
""")
print()

# 5
print("Q-5")
def calculate_area(width, height):
    return width * height

area = calculate_area(5, 10)
price_per_sqm = 60
total_cost = area * price_per_sqm
print(f"Total cost : {total_cost}")


print()

