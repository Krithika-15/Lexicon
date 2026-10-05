class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Product : {self.name}, Price : {self.price} SEK"


table = Product("Ikea Table", 2500)
bed = Product("Ikea bed frame", 3000)
sofa = Product("Ikea 3 seater sofa", 6000)
print("Product object before __str__ method gave object's memory location")
# print(table)
# without __str__ method, this prints <__main__.Product object at 0x0000022570356F90>
# Python only knows the class name and memory address, not what the object means.

print("\nProduct object After __str__ method")
print(table)
print(bed)
print(sofa)

result = str(bed)
print("\nstr(bed) gives : ", result)
print(type(result))
