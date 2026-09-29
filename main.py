from matchpoint.customer import Customer
from matchpoint.resource import Court, GroupClass
from matchpoint.booking import Booking
from matchpoint.booking_system import BookingSystem


system = BookingSystem()


while True:
    menu = """
=== Match Point Sports Centre ===
1. Register
2. See courts and classes
3. Book a court or class
4. Exit
"""
    print(menu)
    user_input = input("Choose : ")
    if user_input == "1":
        name = input("Enter your name : ")
        email = input("Enter your email : ")
        try:
            customer = system.register_customer(name, email)
            print(f"Welcome, {customer.name}! Your ID is {customer.customer_id}")
        except ValueError as e:
            print(f"Error : {e}")
    elif user_input == "2":
        for resource in system.resources:
            print(resource)
    elif user_input == "3":
        print("Chose option 3")
    elif user_input == "4" :
        print("Good Bye")
        break
    else:
        print("Invalid option")
