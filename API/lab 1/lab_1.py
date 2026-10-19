import requests
from pprint import pprint

def get_json(url, params=None, headers=None, timeout=5):
    try:
        response = requests.get(url, params=params, headers=headers, timeout=timeout)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout:
        print("The request took too long")
    except requests.exceptions.ConnectionError:
        print("Could not connect to the server")
    except requests.exceptions.HTTPError as error:
        print(f"The server said no: {error.response.status_code}")
    except requests.exceptions.JSONDecodeError:
        print("The answer was not JSON")
    except requests.exceptions.RequestException as error:
        print(f"Something else went wrong: {type(error).__name__}")
    return None


# # 1
def get_price(product):
    return product['price']

# products = get_json("https://fakestoreapi.com/products")
# # print(type(products))
# # print(len(products))
# # pprint(products[0])
# # print(products[0]['price'])

# price_sorting = sorted(products, key=get_price)
# for number, product in enumerate(price_sorting, start=1):
#     print(f"{number}. {product['title']} - {product['price']}")

# # notes
# # https://fakestoreapi.com => Server
# # /products => is one endpoint (one door) of the API. All the doors together are the API.


# 2
categories = get_json("https://fakestoreapi.com/products/categories")
while True:
    print("Available categories : ")
    for number, category in enumerate(categories, start=1):
        print(f"{number}. {category}")
    user_input = input("Enter the category name : ")
    product_category = get_json(f"https://fakestoreapi.com/products/category/{user_input}")
    if not product_category:
        print("Category is not available, please chose the available one\n")
    else:
        # pprint(product_category)
        print(f"Length of products : {len(product_category)}")
        sorted_by_price = sorted(product_category, key=get_price)
        print(f"Cheapest : {sorted_by_price[0]}")
        break

