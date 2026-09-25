from matchpoint.customer import Customer
from matchpoint.resource import Court, GroupClass


court_1 = Court("T1", "Tennis Court 1", 250, "tennis")
court_2 = Court("T2", "Tennis Court 2", 250, "tennis")
padel_1 = Court("P1", "Padel Court 1", 400, "padel")
padel_2 = Court("P2", "Padel Court 2", 400, "padel")
yoga_1 = GroupClass("Y1", "Yoga - Morning", 120, "Monday", 7, 12)
yoga_2 = GroupClass("Y2", "Yoga - Evening", 120, "Monday", 18, 12)
yoga_3 = GroupClass("Y3", "Yoga - Weekend", 120, "Saturday", 10, 12)
print(court_1)
print(court_2)
print(padel_1)
print(padel_2)
print(yoga_1)
print(yoga_2)
print(yoga_3)

try:
    bad_court = Court("T2", "Tennis Court 2", 0, "tennis")
except ValueError as e:
    print(f"Error : {e}")

try:
    bad_yoga = GroupClass("Y2", "Yoga - Morning", 120, "Monday", 7, 0)
except ValueError as e:
    print(f"Error : {e}")
