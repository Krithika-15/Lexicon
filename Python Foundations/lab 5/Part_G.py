# 1
print("Q-1")
def merge_settings(defaults, **overrides):
    return {**defaults, **overrides}


defaults = {"theme" : "light", "font_size" : 12, "autosave" : True, "language" : "en"}
result_1 = merge_settings(defaults, theme="dark", font_size=16)
print(result_1)
print(defaults)


# 2
print("\nQ-2")
def call_summary(function_name, *args, **kwargs):
    named_args = []
    for item in args:
        named_args.append(f"{item!r}")  # conversion field calls repr() - just shows how you'd type the value like quote marks on string
    for k, v in kwargs.items():
        named_args.append(f"{k}={v!r}")
    named_args = ", ".join(named_args)
    return f"{function_name}({named_args})"


output = call_summary("submit_attendance", "Harry Potter", True, platform="attendance_portal", retries=3, report_webpage_error=True)
print(output)

output = call_summary("register_course", "Ron Weasley", False, platform="Udemy", retries=0, report_webpage_error=False)
print(output)


# 3
print("\nQ-3")
def statistics(*numbers):
    if not numbers:
        return "No Numbers were provided", 0, 0, 0 ,0
    else:
        count = 0
        total = 0
        min_val = numbers[0]
        max_val = numbers[0]
        for n in numbers:
            count += 1
            total += n
            if n < min_val:
                min_val = n
            elif n > max_val:
                max_val = n
        average = total / count
    return count, total, average, min_val, max_val


count, total, average, min_val, max_val = statistics(1, 5, 3, 7, 9, 2, 4)
print(f"Count : {count} \nTotal : {total} \nAverage : {average:.2f} \nMin Value : {min_val} \nMax Value : {max_val}")

count, total, average, min_val, max_val = statistics()
print(f"\nCount : {count} \nTotal : {total} \nAverage : {average:.2f} \nMin Value : {min_val} \nMax Value : {max_val}")



# 4
print("\nQ-4")

print("Predict 1")
message = "This is global"
def msg():
    message = "This is local"
    print(message)

msg()
print(message)
print("Prediction : assigning inside msg() creates a new local, and global is untouched")

print("Predict 2")
count = 5
# def counter():
#     count = count + 1  # UnboundLocalError: cannot access local variable 'count' where it is not associated with a value
#     return count

# print(counter())
print(count)
print("Prediction : UnBoundLocalError ")


print("Predict 3")
name = "Harry"
def username():
    namess = "This is local"

    def innerLoop():
        print(f"inner loop : {name}")
        print(names)
    names = "test"
    innerLoop()
    print(name)

username()
print(name)

# note : global variables can be accessed without global keyword inside function
# but need to use global keyword to modify it

print("Predict 4")
def username():
    def innerLoop():
        print("inner sees:", names)
    names = "first"
    innerLoop()          # inner sees: first
    names = "second"
    innerLoop()          # inner sees: second
username()


print("Predict 5")
# squares = [x * x for x in range(3)]
# print(x)             # NameError: name 'x' is not defined


print("Predict 6")
for i in range(3):
    pass
print(i)

if True:
    colour = "red"
print(colour)

# if False:
#     colour = "red"
# print(colour)      # NameError: name 'colour' is not defined ❌

print("""
Prediction :
- variables created inside for, if, while can be accessed outside, only if it ran ie., the line that creates the variable has to actually run.
- functions create a new scope
- list or any other iterable comprehension creates a new scope
""")





