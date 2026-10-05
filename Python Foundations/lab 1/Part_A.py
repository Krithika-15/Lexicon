# Part A - Warm-up : Python Basics

# 1
print("Q-1")
print("Student Name : Krithika Ravichandran")
print("Course Name : System Developer Python and AI")
print("Today's study goal : Python Fundamentals (Types, Operators, String operations etc.,)")
print()


# 2
print("Q-2")
name = "Krithika Ravichandran"
age = 29
height = 1.50  # metres should be decimal
current_student = True
print(f"Value : {name} and type of Value : {type(name)}")
print(f"Value : {age} and type of Value : {type(age)}")
print(f"Value : {height} and type of Value : {type(height)}")
print(f"Value : {current_student} and type of Value : {type(current_student)}")
print()


# 3
print("Q-3")
print(type(age))
age = "29"
print(type(age))
print(
    "Reason : Since Python is Dynamic Typing, a variable is just a name "
    "that points to an object and the type belongs to the object and not "
    "to the variable name. Python figures out the type at runtime based "
    "on whatever the name currently refers to."
)
print()


# 4
print("Q-4")
num1 = 35
num2 = 6
print(f"First Number : {num1} and Second Number : {num2}")
print(f"Addition : {num1 + num2}")
print(f"Subtraction : {num1 - num2}")
print(f"Multiplication : {num1 * num2}")
print(f"Normal Division : {num1 / num2}")
print(f"Floor Division : {num1 // num2}")
print(f"Remainder : {num1 % num2}")
print(f"Exponentiation : {num1 ** num2}")
print()


# 5
print("Q-5")
print("Case 1 : string to int")
print(
    "Required when we get input from user, it's type is string so "
    "for values like age, height, year etc., and we want to perform certain mathematical operations, "
    "we want it to be in int. "
    )
age_input = input("Enter your age : ")   # input() always returns a string
print(type(age_input))
age_number = int(age_input)              # explicit conversion needed for math
print(type(age_number))
print(f"Next year you'll be {age_number + 1}")
print()

print("Case 2 : int to float")
print(
    "Once the number is about to leave a program and when we write into a file, a database or an API "
    "int value might get rejected, or a strict schema validator may say 'expected number with decimals, got interger' "
    "Similar to case 1, while receiving input from user with decimal point for eg: 3.5 "
    "we need to use float conversion instead of int. "
)
price = 199              # whole number, e.g. price in dollars
print(type(price))
price_as_float = float(price)   # convert so it matches decimal formatting expectations
print(type(price_as_float))
print(f"Price: {price_as_float:.2f}")
print()

print("Case 3 : int to string")
print(
    "Required during concatenation for eg 'your string' + 32 this requires both to be string. "
    "Also while joining a list of numbers using join() method conversion of int to string is necessary. "
)
score = 95
print(type(score))
message = "Your score is " + str(score)   # str() needed to concatenate with text
print(message)
print(type(str(score)))
