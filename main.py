from matchpoint.customer import Customer
from matchpoint.resource import Court, GroupClass
from matchpoint.booking import Booking
from matchpoint.booking_system import BookingSystem

system = BookingSystem()
for resource in system.resources:
    print(resource)

