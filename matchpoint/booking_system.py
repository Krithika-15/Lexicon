from matchpoint.customer import Customer
from matchpoint.resource import Court, GroupClass
from matchpoint.booking import Booking

DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


class BookingSystem:
    """The centre's brain: keeps all customers, resources and bookings, and checks the booking rules."""

    def __init__(self) -> None:
        self.customers = []
        self.resources = []
        self.bookings = []
        self.next_customer_number = 1
        self.next_booking_number = 1

        self.resources.append(Court("T1", "Tennis Court 1", 250, "tennis"))
        self.resources.append(Court("T2", "Tennis Court 2", 250, "tennis"))
        self.resources.append(Court("P1", "Padel Court 1", 400, "padel"))
        self.resources.append(Court("P2", "Padel Court 2", 400, "padel"))
        self.resources.append(GroupClass("Y1", "Yoga - Morning", 120, "Monday", 7, 12))
        self.resources.append(GroupClass("Y2", "Yoga - Evening", 120, "Monday", 18, 12))
        self.resources.append(GroupClass("Y3", "Yoga - Evening", 120, "Tuesday", 18, 12))
        self.resources.append(GroupClass("Y4", "Yoga - Morning", 120, "Wednesday", 7, 12))
        self.resources.append(GroupClass("Y5", "Yoga - Evening", 120, "Thursday", 18, 12))
        self.resources.append(GroupClass("Y6", "Yoga - Morning", 120, "Friday", 7, 12))
        self.resources.append(GroupClass("Y7", "Yoga - Weekend", 120, "Saturday", 10, 12))

    def register_customer(self, name: str, email: str) -> Customer:
        customer = Customer(f"C{self.next_customer_number}", name, email)
        for existing_customer in self.customers:
            if existing_customer.email == customer.email:
                raise ValueError("Email already registered")
        self.customers.append(customer)
        self.next_customer_number += 1
        return customer

    def log_in(self, email: str) -> Customer:
        email = email.strip().lower()
        for existing_customer in self.customers:
            if existing_customer.email == email:
                return existing_customer
        raise ValueError("No customer with that email")


