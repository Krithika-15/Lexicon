
# Part C - For loops
# 1
names = ["john", "bob", "ram", "harish", "ravi"]
# way 1 - using for loop with a counter
count = 1
for name in names :
    print(f"{count}. Hi {name}!. Welcome to the course")
    count += 1

# using enumerate
print("""
Enumerate is a built-in function like print().
- it's job is given a list(or any iterable)(eg : list, tuple, string, range(0,10) etc.,), it hands you back each item paired with a number
- every single item enumerate produces is a tuple of(index, value)
- The key idea: enumerate doesn't hand you all the tuples at once. It hands you a machine that gives out one tuple each time you ask. The for loop is what does the asking
""")

# way 2 using for loop with enumerate
for index, name in enumerate(names, start = 1) :  # using 1 as default index
    print(f"{index}. Hi {name}! Welcome to the course") #eg: 1. Hi john! Welcome to the course

# trying enumerate with list (list pulls them all out once)
print(list(enumerate(names))) # [(0, 'john'), (1, 'bob'), (2, 'ram'), (3, 'harish'), (4, 'ravi')]

# exploring enumerate
fruits = ["apple", "banana", "cherry"]
fruit = enumerate(fruits)
print(list(fruit))  # [(0, 'apple'), (1, 'banana'), (2, 'cherry')]
print(list(fruit))  # []   ← empty! (because the machine pulls out the first time when we print, for second time again you have to call fruit = enumerate(fruits))
print(fruit)

e = enumerate(["a", "b"])
for x in e:
    print(x) # (0, 'a') and (1, 'b')
print(list(e)) # []   ← empty!

e = enumerate(["a", "b", "c"])
print(next(e)) # (0, 'a') #next is a built-in function
for x in e:
    print(x) # prints remaining b and c as a has been printed already in print(next(e))


e = enumerate(["a", "b"])
print(next(e))
print(next(e))
#print(next(e)) # gives stop iteration error

print(*enumerate(fruits))


# 2
for i in range(1,51) :
    if i % 2 == 0 :
        print(i)


# 3
numbers = [1,2,3,4,5]
count = 0
for n in numbers :
    count += n
print(count)


# 4
numbers = [1,2,3,4,5]
max_value = numbers[0]
for n in numbers :
    if n > max_value:
        max_value = n
print(max_value)


# 5
words = ["Python", "C", "C++", "C#", "SQL", "JavaScript", "TypeScript"]
# without using len built in function
count = 0
longer_words = []
for word in words :
    characters = 0
    for ch in word:
        characters = characters + 1
    if characters > 5 :
        count += 1
        longer_words.append(word)

print(f"{count} words have more than 5 characters. Words are : {longer_words}")

# using len function
counter = 0
long_words = []
for word in words :
    if len(word) > 5 :
        counter += 1
        long_words.append(word)
print(f"{counter} words have more than 5 characters. Words are : {long_words}")

# 6
threshold = 70
scores = [20, 65, 55, 70, 85, 0, 90]
count_passes = 0
count_failed = 0
for score in scores :
    if score >= threshold :
        count_passes += 1
    else :
        count_failed += 1

print(f"Passed : {count_passes}")
print(f"Failed : {count_failed}")


# 7
book = {
    "title": "The Pragmatic Programmer",
    "author": "Hunt & Thomas",
    "pages": 352,
    "available": True
    }

# using keys
book_keys = []
for key in book :
    book_keys.append(key)
print(f"Keys : {", ".join(book_keys)}")

# using values
book_values = []
for values in book.values() :
    book_values.append(values)
print(f"Values : {", ".join(str(v) for v in book_values)}") #used generated expression

# using items()
book_KV = []
for key, values in book.items() :
    book_KV.append((key, values)) # used tuple
    print(f"{key} : {values}")
print(book_KV)
