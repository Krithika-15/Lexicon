# Part C - Strings

# 1
print("Q-1")
sentence = "  Python is a dynamic typing, has no compiler time  "
print(len(sentence))
print(sentence.upper())
print(sentence.lower())
print(sentence.strip())
print()


# 2
print("Q-2")
first_name = input("Enter your first name : ")
last_name = input("Enter your last name : ")
print(f"Fullname is {first_name} {last_name}")
print()


# 3
print("Q-3")
course = "python programming"
print(course[0])
print(course[-1])
print(course[0:6])
print(course[-11:])
print(course[::-1])
print()


# 4
print("Q-4")
first_name = input("Enter your first name : ").strip()
last_name = input("Enter your last name : ").strip()
user_name = (first_name[0:3] + last_name[0:5]).lower()
print(user_name)
print()


# 5
print("Q-5")
user_email = "john34@gmail.com"
address_seperator = user_email.split("@")
user_name = address_seperator[0]
domain = address_seperator[1]
print(f"User name is {user_name}")
print(f"Domain is {domain}")
print()


# 6
print("Q-6")
dynamic_languages = "Java, Ruby, Perl, Lua, Javascript are dynamically typed"
updated_dynamic_languages = dynamic_languages.replace("Java", "Python", 1)
print(f"old : {dynamic_languages}")
print(f"new : {updated_dynamic_languages}")
