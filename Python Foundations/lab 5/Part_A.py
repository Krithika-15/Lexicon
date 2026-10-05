# 1
course_name = "python"
def courses():
    course_name = "Python Foundation"
    print(f"Inside the function : {course_name}")


# 2
def local_counter(numbers):
    counter = 0
    for n in numbers:
        counter += n
    return counter


# 3
# cost = 100
# def broken_new_cost():
#     cost = cost + 250   # UnboundLocalError! here cost is treated as local variable and tries to get value to sum with 250
#     return cost

cost = 100
def new_cost(c):
    result = c + 250
    return result

# refactoring
cost_1 = 500
def total_cost():
    global cost_1
    cost_1 += 600
    return cost_1


# 4
def outer_loop(n):
    num = n

    def inner_loop():
        print(f"This is the modified number in inner loop : {num}") # Enclosing

    print(f"Outer loop : {num}")
    inner_loop()


def outer_loop_practice(n):
    num = n
    def inner_loop():
        nonlocal num
        n = 15
        num = n
        print(f"This is the modified number in inner loop : {n}")

    print(f"Outer loop before: {n}")
    inner_loop() # need to call this inner loop before you access num to reflect the num changes else num will have older value
    print(f"Outer loop after : {num}")



if __name__ == "__main__":
    print("Q-1")
    courses()
    print(f"Outside the function : {course_name}")
    print("""
    - course_name inside courses function has local scope and it doesn't get values from global variable
    - course_name outside the courses function has global scope, which is not modified until the function uses it with keyword global
    - for eg : gloabl course_name then in next line modify the course_name .
    - gloabl course_name is declaration
    """)
    print()

    print("Q-2")
    total = local_counter([1,2,3,4,5])
    print(f"Total of list values : {total}")
    # print(counter) # error as counter is not defined
    print()

    print("Q-3")
    # cost = broken_new_cost() ==> gives  # UnboundLocalError!
    print(f"Old cost is global variable : {cost}")
    cost = new_cost(cost)
    print(f"New cost is global variable : {cost}\n")

    print(f"Old cost is global variable: {cost_1} ")
    print(f"New cost is : {total_cost()}")
    print(f"Global variable is also changed : {cost_1}")
    print("""
    Without using global keyword inside function, we have to again save the returned value from function in same global variable itself
    With global keyword inside function, the global variable automatically gets modified without re-assigning again manually.
    """)

    print("Q-4")
    data = outer_loop(5)
    print("Using nonLocal keyword inside inner function , similar to the way we use global keyword inside function to access global variable")
    new_data = outer_loop_practice(6)

    print("Q-5")
    # #shadowing list
    # list = [9, 2, 15]          # 'list' now refers to this actual list, not the built-in type
    # print(list)                # [9, 2, 15]

    # new_list = list(range(5))  # TypeError: 'list' object is not callable
    # # Python tries to call list like a function
    # # but 'list' is now my [9, 2, 15] object, which can't be called.

    # #shadowing max
    # max = 100
    # print(max([4, 7, 2]))      # TypeError: 'int' object is not callable
    # # 'max' used to be the built-in max() function; now it's just the number 100.

    # # shadowing str
    # str = "hello world"        # 'str' refers to this actual string, not the built-in type
    # print(str)                  # hello world

    # num_to_text = str(42)       # TypeError: 'str' object is not callable
    # # python tries to call str built-in function but gives error

    # # shadowing sum
    # sum = 100
    # print(sum([1, 2, 3]))       # TypeError: 'int' object is not callable
    # # now sum is considered as variable instead of built-in function

    # solution
    numbers_list = [9, 2, 15]
    new_list = list(range(5))
    print(numbers_list, new_list)

    max_score = 100
    print(max([4, 7, 2]))

    greeting = "hello world"
    num_as_text = str(42)
    print(greeting, num_as_text)

    total_score = 100
    print(sum([1, 2, 3]))
