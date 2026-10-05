# Part H - Stretch Challenges
# 1
print("Q-1")
for n in range(1,101) :
    if n % 3 == 0 and n % 5 == 0 :
        print(f"{n} is FizzBuzz")
    elif n % 3 == 0 :
        print(f"{n} is Fizz")
    elif n % 5 == 0 :
        print(f"{n} is Buzz")
print()


# 2
print("Q-2")
# vowels = ["a", "e", "i", "o", "u"] # both works
vowels = "aeiou"
sentence = "Python is dynamically typed programming language."
count = 0
for ch in sentence :
    if ch in vowels :
        count += 1
print(count)
print()


# 3
print("Q-3")
languages = ["python", "c", "c++", "python", "python", "c", "java", "javascript"]
duplicates = []
originals = []
for lang in languages :
    if lang not in originals :
        originals.append(lang)
    elif lang not in duplicates :
        duplicates.append(lang)
print(f"originals : {originals}")
print(f"duplicates : {duplicates}")
print()


# 4
print("Q-4")
histogram = [3, 5, 2]
for n in histogram :
    print(n * "*")
print()
