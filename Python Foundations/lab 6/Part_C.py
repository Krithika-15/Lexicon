# 1
print("Q-1")
playlist = ["Jai Ho", "Chaiyya Chaiyya", "Chinna Chinna Aasai", "Mustafa Mustafa", "Nenjukkul Peidhidum"]
for index, song in enumerate(playlist, 1):
    print(index, song)


# 2
print("\nQ-2")
tasks = ["Login", "Submit_Attendance", "Complete_Lab", "Push_To_Git"]
for index, task in enumerate(tasks, 1):
    print(f"Task {index}: {task}")



# 3
print("\nQ-3")
threshold = 500
values = [100, 200, 300, 400, 500, 600, 700, 800, 900]
large_values = [index for index, val in enumerate(values) if val > threshold]
print(large_values)


# 4
print("\nQ-4")
words = ["python", "java", "SQL", "C"]
for i in range(len(words)):
    print(i, words[i])

for i, word in enumerate(words):
    print(i, word)

print("""
- range(len(words)), gives only the index, so need to look for the item with words[i]
- Without enumerate words need to be used twice to get length of words len(words) and for indexing words[i]
- enumerate removes manual indexing, gives both the index and the item in one step.
""")
