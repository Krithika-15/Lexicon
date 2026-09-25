from matchpoint.customer import Customer

harry_customer = Customer("C1", "Harry Potter", "harry01@gmail.com")
print(harry_customer)

max_customer = Customer("C3", "Max ", "MAX@GMAIL.COM")
print(max_customer)


try:
    ron_customer = Customer("C2", "  ", "ron@gmail.com")
except ValueError as e:
    print(f"Error : {e}")

try:
    jack_customer = Customer("C4", "Jack ", "jackgmail.com")
except ValueError as e:
    print(f"Error : {e}")

try:
    emma_customer = Customer("C5", "Emma", "emma@gmailcom")
except ValueError as e:
    print(f"Error : {e}")


