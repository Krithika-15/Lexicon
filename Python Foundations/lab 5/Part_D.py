# 1
def show_profile(**info):
    for k, v in info.items():
        print(f"{k} : {v}")

print("Q-1")
data = show_profile(name="john", age=29, city="stockholm")
print()


# 2
print("Q-2")
def create_user(username, **details):
    data = {"username" : username}
    # print(details)  # {'age': 29, 'city': 'stockholm'}
    data.update(details)
    return data

student_data = create_user("john", age=29, city="stockholm", student_status=True)
print(student_data)
print()


# 3
print("Q-3")
def build_product(name, price, **metadata):
    product_data = {"name" : name, "price" : price}
    product_data.update(metadata)
    return product_data

product_details = build_product("Office Chair", 190.50, material="mesh", weight_kg=15.4)
print(f"Product Details : {product_details}")
product_details_1 = build_product("Notebook", 3.50, color="blue", pages=200)
print(f"Product Details : {product_details_1}")
product_details_2 = build_product("Coffee Mug", 8.00, material="ceramic")
print(f"Product Details : {product_details_2}\n")


# 4
print("Q-4")
def filter_settings(**settings):
    print(settings)
    # remove_value = ""  # tried to save in string but only one occurrence of None got removed
    remove_value = []    # to remove all the occurence of None , used list to save the key names
    for k in settings:
        if settings[k] is None:
            # remove_value.update({k:settings[k]})  # wrong way : earlier stored as dictionary but I needed only keyname
            remove_value.append(k)
    for key in remove_value:
        settings.pop(key)
    return settings

data_1 = filter_settings(language="english", autosave=None, font_size=14)
print(data_1)
data_2 = filter_settings(wifi=True, bluetooth=None, brightness=None, location=False)
print(data_2)

print("""
Notes :
- pop(key, default_value) = deletes the key you specified here and returns back deleted key's value.
If key is not available then fallback value (default value) is returned
KeyError unless you give a default

- popitem() = always removes the most recently added key-value pair, and gives you back both the key and value together as a tuple.
KeyError (dict is empty)
""")


# 5
print("Q-5")
def user_details(name, age, is_student, city):
    data = f"{name} is {'a student' if is_student else 'Not a Student'} from city {city} and age is {age}"
    return data


user_data = {"name" : "Harry", "age" : 29, "is_student" : True, "city" : "Stockholm"}
print("""
Note : keys in user_data like name, age etc., should match with parameter names in function
Else will get : TypeError: user_details() got an unexpected keyword argument 'Age'. Did you mean 'age'?
""")
sentence_1 = user_details(**user_data)
print(sentence_1)
sentence_2 = user_details(**{"name" : "Ron", "age" : 29, "is_student" : False, "city" : "Stockholm"})
print(sentence_2)
print("""
- ** in a function definition will take n number of arguments and packs as single dictionary.
- ** in a function call will unpack dictionary while passing so function will get separate values for keyword arguments.
""")

