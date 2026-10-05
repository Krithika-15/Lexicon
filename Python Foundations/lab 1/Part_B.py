# PART B - User Input and Calculations

# 1
print("Q-1")
name = input("Enter your name : ")
date_of_birth = int(input("Enter your year of birth : "))
current_year = 2026
print(f"Your approximate age is : {current_year - date_of_birth}")
print()


# 2
print("Q-2")
item_price = float(input("Enter the price of an item : ")) #199 as input
discount_percentage = float(input("Enter the discount percentage : ")) #25 as input
total_price = item_price - item_price * (discount_percentage / 100)
print(round(total_price, 2)) # gives 149.25
print(f"{total_price:.2f}") # cannot be used further for mathematical operations as it's type is string
print()


# 3
print("Q-3")
temperature = float(input("Enter the temperature in celcius : "))
fahrenheit = temperature * 9/5 + 32
print(f"Fahrenheit is : {fahrenheit}")
print()


# 4
print("Q-4")
length = float(input("Enter the room length : "))
width = float(input("Enter the room width : "))
area = length * width
perimeter = 2 * (length + width)
print(f"Area : {area:.2f} sq.m and Perimeter : {perimeter:.2f} sq.m")
print()


# 5
print("Q-5")
name = input("Enter your name : ")
date_of_birth = int(input("Enter your year of birth : "))
current_year = 2026
print(f"Your approximate age is : {current_year - date_of_birth}")
print("""
- If user enters 'hello', int('hello') raises:
- ValueError: invalid literal for int() with base 10: 'hello'
- and the program crashes immediately at that line.

EG:
int("101", 2)   # interpret "101" as binary (base 2)  → 5
int("ff", 16)   # interpret "ff" as hexadecimal (base 16) → 255
int("17", 8)    # interpret "17" as octal (base 8) → 15

If you don't specify a base, Python defaults to base 10 (normal decimal numbers)
""")
