# 1
def sum_nums(a,b,c):
    return a+b+c

print("Q-1")
numbers = [10, 20, 30]
total = sum_nums(*numbers)
print(f"Total : {total}\n")


# 2
def user_data(first_name, last_name, city):
    data = {
        "Name" : first_name + " " +last_name,
        "City" : city
    }
    return data

print("Q-2")
details = ("Harry", "Potter", "Stockholm")
print(user_data(*details))
print()


# 3
# Using list
print("Q-3")
list_a = [1, 2, 3, 4, 5, 6]
list_b = ["Harry", "Hermione", "Ron", "Emma", "Draco", "John"]
list_c = [1, 2]

first, *middle, last = list_a
print(f"Using numbers \nFirst : {first} \nMiddle : {middle} \nLast : {last}")
print(f"Their types : \nFirst : {type(first)} \nMiddle : {type(middle)} \nLast : {type(last)}\n")

first, *middle, last = list_c
print(f"Using 2 numbers \nFirst : {first} \nMiddle : {middle} \nLast : {last}\n")

first_1, *middle_1, last_1 = list_b
print(f"Using names \nFirst : {first_1} \nMiddle : {middle_1} \nLast : {last_1}\n")

print("""
Notes :
- Function Parameter : def f(*args) => here it packs into tuple
- Assignment target : first, *middle, last = values => here it packs into list
""")

# Exploring with tuple, dict and string
#using tuple
first, *middle, last = (7, 2, 3, 2.5, 5.5, 7.5)
print(f"Using tuple \nFirst : {first} \nMiddle : {middle} \nLast : {last}")
print(f"Their types : \nFirst : {type(first)} \nMiddle : {type(middle)} \nLast : {type(last)}\n")

# using dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
first, *middle, last = my_dict
print(f"Using dict takes only keys \nFirst : {first} \nMiddle : {middle} \nLast : {last}")
print(f"Their types : \nFirst : {type(first)} \nMiddle : {type(middle)} \nLast : {type(last)}\n")
# dict -> First: 'a', Middle: ['b', 'c'], Last: 'd'

first, *middle, last = my_dict.values()   # unpacks the values
print(f"Using dict values \nFirst : {first} \nMiddle : {middle} \nLast : {last}")
print(f"Their types : \nFirst : {type(first)} \nMiddle : {type(middle)} \nLast : {type(last)}\n")

first, *middle, last = my_dict.items()    # unpacks (key, value) tuples
print(f"Using dict key, value \nFirst : {first} \nMiddle : {middle} \nLast : {last}")
print(f"Their types : \nFirst : {type(first)} \nMiddle : {type(middle)} \nLast : {type(last)}\n")

# using string
name = "Harry Potter"
first, *middle, last = name
print(f"Using string \nFirst : {first} \nMiddle : {middle} \nLast : {last}")
print(f"Their types : \nFirst : {type(first)} \nMiddle : {type(middle)} \nLast : {type(last)}\n")

# 4
print("Q-4")
print("""
- * in a function definition will take n number of arguments and packs as single tuple with each argument as single item.
- * in a function call will unpack values while passing so function will get separate values for positional arguments.
""")
