# Part F - Applied Challenge : Personal media catalogue
# 1 & 2
print("Q-1 and Q-2")
catalogue = [
    {
        "id": "MV001",
        "title": "Inception",
        "category": "movie",
        "year": 2010,
        "rating": 8.8,
    },
    {
        "id": "MV002",
        "title": "Parasite",
        "category": "movie",
        "year": 2019,
        "rating": 8.5,
    },
    {
        "id": "GM001",
        "title": "The Witcher 3",
        "category": "game",
        "year": 2015,
        "rating": 9.3,
    },
    {
        "id": "GM002",
        "title": "Hades",
        "category": "game",
        "year": 2020,
        "rating": 9.0,
    },
    {
        "id": "GM003",
        "title": "Stardew Valley",
        "category": "game",
        "year": 2016,
        "rating": 8.9,
    },
    {
        "id": "BK001",
        "title": "Dune",
        "category": "book",
        "year": 1965,
        "rating": 8.7,
    },
    {
        "id": "BK002",
        "title": "The Hobbit",
        "category": "book",
        "year": 1937,
        "rating": 8.6,
    },
    {
        "id": "BK003",
        "title": "Software Testing",
        "category": "book",
        "year": 1949,
        "rating": 8.5,
    },
]
print()


# 3
print("Q-3")
new_catalogue = set()
for item in catalogue:
    new_catalogue.add(item["category"])

#so in above each item is a whole dictionary, to access dictionary key just put another nested for loop and loop the item like key in item
#for item in catalogue:           # item is one dictionary
    # for key in item:             # looping a dict gives its KEY NAMES
    #     print(key)               # 'title', 'category', 'year', 'rating'

print(f"Printing set : {new_catalogue}")
print()


# 4
print("Q-4")
for item in catalogue:
    item["ref"] = (item["id"], item["year"])

for item in catalogue:
    print(f"{item['title']} ({item['year']}) - {item['category']}, rating {item['rating']}, Reference {item["ref"]}")
print()


# 5
# nested indexing
print("Q-5")
print("Nested indexing")
print(f"{catalogue[0]["id"]}")
print(f"{catalogue[-1]["category"]}")
print(f"{catalogue[-3]["year"]}")
print()

#updating
print("Updating")
catalogue[0]["id"] = "MV003"
catalogue[-1]["category"] = "Book"

print(f"{catalogue[0]["id"]}")
print(f"{catalogue[-1]["category"]}")
print()

# membership testing
print("membership testing")
print("title" in catalogue[0])
print("Category" in catalogue[2])
print("category" in catalogue[2])

print("Testing membership inside loop")
for item in catalogue:
    print("title" in item)
print()

#collection methods
print("collection methods")
print(list(catalogue[0].keys()))
print(list(catalogue[0].values()))
print(len(catalogue))
print(len(catalogue[0]))
catalogue[-1]["title"] = catalogue[-1]["title"].upper()
print(catalogue[-1]["title"])
print()


# 6
print("Q-6")
print("-" * 50)
print("                     Catalogue")
print("-" * 50)
print(f"Total Items : {len(catalogue)}")
print("-" * 50)
# :<22 Used format specification with padding of 22 as minimum width and < align the title to left and space will be in right
print(f"{catalogue[0]['id']}  {catalogue[0]['title']:<22} {catalogue[0]['year']}  {catalogue[0]['rating']}")
print(f"{catalogue[1]['id']}  {catalogue[1]['title']:<22} {catalogue[1]['year']}  {catalogue[1]['rating']}")
print(f"{catalogue[2]['id']}  {catalogue[2]['title']:<22} {catalogue[2]['year']}  {catalogue[2]['rating']}")
print(f"{catalogue[3]['id']}  {catalogue[3]['title']:<22} {catalogue[3]['year']}  {catalogue[3]['rating']}")
print(f"{catalogue[4]['id']}  {catalogue[4]['title']:<22} {catalogue[4]['year']}  {catalogue[4]['rating']}")
print(f"{catalogue[5]['id']}  {catalogue[5]['title']:<22} {catalogue[5]['year']}  {catalogue[5]['rating']}")
print(f"{catalogue[6]['id']}  {catalogue[6]['title']:<22} {catalogue[6]['year']}  {catalogue[6]['rating']}")
print(f"{catalogue[7]['id']}  {catalogue[7]['title']:<22} {catalogue[7]['year']}  {catalogue[7]['rating']}")
print("-" * 50)
