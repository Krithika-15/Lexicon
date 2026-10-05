# Part A - Lists

import copy

# 1
print("Q-1")
programming_languages = ["Python", "JavaScript", "Java", "C", "C++", "C#", "Go", "Rust", "Typescript"]
first_value = programming_languages[0]
last_value = programming_languages[-1]
third_value = programming_languages[2]
second_to_last = programming_languages[-2]
print(f"{first_value} \n{last_value} \n{third_value} \n{second_to_last}")
print()


# 2
print("Q-2")
print(programming_languages[0:3])
print(programming_languages[-3::-1])
print(programming_languages[-3::])
print(programming_languages[::-1])
print()


# 3
print("Q-3")
print(programming_languages)
programming_languages.append("Swift")
print(programming_languages)
programming_languages.insert(-3,"Ruby")  # lands immdediately before -3 so index of Ruby will be -4
print(programming_languages)
programming_languages.insert(3,"PHP")    # lands immdediately after 3 so index of PHP will be 4
print(programming_languages)
programming_languages.remove("Ruby")
print(programming_languages)
programming_languages.pop(4)    # only Index values is accepted both positive and negative.
                                # If not mentioned default is last. Values like "Ruby" is not allowed gives TypeError: 'str' object cannot be interpreted as an integer
print(programming_languages)
print()


# 4
print("Q-4")
numbers = [1,2,3,4,7,2]
print(f"Length : {len(numbers)}")
print(f"min value : {min(numbers)}")
print(f"max value : {max(numbers)}")
print(f"sum value : {sum(numbers)}")
print()


# 5
print("Q-5")
list_a = [5,3,7,2,9,10]
print(f"Original list : {list_a}")
list_a.sort()
print(f"sorted list : {list_a}")

list_b = [4,1,8,9,1,4,15]
print(f"Original list : {list_b}")
descending = sorted(list_b)
descending.reverse()
print(f"descending list : {descending}")

print("""
.sort() vs sorted() :
    - .sort() is a method modifies the list in place and returns None
    works on lists only, called on an object with a dot
    - sorted() is a built in function and returns a brand new sorted list, original list is untouched
    works on any iterable(list, tuple, string, dict, set, range ...) and pass the data as an argument
"""
)
print()


# 6
print("Q-6")
list_a = [1,2,3,4,5]
list_b = list_a  # both a and b points to same object in memory
print(f"List a : {list_a}")
print(f"List b : {list_b}")
list_a.append(6)
print(f"List a : {list_a}")
print(f"List b : {list_b}")
list_b = list_a.copy()  # gives a copy of list a
list_a.append(7)
print(f"List a : {list_a}")
print(f"List b : {list_b}")

print(".copy() gives a shallow copy so for inner list changes reflect hence deepcopy is required")
list_a = [[1,2],[3,4]]
list_b = list_a.copy()
print(f"List a : {list_a}")
print(f"List b : {list_b}")
list_a.append([5,6])
print(f"List a : {list_a}")
print(f"List b : {list_b}")
list_a[0][1] = 7
print(f"List a : {list_a}")
print(f"List b : {list_b}")
print("Even list b is altered in .copy()")

print("deep copy eg : for this need to import copy module from the standard library it is not a buil in like len")
list_b = copy.deepcopy(list_a)
print(f"List a : {list_a}")
print(f"List b : {list_b}")
list_a[0][0] = 10
list_a[0][1] = 15
print(f"List a : {list_a}")
print(f"List b : {list_b}")
