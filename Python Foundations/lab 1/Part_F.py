# Part f - stretch challenges Python foundation

# 1
print("Q-1")
total_seconds = int(input("Enter total seconds : "))
hours = total_seconds // 3600
remaining = total_seconds % 3600
minutes = remaining // 60
seconds = remaining % 60
print(f"Time is {hours:02d}:{minutes:02d}:{seconds:02d}")
print()


# 2 (using while and for loop )
print("Q-2")
num = 2451
nums = []
while num > 0:
    rem = num % 10
    nums.append(rem)
    num = num // 10
nums.reverse()
for i in nums:
    print(i)
print()

# 2 without loops
print("Q-2 without loops")
num = 5678
thousands = num // 1000 % 10
hundreds = num // 100 % 10
tens = num // 10 % 10
units = num % 10
print(f"{thousands} \n{hundreds} \n{tens} \n{units}")
print()


# 3
print("Q-3")
word = input("Enter any word : ")
word_length = len(word) - 4
characters = "*" * word_length
print(f"{word[:2]}{characters}{word[-2:]}")
print()


#4
print("Q-4")
print("predict int('5') + int('3')")
print("predict word[::1]")
print("predict word[5:2]")
print("predict 'ab' * 3")
print("predict int(True) + int(True)")
