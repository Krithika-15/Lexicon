# 1
def log_event(event_type, *messages, **metadata):
    data = {"user action" : event_type, "messages" : list(messages)}
    data.update(metadata)
    return data
print("Q-1")
event_1 = log_event("Login", "User Signed In", "Home Page Loaded", user_id=56, ip="192.168.1.1")
print(event_1)

# 2
def calculate_order(customer, *prices, **options):
    sub_total = sum(prices)
    discount = options.get("discount", 0)  # won/t crash if discount is not available
    shipping_fee = options.get("shipping_fee", 0)  # won't crash if shipping fee is not available
    total = sub_total - (sub_total * discount/100) + shipping_fee
    data = {"name" : customer, "total" : total, "discount" : discount, "shipping_fee" : shipping_fee}
    return data

print("\nQ-2")
order_1 = calculate_order("John", 500, 600, 700, discount = 10, shipping_fee = 100)
print(order_1)


# 3
def calculate_area(width, height):
    return width * height

print("\nQ-3")
area_1 = calculate_area(5, 10)
print(area_1)

def calc_area(**kwargs):
    return kwargs["width"] * kwargs["height"]

area_2 = calc_area(width = 3, height = 5)
print(area_2)
print("""
Named Parameters : def calculate_area(width, height):
- function declaration (signature) tells what's required => no need to read the function body
- while calling the function IDE automcomplete/hints shows width and height by name
- typos are caught immediately: calculate_area(width=5, hieght=10) raises a clear TypeError
- best when the function takes a small, fixed, known set of inputs

**kwargs : def calc_area(**kwargs):
- function declaration (signature) doesn't give any clue about what keys are expected => need to read the function body
- while calling the function no autocomplete hints, any keyword is silently accepted
- a typo like height="hieght" doesn't fail at the call site, it fails later, deep inside the function, with a confusing KeyError instead of a clear TypeError
- best when the set of inputs is genuinely open-ended/unpredictable (e.g. metadata, options)
""")


# 4
print("\nQ-4")

log_1 = log_event("Error", "Payment failed", severity="high", retry_count=3)
log_2 = log_event("Logout")
order_2 = calculate_order("Priya", 250, 150, discount=5)
order_3 = calculate_order("Harry", 1500)

print(log_1)
print(log_2)
print(order_2)
print(order_3)

