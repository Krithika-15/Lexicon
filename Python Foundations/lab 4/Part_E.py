# 1
print("Q-1")
def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def classify(celsius):
    if celsius < 10:
        return "cold"
    elif (celsius >= 10) and (celsius <= 25):
        return "warm"
    elif (celsius > 25):
        return "hot"

def formatting(celsius, fahrenheit, classification):
    return f"{celsius}°C  ({fahrenheit}°F)   - {classification}"


# 2
print("Q-2")
def sub_total(price, quantity):
    return price * quantity

def discount(sub, discount_percent):
    return sub * discount_percent/100

def total(sub, discount_percent):
    return sub - discount_percent


# 3
print("Q-3")
print("Refactoring")
def calculate_area(width, height):
    return width * height

def calculate_cost(area, price_per_sqm):
    return area * price_per_sqm

def report_area_cost(width, height, price_per_sqm):
    area = calculate_area(width, height)
    cost = calculate_cost(area, price_per_sqm)
    return cost



# 4
print("Q-4")
if __name__ == "__main__":
    # Q1
    celsius = [-1, 10, 25, 30]
    print("Temperature Report")
    print("------------------------")
    for c in celsius:
        f = celsius_to_fahrenheit(c)
        classification = classify(c)
        print(formatting(c, f, classification))
    print()

    # Q2
    price = 200
    quantity = 3
    discount_percent = 15
    sub = sub_total(price, quantity)
    disc = discount(sub, discount_percent)
    result = total(sub, disc)
    print(f"sub : {sub}")
    print(f"discount : {disc}")
    print(f"Total : {result}")
    print()

    #Q3
    area = calculate_area(5, 10)
    price_per_sqm = 60
    total_cost = area * price_per_sqm
    print(f"Without refactoring : {total_cost}")

    tot_cost = report_area_cost(5, 10, 60)
    print(f"With refactoring : {tot_cost}")
    print("""
if __name__ == "__main__":
This is called as main guard or sometimes called as "entry point" of a script
What it actually does: every Python file has a hidden variable called __name__.
-- If you run the file directly (python myfile.py), Python sets __name__ to the string "__main__".
-- If you import the file into another file (import myfile), Python sets __name__ to the file's own name ("myfile"), not "__main__".

So the guard is basically saying: "only run this code if this file was run directly, not if someone else imported it as a module."
""")
