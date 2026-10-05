# Part B

# 1
# empty string
print("Q-1")
print("empty string")
value1 = ""
if value1:
    print("Empty string is truthy")
else:
    print("Empty string is falsy")
print()

# non-empty string
print("non-empty string")
value2 = "hello"
if value2:
    print("Non-empty string is truthy")
else:
    print("Non-empty string is falsy")
print()

# zero
print("zero")
value3 = 0
if value3:
    print("Zero is truthy")
else:
    print("Zero is falsy")
print()

# non-zero integer
print("non-zero integer")
value4 = 7
if value4:
    print("Non-zero integer is truthy")
else:
    print("Non-zero integer is falsy")
print()

# empty list
print("empty list")
value5 = []
if value5:
    print("Empty list is truthy")
else:
    print("Empty list is falsy")
print()

# non-empty list
print("non-empty list")
value6 = [1, 2, 3]
if value6:
    print("Non-empty list is truthy")
else:
    print("Non-empty list is falsy")
print()

# Notes
# Falsy values
# False          # the boolean itself
# None           # represents "nothing"
# 0              # zero as an int
# 0.0            # zero as a float
# 0j             # zero as a complex number
# ""             # empty string
# ''             # empty string (same thing, different quotes)
# []             # empty list
# ()             # empty tuple
# {}             # empty dict
# set()          # empty set
# range(0)       # empty range

# Truthy values
# True
# 1, -1, 42, 0.5        # any nonzero number
# "0", "False", " "     # any non-empty string — even ones that "look" false!
# [0], [False], [None]  # non-empty list, even if the only item is falsy
# {0: "x"}               # non-empty dict

#  2
print("Q-2")
language = (input("Enter a programming language : ")).strip().lower()
languages = ["python", "java", "javascript", "c#", "c", "c++"]

if language in languages :
    print("Language is available")
else :
    print("Language is not available")
print()


# 3
print("Q-3")
blocked_usernames = ["john", "bob", "alice", "grace", "raghav"]
username = (input("Enter your username : ")).strip().lower()

if username in blocked_usernames :
    print("Sorry you are blocked")
else :
    print("Login successful!")
print()


# 4
cart = []
if not cart :
    print("Your cart is empty")

is_logged_in = False
if not is_logged_in :
    print("You need to Login first")
