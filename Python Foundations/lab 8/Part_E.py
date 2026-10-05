class Device:
    def __init__(self, brand, year):
        self.brand = brand
        if year < 0 or year > 2026:
            raise ValueError("Year can't be negative and can't be in future")
        self.year = year
        self.is_active = True


class Laptop(Device):
    def __init__(self, brand, year, ram_gb):
        super().__init__(brand, year)
        self.ram_gb = ram_gb

class Phone(Device):
    def __init__(self, brand, year, storage_gb):
        super().__init__(brand, year)
        self.storage_gb = storage_gb


laptop_1 = Laptop("Dell", 2015, 16)
phone_1 = Phone("Samsung", 2026, 128)

for device in [laptop_1, phone_1]:
    print(f"Device : {device.brand}\nYear : {device.year}\nIs active : {device.is_active}\n")

print(f"Laptop RAM : {laptop_1.ram_gb}")
print(f"Phone storage size : {phone_1.storage_gb}")

print("Following both fails because of year in future and in negative")
# Laptop and Phone have no validation code of their own.
# The check is written once in Device, and both run it through super().__init__().
try:
    laptop_2 = Laptop("HP", 2027, 16)
except ValueError as e:
    print(f"Laptop Error : {e}")

try:
    phone_2 = Phone("Samsung", -1, 128)
except ValueError as e:
    print(f"Phone Error : {e}")
