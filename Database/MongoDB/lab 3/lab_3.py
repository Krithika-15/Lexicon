from pprint import pprint

from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/", serverSelectionTimeoutMs=3000)
db = client["webshop"]


# 1
# Reviews should be Embed, because each review belongs to one book and
# the book page shows them together.
# Members should be Reference by their _id, because one member may borrow many books
# and copying the member details in every book would mean updating many copies whenever member data change.


# 2
# Advantage :
# Order can be shown in the screen with the product name without looking up anywhere in products
# which makes the reading faster.
# It also keep the name as it was when the customer bought it (true historical record)
#
# Disadvantage :
# The same name is stored many times, which takes more space.
# If a name must be corrected in case of a typo, then every order that copied it must be updated too.


# # 3
# db.drop_collection("newsletter_signups")
# db.create_collection("newsletter_signups", validator={"$jsonSchema":{
#     "required": ["email"],
#     "properties": {
#         "email": {"bsonType": "string"},
#         "source": {"enum": ["web", "store"]}
#     }
# }} )
# # valid document
# db.newsletter_signups.insert_one({"email": "harry@mail.com", "source": "web"})
# print("Valid Signup inserted")
# # invalid document
# # db.newsletter_signups.insert_one({"email": "ron@mail.com", "source": "online"})


# 4
# How many customers live in each city? Use $group. Biggest city first.
# List of customers and their city
for customer in db.customers.find():
    pprint(f"{customer["first_name"]} : {customer.get("city")}")
print()

# biggest_city with count
biggest_city = ([
    {"$group": {"_id": "$city", "count": {"$sum": 1}}},
    {"$sort": {"count": -1}}
])

for row in db.customers.aggregate(biggest_city):
    print(row)

