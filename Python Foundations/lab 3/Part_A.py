# Part A - Conditions

# 1
print("Q-1")
user_input = int(input("Enter a number : "))
if user_input == 0 :
    print("Number is 0")
elif user_input < 0 :
    print("Number is negative")
elif user_input > 0 :
    print("Number is positive")
print()


# 2
print("Q-2")
age = int(input("Enter your age : "))
if age < 0 : # adding a guard check to skip all the conditions
    print("Not a valid age")
elif age >= 60 :
    print("You are a senior person")
elif age >= 40:
    print("You are a middle aged person")
elif age >= 20:
    print("You are an Adult")
elif age >= 13:
    print("You are a teenager")
else :
    print("Child")
print()


# 3
print("Q-3")
user_name = "john13@gmail.com"
password = "passwordjohn"
user_input = input("Enter your username : ")
user_Password = input("Enter your password : ")

if (user_input == user_name) and (user_Password == password) :
    print("Login Successfull")
elif user_input != user_name :
    print("Username does not match")
elif user_Password != password :
    print("Wrong Password! Please try again")
print()


# 4
print("Q-4")
score = int(input("Enter your score : "))
if score > 100 or score < 0 :
    print("Invalid score enter between range 0 - 100")
elif score >= 90 :
    print("Your grade is S")
elif score >= 80 :
    print("Your grade is A")
elif score >= 70 :
    print("Your grade is B")
elif score >= 60 :
    print("Your grade is C")
elif score >= 50 :
    print("Your grade is D")
elif score >= 40:
    print("Your grade is E")
elif score < 40 :
    print("Sorry You are Failed")
print()


# 5
print("Q-5")
order_total = int(input("Enter Order Total : "))
membership_input = input("Enter membership status (True or False) : ")
membership = membership_input.strip().lower() == "true"

if membership and order_total >= 500:
    print("Will be shipped in 2 days")
elif membership and order_total < 500:
    print("You are a member, standard shipping charges apply")
elif not membership and order_total >= 500:
    print("You are not a member, shipping charges will be 100")
else:
    print("Your order is less than 500 and not a member, shipping charges are based on location")

# bool("False")  # True  ← non-empty string!
# bool("0")      # True  ← non-empty string!
# bool("no")     # True  ← non-empty string!
# bool("")       # False ← only empty string is falsy
print()


# 6
print("Q-6")
print(5 == 5)     # predict: True   (same value)
print(3 != 7)     # predict: True   (different values)
print(10 > 15)    # predict: False  (10 is not bigger than 15)
print(8 < 2)      # predict: False  (8 is not smaller than 2)
print(6 >= 6)     # predict: True   (equal counts for >=)
print(4 <= 3)     # predict: False  (4 is not smaller than or equal to 3)
