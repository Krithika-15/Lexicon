from matchpoint.customer import Customer
from matchpoint.resource import Court, GroupClass
from matchpoint.booking import Booking
from matchpoint.booking_system import BookingSystem


system = BookingSystem()
current_customer = None


while True:
    menu = """
=== Match Point Sports Centre ===
1. Register
2. Login
3. See courts and classes
4. Book a court or class
5. Exit
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
        email = input("Enter your email : ")
        try:
            current_customer = system.log_in(email)
            print(f"Welcome back, {current_customer.name}!")
        except ValueError as e:
            print(f"Error : {e}")
    elif user_input == "3":
        for resource in system.resources:
            print(resource)
    elif user_input == "4":
        if current_customer is None:
            print("Please log in first")
        else:
            print(f"Booking for {current_customer.name}")
    elif user_input == "5":
        print("Good Bye")
        break
    else:
        print("Invalid option")
