# 1
print("Q-1")
squares = {n : n**2 for n in range(1,11)}
print(squares)

# 2
print("\nQ-2")
words = ["Python", "C", "C++", "C#", "SQL", "JavaScript", "TypeScript"]
word_length = {word : len(word) for word in words}
print(word_length)


# 3
print("\nQ-3")
languages = ["  pyThoN", "C", "pYTHOn", "C++", "SqL", "C#", "sQL", "  JavaSCRipt  ", "  TyPEsCrIpT  ", "   JavaSCRipT   "]
without_duplicates = {lang.lower().strip() for lang in languages}
# note : unordered and unique
print(without_duplicates)


# 4
print("\nQ-4")
products = {
    "Bed_Frame" : 4000,
    "Kitchen_Toy" : 1095,
    "Colours" : 250,
    "Board" : 300,
    "Soft_Toy" : 500
}

threshold = 500
low_budget = {k : v for k, v in products.items() if v < threshold}
print(low_budget)


# 5
print("\nQ-5")
students = [
    {
        "name" : "Harry Potter",
        "score" : 85,
        "active" : True
    },
    {
        "name" : "Ron Weasley",
        "score" : 75,
        "active" : True
    },
    {
        "name" : "Hermione Granger",
        "score" : 95,
        "active" : True
    },
    {
        "name" : "Luna",
        "score" : 55,
        "active" : False
    },
    {
        "name" : "Emily",
        "score" : 60,
        "active" : True
    }
]

pass_mark = 75
score = {s["name"] : "PASS" if s["score"] >=pass_mark else "FAIL" for s in students}
print(score)
