# 1
print("Q-1")
def greet(name, greeting="Hello"):
    return f"{greeting} {name}"
val_1 = greet("Harry", "Hi")
# val_2 = greet("Hi", name="Bob") gives error because name is filled with "hi" and again with "bob"
val_3 = greet("John")
val_4 = greet("Bob", greeting="hiii")
print(val_1)
# print(val_2)
print(val_3)
print(val_4)
print()

# 2
print("Q-2")
def calculate_price(price, quantity=1, discount=0):
    total = (price * quantity) - (price * quantity * discount / 100)
    return total
product_1 = calculate_price(500, 2, 10)
product_2 = calculate_price(500, 2)
print(f"With Discount : {product_1}")
print(f"Without Discount : {product_2}")
print()

# # 3
# print("Q-3")
def create_profile(name, city="Unknown", active=True):
    profile = {
        "Name" : name,
        "City" : city,
        "Status" :active
    }
    return profile
user_1 = create_profile("Harry", "Stockholm", True)
user_2 = create_profile("John",active=True) #mentioning the default parameter to avoid filling in 2nd parameter
user_3 = create_profile("Bob", "Gothenburg")
user_4 = create_profile("Bob", "Stockholm", "False")
print(user_1)
print(user_2)
print(user_3)
print(user_4)
print()

# 4
print("Q-4")
# using the above function create_profile
# user_5 = create_profile("Vijay", active=False, "coimbatore")
# error : Positional argument cannot appear after Keyword arguments
# active="False" is Keyword argument

user_6 = create_profile("Ajith", "coimbatore")
print(user_6)
user_7 = create_profile(active=False, name="Alice")
print(user_7)
user_8 = create_profile(city="Stockholm", name="Henry", active=True)
print(user_8)
print()

# 5
print("Q-5")
# INVALID:
# def greet(greeting="Hello", name):
#     return f"{greeting} {name}"
print(f"""
while writing the above function, Pylance gives you error before running as :
Non-default argument(name) follows default argument(greeting)

If we call greet("Amy"), python doesn't know which if 'amy' belongs to default or non default argument.
Always put non default argument first, then default arguments
""")


### INCOMPLETE
