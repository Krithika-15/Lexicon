# 1
print("Q-1")
products = [
    {
        "category" : "  textiles ",
        "product" : "cushion cover",
        "price": "119",
        "stock": 30,
    },
    {
        "category" : "Textiles",
        "product" : "RUG",
        "price": "4 495 kr",
        "stock": "50",
    },
    {
        "category" : "decoration",
        "product" : "Tealight holder  ",
        "price": 99.0,
        "stock": 100,
    },
    {
        "category" : "Decoration",
        "product" : "Mirror",
        "price": 699,
        "stock": None,
    },
    {
        "Category" : "Table Setting",
        "product" : "glass",
        "price": "129.00",
        "stock": 60,
    },
    {
        "category" : "table setting",
        "product" : "Cutlery",
        "price": 599,
        "stock": -15,
    },
    {
        "category" : "Lighting",
        "product" : "Ceiling Lamp",
        "price": "1995:-",
        "stock": 70,
    },
    {
        "category" : "LIGHTING",
        "product" : " table lamp",
        "price": 799,
    },
    {
        "category" : "Living Room",
        "product" : "3-seater sofa",
        "price": "14995 SEK",
        "stock": "30 pcs",
    },
    {
        "category" : "Living room",
        "product" : "Coffee Table",
        "price": 2495,
        "stock": 30,
    },
    {
        "category" : "Barnrum",
        "product" : "Rock elk",
        "price": 449,
        "stock": "0",
    },
    {
        "category" : " CHILDREN",
        "product" : "Children's kitchen",
        "price": "995 kr",
        "stock": 2,
    },
    {
        "category" : "Living Room",
        "product" : "coffee table ",
        "price": 2495,
        "stock": 30,
    }
]

# 2
print("\nQ-2")

def key_normalizing(product):
    return {key.strip().lower(): value for key, value in product.items()}

normalized_product_keys = [key_normalizing(product) for product in products]

def price_normalizing(price):
    if isinstance(price, (int, float)):  # checks whether price is int or float
        return int(price)

    text = price.lower()
    for messy in ["kronor", "sek", ":-", ":", " ", "kr"]:
        text = text.replace(messy, "")
    return int(float(text))   # int("129.00") raises a ValueError as int() can't read a decimal value. float("129.00") gives 129.0, and int(129.0) gives 129

def stock_normalizing(stock):
    # case 1 checks if None then returns 0 without checking further loop
    if stock is None:
        return 0

    # case 2 checks if value is int or float or string
    if isinstance(stock, (int, float)):
        number = int(stock)
    else:
        text = stock.lower()
        for messy in ["pieces", "pcs", " ",]:
            text = text.replace(messy, "")
        number = int(float(text))

    # case 3 check if value is negatvie
    if number < 0:
        return 0

    return number

normalized_products = [
    {
        "category": product.get("category", None).strip().capitalize(),
        "product": product.get("product", None).strip().capitalize(),
        "price": price_normalizing(product.get("price")),
        "stock": stock_normalizing(product.get("stock"))
    }
    for product in normalized_product_keys
]
print(normalized_products)


# 3
print("\nQ-3")
in_stock = []
for product in normalized_products:
    if product["stock"] > 0 and product["product"] not in in_stock:
        in_stock.append(product["product"])
print(f"Products in stock : {in_stock}")

# 4
print("\nQ-4")
seen = set()
unique_products_list = []
for product in normalized_products:
    if product["product"] not in seen:
        seen.add(product["product"])
        unique_products_list.append(product)

unique_categories = {product["category"] for product in normalized_products}
print(unique_categories)


# 5
print("\nQ-5")
product_mapping= {}
for product in normalized_products:
    inv_value = product["price"] * product["stock"]
    product_mapping[product["product"]] = inv_value
print(product_mapping)

# 6
print("\nQ-6")
sorting_products = sorted(product_mapping.items(), key=lambda product: product[1], reverse=True)
for product in sorting_products:
    print(f"{product[0]} - {product[1]}")


# 7
print("\nQ-7")
for index, inv in enumerate(sorting_products, start=1):
    print(f"{index}. {inv[0]} - {inv[1]}")


# 8
print("\nQ-8")
#using unique product list => list of dict Eg : [{'category': 'Textiles', 'product': 'Cushion cover', 'price': 119, 'stock': 30}, {'category': 'Textiles', 'product': 'Rug', 'price': 4495, 'stock': 50}, ......]
names = [product["product"] for product in unique_products_list]
prices = [product["price"] for product in unique_products_list]
product_status = ["In Stock" if product["stock"] > 0 else "Out of Stock" for product in unique_products_list]
print(f"\nProduct Names : {names}")
print(f"\nProduct Prices : {prices}")
product_metadata = list(zip(names, prices, product_status))
print("\nProduct Stock :")
for index, (name, price, status) in enumerate(product_metadata, start=1):
    print(f"{index}. {name} (price : {price}) - {status}")


# 9
print("\nQ-9")

complicated = {product["product"]: "Very cheap" if product["price"] < 200 else "Cheap" if product["price"] < 600 else "Budget" for product in unique_products_list if product["stock"] > 0 and product["price"] < 1000}
print(f"Complicated : {complicated}")

def price_label(price):
    if price < 200:
        return "Very cheap"
    elif price < 600:
        return "Cheap"
    return "Budget"

def is_low_budget_in_stock(product):
    return product["stock"] > 0 and product["price"] < 1000

clear = {
    product["product"]: price_label(product["price"])
    for product in unique_products_list
    if is_low_budget_in_stock(product)
}

print(f"Clear : {clear}")
print("""
Over-Complicated : has multiple conditions and has difficult readability
Clear : uses normal functions and has better code readability
""")
