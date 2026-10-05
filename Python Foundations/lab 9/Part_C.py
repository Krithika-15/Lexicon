class Printer:
    def __init__(self, brand, paper, ink_level):
        self.brand = brand
        self.paper = paper
        self.ink_level = ink_level

    def display_status(self):
        if self.ink_level < 5:
            return f"{self.brand} is a printer using {self.paper} paper with low ink level {self.ink_level}%"
        return f"{self.brand} is a printer using {self.paper} paper with good ink level {self.ink_level}%"


class Screen:
    def __init__(self, name, brightness):
        self.name = name
        self.brightness = brightness

    def display_status(self):
        if self.brightness >= 90:
            return f"{self.name} is a screen with high brightness {self.brightness}"
        elif self.brightness >= 50:
            return f"{self.name} is a screen with moderate brightness {self.brightness}"
        else:
            return f"{self.name} is a screen with low brightness {self.brightness}"


hp = Printer("HP", "A4", 6)
hp_1 = Printer("HP_1", "A3", 4)
monitor = Screen("Monitor", 90)
monitor_1 = Screen("Monitor_1", 50)
monitor_2 = Screen("Monitor_2", 30)

devices = [hp, hp_1, monitor, monitor_1, monitor_2]
for device in devices:
    print(device.display_status())


# When the loop reaches the method call it just looks whether the object has display_status() method.
# It doesn't look at the class it belong to
# Classes need not have any relationship
# This is called Polymorphism through duck typing, and don't share parent class, they just have same method name
# If an object doesn't have display_status(), Python raises an AttributeError at that point.
