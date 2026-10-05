# Part F - break and continue

# 1
print("Q-1")
for n in range(1,101):
    if (n % 7 == 0) and (n % 9) == 0 :
        print(f"{n} is divisible by both 7 and 9 ")
        break
print()


# 2
print("Q-2")
languages = ["python", "c++", "C#", " ", "SQL", "   ", "Java"]
for language in languages :
    if not language.strip() :
        continue
    print(f"{language} is Truthy")
print()


# 3
print("Q-3")
names = ["john", "bob", "alice", "ram", "vijay", "suriya"]
target_name = "vijay"

for name in names:
    if name == target_name:
        print("Found")
        break
else:
    print("Not found") # loop finished without hitting break

# print("""
# Why for...else (not if/else) here:
# - if/else inside the loop runs ONCE PER ITEM, so it would print "Not found" for every name that isn't the target -- even though the target might show up later in the list. That's misleading.
# - for...else runs the else block AT MOST ONCE, only after the loop finishes ALL iterations WITHOUT hitting break. So it only fires
# when the target was checked against every name and never matched which is the correct way to say "confirmed not in the list".
# - Rule of thumb: break = found it, stop early -> skip else.
#                  loop completes with no break -> run else.
# """)
print()


# 4
print("Q-4")
numbers = [0, 1, 3, -1, -33, 499, 999, 263]
for n in numbers :
    if n < 0 :
        continue
    elif n >= 0 and n < 999 :
        print(f"Number is {n}")
    elif n == 999 :
        print("Processing stopped")
        break
