class Resource:
    """Something a customer can book at Match Point: a court or a group class."""

    def __init__(self, resource_id: str, name: str, price: int) -> None:
        if price <= 0:
            raise ValueError("Price can't be 0 or less")
        self.resource_id = resource_id
        self.name = name
        self.price = price

    def __str__(self) -> str:
        return f"{self.resource_id}: {self.name} ({self.price} kr)"


class Court(Resource):
    """A court booked by one customer at a time, per hour."""

    def __init__(self, resource_id: str, name: str, price: int, sport: str) -> None:
        super().__init__(resource_id, name, price)
        self.sport = sport


class GroupClass(Resource):
    """A Group class booked by many customers at a time, based on spot capacity."""

    def __init__(self, resource_id: str, name: str, price: int, day: str, start_hour: int, capacity: int) -> None:
        super().__init__(resource_id, name, price)
        if capacity <= 0:
            raise ValueError("Capacity must be more than 0")
        self.day = day
        self.start_hour = start_hour
        self.capacity = capacity

    def __str__(self) -> str:
        return f"{self.resource_id}: {self.name} ({self.day} {self.start_hour:02}:00, {self.capacity} spots, {self.price} kr)"
