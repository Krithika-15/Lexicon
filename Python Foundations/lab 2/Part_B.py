# Part b - Tuples and unpacking

# 1
print("Q-1")
rgb_values = (255, 165, 0)
print(rgb_values)
red, green, blue = rgb_values
print(f"Red : {red}, Green : {green}, Blue : {blue}")
print()


# 2
print("Q-2")
personal_details = ("John", 25, "Stockholm")
print(personal_details)
name, age, city = personal_details
print(f"Your name is {name}, {age} years old from city {city}")
print()


# 3
print("Q-3")
print("""
Tuples are immutable, once created it's contents can never change. Tuple type has no way to assign to an index.
Gives TypeError: 'tuple' object does not support item assignment
Can modify in the following way
""")
rgb = (255, 165, 0)
print(rgb)
rgb = (rgb[0], 200, rgb[2])
print(rgb)
print("""
Tuples are useful when values should not change because of Safety when data can't be altered by accident anywhere in the program
useful in an (x,y) point, date(year, month, day)
Slightly faster and smaller in memory than an equivalent list
""")
print()


# 4
print("Q-4")
points = [(10, 20), (3, 7), (0, 0), (15, 4), (8, 12)]
print(points[0])
print(points[1])
print(points[0][1])
print(points[-1][1])
x, y = points[3]
print(f"x = {x}, y = {y}")
