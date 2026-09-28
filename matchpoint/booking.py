from matchpoint.customer import Customer
from matchpoint.resource import Resource


class Booking:
    """Links who (customer), what (court or class) and when (day and hour)."""

    def __init__(self, booking_id: str, customer: Customer, resource: Resource, day: str, start_hour: int) -> None:
        self.booking_id = booking_id
        self.customer = customer
        self.resource = resource
        self.day = day
        self.start_hour = start_hour

    def __str__(self) -> str:
        return f"{self.booking_id}: {self.resource.name}, {self.day} {self.start_hour:02}:00 ({self.resource.price} kr)"

