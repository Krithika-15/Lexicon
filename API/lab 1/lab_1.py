from pprint import pprint
from api_client import get_json

# # 1
def get_price(product):
    return product['price']

products = get_json("https://fakestoreapi.com/products")
if not products:
    print("Could not load products")
else:
    price_sorting = sorted(products, key=get_price)
    for number, product in enumerate(price_sorting, start=1):
        print(f"{number}. {product['title']} - {product['price']}")


# print(type(products))
# print(len(products))
# pprint(products[0])
# print(products[0]['price'])

# notes
# https://fakestoreapi.com => Server
# /products => is one endpoint (one door) of the API. All the doors together are the API.


# 2
categories = get_json("https://fakestoreapi.com/products/categories")
if not categories:
    print("Could not load categories")
else:
    while True:
        print("Available categories : ")
        for number, category in enumerate(categories, start=1):
            print(f"{number}. {category}")
        user_input = input("Enter the category name : ")
        product_category = get_json(f"https://fakestoreapi.com/products/category/{user_input}")
        if product_category is None:
            print("Could not load, Check your Internet connection")
            break
        elif not product_category:
            print("Category is not available, please choose the available one\n")
        else:
            # pprint(product_category)
            print(f"Length of products : {len(product_category)}")
            sorted_by_price = sorted(product_category, key=get_price)
            print("Cheapest : ")
            pprint(sorted_by_price[0])
            break


# 3

