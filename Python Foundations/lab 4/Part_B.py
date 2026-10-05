# 1
print("Q-1")
def is_even(num):
    return num % 2 == 0

num_1 = is_even(4)
num_2 = is_even(5)
print(f"Even : {num_1}")
print(f"Odd : {num_2}")
print()

# 2
print("Q-2")
def get_larger(a, b):
    return a if a > b else b

max_a = get_larger(5, 10)
max_b = get_larger(50, 3)
print(f"{max_a}")
print(f"{max_b}")
print()

# 3
print("Q-3")
def classify_score(score):
    return "PASS" if score >= 50 else "FAIL"
pass_value = classify_score(50)
fail_value = classify_score(49)
print(f"50 is {pass_value}")
print(f"49 is {fail_value}")
print()

# 4
print("Q-4")
def full_name(first_name, last_name):
    return f"{first_name} {last_name}"
name = full_name("Harry", "Potter")
print(name)
print()

# 5
print("Q-5")
def calculate_discount(price, percent):
    return price - (price * percent/100)
discounted_price = calculate_discount(1500, 10)
print(f"Discounted price : {discounted_price}")
print()

# 6
print("Q-6")
def calculate_area(width, height):
    return width * height

area = calculate_area(5, 10)
price_per_sqm = 60
total_cost = area * price_per_sqm
print(f"Total cost : {total_cost}")

def calculate_area_1(width, height):
    print(width * height)

area_1 = calculate_area_1(5, 5)
print(area_1)
# total_cost_1 = area_1 * price_per_sqm     # TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'
# print(f"Total cost : {total_cost_1}")

print("""
print(result)
- inside a function just prints in the console when the function is called.
- It doesn't return anything, so when we try to call the function and try to store in a variable we get None
- we can't use the value for futher calculations
whereas in return result
- the value is returned to the variable where we tried to store the function call
- so we can use the value for further calculations
""")
print()
