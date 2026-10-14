from pprint import pprint
from datetime import datetime

from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/", serverSelectionTimeoutMs=3000)
db = client["webshop"]


# 1
for product in db.products.find({"price": {"$gt": 1000}}):
    print(f"{product["name"]} {product["price"]}")


# 2
for order in db.orders.find({"status": {"$ne": "delivered"}}):
    print(f"{order["_id"]} {order["status"]}")


# 3
for customer in db.customers.find({"city": {"$in": ["Stockholm", "Malmö"]}}):
    pprint(customer)


# 4
for product in db.products.find({"details.color": "white"}):
    print(product["name"])


# 5
for product in db.products.find({"tags": "sport"}, {"name": 1, "tags": 1, "_id": 0}):
    print(product)


# 6
for product in db.products.find({}, {"name": 1, "price": 1, "_id": 0}).sort("price", 1).limit(5):
    print(product)


# 7
for order in db.orders.find({"items.product_id" : 2}):
    pprint(order)


# 8
result = db.products.update_many({"category": "Accessories"}, {"$inc": {"price": 20}})
print(result.matched_count)
print(result.modified_count)
for product in db.products.find({"category": "Accessories"}):
    print(product["name"], product["price"])


# 9
db.products.update_one(
    {"name": "Rain Jacket"},
    {
       "$addToSet": {"tags": "new"},
       "$set": {"restock_date": datetime.now()}
    }
)
jacket = db.products.find_one({"name": "Rain Jacket"})
pprint(jacket)


# 10
old_orders = {"status": "new", "order_date": {"$lt": datetime(2026, 3, 20)}}
date_counts = db.orders.count_documents(old_orders)
print(date_counts)
result = db.orders.delete_many(old_orders)
print(result.deleted_count)
