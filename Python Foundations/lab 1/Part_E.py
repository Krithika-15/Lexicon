#Part E - Applied Challenge : Registration summary

# 1
print("Q-1")
first_name = input("Enter your first name : ")
last_name = input("Enter your last name : ")
city = input("Enter your city : ")
year_of_birth = input("Enter your year of birth : ")
favourite_programming_language = input("Enter your favourite programming language : ")
print(f"You are {first_name} {last_name} from {city} with birth year as {year_of_birth} and your favourite programming language is {favourite_programming_language} !")
print()


#2
print("Q-2")
first_name = first_name.strip()
last_name = last_name.strip()
city = city.strip()
print(f"Normalized -> First Name : '{first_name}', Last Name : '{last_name}', City : '{city}'")
print()


# 3
print("Q-3")
birth_year = int(year_of_birth)
customer_id = first_name[0:2].upper() + last_name[:2].upper() + str(birth_year)
print(f"Your ID : {customer_id}")
print()


# 4
print("Q-4")
print("Triple quotes let's us write strings that span multiple lines, using either three single quotes or three double quotes")
summary = f"""
--------- REGISTRATION SUMMARY ---------
Name        : {first_name} {last_name}
City        : {city}
Birth Year  : {birth_year}
User Id     : {customer_id}
----------------------------------------
"""
print(summary)
print()


#5
print("Q-5")
full_name = first_name + last_name
print(f"Length of Fullname : {len(full_name)}")
print(f"Initials : {first_name[0].upper()}{last_name[0].upper()}")
print(favourite_programming_language[::-1])
print()


# 6 considering values from above question 4
print("Q-6")
current_year = 2026
age = current_year - birth_year
birth_decade = (birth_year // 10) * 10
print(f"Your age is {age}")
print(f"You were born in the {birth_decade}s")
new_mail = first_name + last_name[:2] + str(age) +"@lexicon"
print(f"Your generated mail : {new_mail}")
