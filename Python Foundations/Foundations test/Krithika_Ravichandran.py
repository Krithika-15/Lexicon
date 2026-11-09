# ==================================================
# TASK 1
# ==================================================

products = [
    {"name": "Laptop", "price": 12000, "stock": 4},
    {"name": "Mouse", "price": 350, "stock": 0},
    {"name": "Keyboard", "price": 800, "stock": 6},
    {"name": "Monitor", "price": 3200, "stock": 3},
    {"name": "Headset", "price": 950, "stock": 0},
    {"name": "Webcam", "price": 1100, "stock": 5}
]

# 1. Loop through the products.
# 2. Print the name of every product that is in stock.
# 3. Calculate the total value of all products in stock.
#    The value of a product is price * stock.
# 4. Print the total value.
# 5. Keep track of which in-stock product has the highest price
#    without using max(), and print its name.


# Write your solution below:

print("Task 1")
total_value = 0
highest_product_price_name = None
highest_product_price = 0

print("Name of every product in stock : ")
for product in products:
    if product["stock"]:
        print(product["name"])
        total_value += (product["price"] * product["stock"])
        if product["price"] > highest_product_price:
            highest_product_price = product["price"]
            highest_product_price_name = product["name"]


print(f"\nTotal Value of all products in stock : {total_value}")
print(f"\nProduct with highest price is {highest_product_price_name} with price {highest_product_price}")




# ==================================================
# TASK 2
# ==================================================

scores = [78, 92, 55, 81, 67, 95, 73]

# Create a function called calculate_average that:
# - receives a list of scores
# - calculates and returns the average score
#
# Create another function called create_result that:
# - receives a list of scores
# - uses calculate_average()
# - returns "PASS" if the average is 70 or higher
# - otherwise returns "FAIL"
#
# Call create_result() using the scores above.
# Print both the average score and the final result.


# Write your solution below:
def calculate_average(scores):
    avg_score = sum(scores) / len(scores)
    return avg_score

def create_result(scores):
    average = calculate_average(scores)
    return "PASS" if average >= 70 else "FAIL"

print("\nTask 2")
average_score = calculate_average(scores)
result = create_result(scores)
print(f"Average Score : {average_score:.2f} \nResult : {result}")  # used format specification .2f




# ==================================================
# TASK 3
# ==================================================

product_prices = [250, 400, 150, 700]

order_settings = {
    "discount": 10,
    "shipping": 49,
    "priority": True
}

# Create a function called calculate_order that:
# - receives a customer name as a normal parameter
# - receives any number of product prices using *args
# - receives optional settings using **kwargs
# - calculates the subtotal of all product prices
# - applies the discount percentage if "discount" exists
# - adds shipping if "shipping" exists
# - returns a dictionary containing:
#       customer
#       subtotal
#       final_total
#       settings
#
# Call the function using:
# - customer name "Anna"
# - the values from product_prices using unpacking
# - the values from order_settings using dictionary unpacking
#
# Print the returned dictionary.


# Write your solution below:

def calculate_order(name, *args, **kwargs):
    sub_total = sum(args)
    discount = kwargs.get("discount", 0) # 0 as fallback
    shipping = kwargs.get("shipping", 0) # 0 as fallback
    after_discount = sub_total - (sub_total * discount/100)
    total = after_discount + shipping
    customer_data = {
        "customer" : name,
        "subtotal" : sub_total,
        "final_total" : total,
        "settings" : kwargs
        }
    return customer_data

print("\nTask 3")
result = calculate_order("Anna", *product_prices, **order_settings)
print(result)



# ==================================================
# TASK 4
# ==================================================

players = [
    {"name": "  anna", "score": 85, "active": True},
    {"name": "DAVID ", "score": 72, "active": False},
    {"name": " sara ", "score": 94, "active": True},
    {"name": "LEO", "score": 67, "active": True},
    {"name": " emma", "score": 88, "active": True},
    {"name": "OSCAR ", "score": 76, "active": False}
]

# 1. Create a new list containing normalized player names.
#    Remove unnecessary whitespace and use consistent capitalization.
#    Use a list comprehension.
#
# 2. Create a new list containing only the active players
#    with a score of 80 or higher.
#    Use a list comprehension.
#
# 3. Sort the original players by score from highest to lowest.
#    Use sorted() with a lambda.
#
# 4. Print the ranking in the following format:
#
#    1. Sara - 94
#    2. Emma - 88
#    ...
#
#    Generate the ranking numbers using enumerate().
#
# 5. Create a separate list containing the player names and
#    another list containing their scores.
#    Combine them using zip() and print each name together
#    with its score.


# Write your solution below:

print("\nTask 4")
# 1
player_names = [p["name"].strip().lower().capitalize() for p in players]
print(f"Normalized player names : {player_names}\n")

# 2
active_players = [p["name"].strip().lower().capitalize() for p in players if p["score"] >= 80 and p["active"]]
print(f"Active players with score 80 and higher : {active_players}\n")

# 3
sorted_players = sorted(players, key= lambda p: p["score"], reverse=True)
print(f"Sorted players : {sorted_players}\n")

# 4
print("ranking numbers using enumerate()")
for index, value in enumerate(sorted_players, 1):
    print(f"{index}. {value['name'].strip().lower().capitalize()} - {value['score']}")

# 5
players_names =[p["name"] for p in players]
print(f"\nPlayers name list : {player_names}")

players_scores = [p["score"] for p in players]
print(f"Players scores lists : {players_scores}")

player_name_score = zip(player_names, players_scores)
print("\nPrinting player name and score together using zip")
for p in player_name_score:
    print(p)
