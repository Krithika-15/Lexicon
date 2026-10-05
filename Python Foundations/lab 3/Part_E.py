# Part E - While loops
# 1
print("Q-1")
count = 10
while count >= 0 :
    print(count)
    count -= 1
print()


# 2
print("Q-2")
password = "john@123"
user_input = input("Enter your password : ")
while user_input != password:
    print("Wrong password, Try again")
    user_input = input("Enter your password : ")
print("Login Successful")
print()


# 3
print("Q-3")
menu = ["add", "update", "remove", "delete", "view", "quit"]

user_input = (input(f"Select any menu from the list : {menu} ")).strip().lower()

while user_input != "quit" :
    print(f"You selected : {user_input}")
    user_input = (input(f"Select any menu from the list : {menu} ")).strip().lower()
print()


# 4
print("Q-4")
user_input = float(input("Enter a number (Enter 0 to stop) : "))
total = 0

while user_input :
    total = total + user_input
    print(f"total : {total}")
    user_input = float(input("Enter a number (Enter 0 to stop) : "))

print(f"Final Total : {total}")
print()


# 5
print("Q-5")
user_input = int(input("Guess the secret number (integer) : "))
secret_number = 30

while user_input != secret_number :
    if user_input >= 40 :
        print("Entered value is too big than the secret number. Try again")
        user_input = int(input("Guess the secret number (integer) : "))
    elif user_input >=31 :
        print("Entered value is little bigger than the secret number. Try again")
        user_input = int(input("Guess the secret number (integer) : "))
    elif user_input < 20 :
        print("Entered value is too less than the secret number. Try again")
        user_input = int(input("Guess the secret number (integer) : "))
    elif user_input < 30 :
        print("Entered value is less than the secret number. Try again")
        user_input = int(input("Guess the secret number (integer) : "))

print(f"Congratulations! You found the secret number {secret_number}")
