class Customer:
    """A registered person at Match Point who can book courts and yoga class spots."""

    def __init__(self, customer_id: str, name: str, email: str) -> None:
        if not name.strip():
            raise ValueError("Name can't be empty")
        if not any(ch.isalpha() for ch in name):
            raise ValueError("Name must contain at least one character")
        if "@" not in email or "." not in email:
            raise ValueError("Invalid email address")
        self.customer_id = customer_id
        self.name = name.strip().title()
        self.email = email.strip().lower()

    def __str__(self) -> str:
        return f"{self.customer_id}: {self.name} ({self.email})"
