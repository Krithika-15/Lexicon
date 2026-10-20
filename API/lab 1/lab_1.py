from pprint import pprint
from api_client import get_json
import requests

# # # 1
# def get_price(product):
#     return product['price']

# products = get_json("https://fakestoreapi.com/products")
# if not products:
#     print("Could not load products")
# else:
#     price_sorting = sorted(products, key=get_price)
#     for number, product in enumerate(price_sorting, start=1):
#         print(f"{number}. {product['title']} - {product['price']}")


# # print(type(products))
# # print(len(products))
# # pprint(products[0])
# # print(products[0]['price'])

# # notes
# # https://fakestoreapi.com => Server
# # /products => is one endpoint (one door) of the API. All the doors together are the API.


# # 2
# categories = get_json("https://fakestoreapi.com/products/categories")
# if not categories:
#     print("Could not load categories")
# else:
#     while True:
#         print("Available categories : ")
#         for number, category in enumerate(categories, start=1):
#             print(f"{number}. {category}")
#         user_input = input("Enter the category name : ")
#         product_category = get_json(f"https://fakestoreapi.com/products/category/{user_input}")
#         if product_category is None:
#             print("Could not load, Check your Internet connection")
#             break
#         elif not product_category:
#             print("Category is not available, please choose the available one\n")
#         else:
#             # pprint(product_category)
#             print(f"Length of products : {len(product_category)}")
#             sorted_by_price = sorted(product_category, key=get_price)
#             print("Cheapest : ")
#             pprint(sorted_by_price[0])
#             break


# # 3
# # move get_json to its own file


# 4
new_product = {
    "title": "Ikea sofa",
    "price": 5000,
    "description": "The KIVIK sofa has a strong personality and clear design language, while the options mean you can easily match it with your home decor.",
    "category": "Furniture",
    "image" : "https://www.ikea.com/se/sv/images/products/kivik-hoernsoffa-5-sits-kelinge-graturkos__1055828_pe848118_s5.jpg?f=u"
}

response = requests.post("https://fakestoreapi.com/products", json=new_product, timeout=5)
new_product_status = response.status_code
print(new_product_status)
if new_product_status == 201 or new_product_status == 200:
    pprint(response.json())
else:
    print(f"New Product creation failed with status code : {new_product_status}")

# 201
# result : {'category': 'Furniture',
#  'description': 'The KIVIK sofa has a strong personality and clear design '
#                 'language, while the options mean you can easily match it with '
#                 'your home decor.',
#  'id': 21,
#  'image': 'https://www.ikea.com/se/sv/images/products/kivik-hoernsoffa-5-sits-kelinge-graturkos__1055828_pe848118_s5.jpg?f=u',
#  'price': 5000,
#  'title': 'Ikea sofa'}

price_change = {"price": 599}
response = requests.patch("https://fakestoreapi.com/products/7", json=price_change, timeout=5)
price_change_status_code = response.status_code
if price_change_status_code == 200:
    print(price_change_status_code) # status code : 200
    pprint(response.json()) # {'id': 7, 'price': 599}
else:
    print(f"Price change failed with status code : {price_change_status_code}")

