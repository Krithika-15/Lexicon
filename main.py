from matchpoint.customer import Customer
from matchpoint.resource import Court, GroupClass
from matchpoint.booking import Booking


harry = Customer("C1", "Harry Potter", "harry03@gmail.com")
court_1 = Court("T1", "Tennis Court 1", 250, "tennis")
booking_1 = Booking("B1", harry, court_1, "Monday", 10)
print(booking_1)
print(booking_1.customer.name)
