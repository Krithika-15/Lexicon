# 1, 2, 3
print("Q-1, 2, 3")
class Product:
    tax_rate = 0.25

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def price_with_tax(self):
        return self.price + self.price * self.tax_rate



# Notes :
# Instance attribute - written inside __init__ with self, belongs to one object (for eg : self.name, self.price)
# Class attribute - written directly inside the class body, belongs to class, shared by all objects.



# 4
print("\nQ-4")
product1 = Product("Ikea Table", 1500)
product2 = Product("Chair", 1500)
product3 = Product("Carpet", 1500)
product4 = Product("Lamp", 2500)
print("All products have same 0.25 tax")
for product in [product1, product2, product3, product4]:
    print(f"Product Name : {product.name}\nProduct Tax rate : {product.tax_rate}\nPrice without tax : {product.price}\nPrice with tax : {product.price_with_tax()}\n")


# 5
print("\nQ-5")
Product.tax_rate = 0.35
print("All products have same 0.35 tax")
for product in [product1, product2, product3, product4]:
    print(f"Product Name : {product.name}\nProduct Tax rate : {product.tax_rate}\nPrice without tax : {product.price}\nPrice with tax : {product.price_with_tax()}\n")


# 6
print("\nQ-6")
product1.tax_rate = 0.15
print("Product 1 alone has 0.15 tax and remaining has 0.35 tax")
print(f"Product Class tax rate : {Product.tax_rate}\n")
for product in [product1, product2, product3, product4]:
    print(f"Product Name : {product.name}\nProduct Tax rate : {product.tax_rate}\nPrice without tax : {product.price}\nPrice with tax : {product.price_with_tax()}\n")


