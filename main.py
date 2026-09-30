from matchpoint.customer import Customer
from matchpoint.resource import Court, GroupClass
from matchpoint.booking import Booking
from matchpoint.booking_system import BookingSystem, DAYS


system = BookingSystem()
current_customer = None


while True:
    menu = """
=== Match Point Sports Centre ===
1. Register
2. Login
3. See courts and classes
4. Book a court
5. Join a yoga class
6. My Bookings
7. Exit
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
            courts = system.get_courts()
            for number, court in enumerate(courts, start=1):
                print(f"{number}. {court}")
            try:
                court_num = int(input("Choose a court number : "))
                if court_num < 1 or court_num > len(courts):
                    raise ValueError("Please choose a court between 1 and 4")
                court = courts[court_num-1]
                for day_no, day in enumerate(DAYS, start=1):
                    print(f"{day_no}. {day}")
                day_num = int(input("Choose a day number : "))
                if day_num < 1 or day_num > len(DAYS):
                    raise ValueError("Please choose a number between 1 and 7")
                day = DAYS[day_num-1]
                starting_hour = int(input("Enter the start hour (7-21) : "))
                new_booking = system.book_court(current_customer, court, day, starting_hour)
                print(f"Booked! {new_booking}")
            except ValueError as e:
                print(f"Error : {e}")

    elif user_input == "5":
        if current_customer is None:
            print("Please log in first")
        else:
            yoga_classes = system.get_classes()
            for number, yoga_class in enumerate(yoga_classes, start=1):
                print(f"{number}. {yoga_class} - {system.spots_left(yoga_class)} left")
            try:
                yoga_class_num = int(input("Choose a yoga class number : "))
                if yoga_class_num < 1 or yoga_class_num > len(yoga_classes):
                    raise ValueError("Please choose a class number between 1 and 7")
                yoga_class = yoga_classes[yoga_class_num-1]
                new_booking = system.join_class(current_customer, yoga_class)
                print(f"Joined! {new_booking}")
            except ValueError as e:
                print(f"Error : {e}")

    elif user_input == "6":
        if current_customer is None:
            print("Please log in first")
        else:
            my_bookings = system.get_bookings_for(current_customer)
            if len(my_bookings) == 0:
                print("You have no bookings yet")
            else:
                for booking in my_bookings:
                    print(booking)

    elif user_input == "7":
        print("Good Bye")
        break
    else:
        print("Invalid option")
