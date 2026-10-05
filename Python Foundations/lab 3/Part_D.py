# Part D - range, enumerate and nested loops
# 1
for n in range(10, 0, -1) :
    print(n)

# 2
number = int(input("Enter a number : "))
for n in range(1, 11) :
    print(f"{number} * {n} = {number * n}")

# 3
playlist = ["Rowdy Baby", "Vaathi Coming", "Arabic Kuthu", "Why This Kolaveri Di", "Kaavaalaa"]
for index, song in enumerate(playlist, start=1) :
    print(f"{index}. {song}")

# 4
for x in range(1,4) :
    for y in range(1,5) :
        print((x,y))


# 5 "text grid" just means a block of characters arranged in rows and columns
for x in range(1,6) :
    for y in range(1,6) :
        print("*", end=" ")  # print by default has this print("%", end="\n"), but we overwrite with space so y stays in same line
    print()

