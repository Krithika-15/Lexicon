# Part D - Dictionaries

# 1
print("Q-1")
laptop = {
    "brand": "Dell",
    "model": "XPS 13",
    "ram": 16,
    "storage": 512,
    "price": 1299,
}
print(f"Brand : {laptop["brand"]}")
print(f"Model : {laptop["model"]}")
print(f"RAM : {laptop["ram"]}")
print(f"Storage : {laptop["storage"]}")
print(f"Price : {laptop["price"]}")
print()


# 2
print("Q-2")
print("Before :", laptop)
laptop["price"] = 1500
laptop["operating_system"] = "Windows"
del laptop["storage"]
print("After :", laptop)
print()


# 3
# existing key: both work the same
print("Q-3")
# print(f"Os : {laptop["OS"]}") #unsafe way to get unknown key
print(f"Os : {laptop.get("OS", "Not available")}")

# missing key: they behave very differently
# print(f"Accessing Unavailable key - Production Year : {laptop["production_year"]}") # gives KeyError
print(f"Accessing Unavailable key - Production Year : {laptop.get("Production_year", "Not Available")}")  #safe way to get value that is not available
print()


# 4
print("Q-4")
print(f"Keys : {laptop.keys()}")
print(f"Values : {laptop.values()}")
print(f"Items : {laptop.items()}")
# .keys(), .values() and .items() return a special object called view objects
# hence converting to list for better view
print(f"Keys : {list(laptop.keys())}")
print(f"Values : {list(laptop.values())}")
print(f"Items : {list(laptop.items())}")
# or another way using join
print(f"Keys : {', '.join(laptop.keys())}")
print()


# 5
print("Q-5")
study_hours = {
    "Python": 12,
    "SQL": 8,
    "Git": 4,
    "Testing": 6,
    "Networking": 5,
}

total_hours = 0
for value in study_hours.values():
    total_hours = total_hours + value

print(f"Total hours : {total_hours}")
print(f"Anothey way without loops : {sum(study_hours.values())}")
