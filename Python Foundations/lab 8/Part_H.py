class User:
    def __init__(self, username, email):
        if "@" not in email:
            raise ValueError(f"Invalid email : {email}")
        self.username = username
        self.email = email

    def get_profile(self):
        return f"User : {self.username} ({self.email})"

    def get_email_domain(self):
        domain = self.email.split("@")
        return domain[1]


# AdminUser "is-a" User, an admin is still a user of the system.
# It has a username and email and can use every User method,
# but it also has permissions and admin-only actions like ban_user().

class AdminUser(User):
    def __init__(self, username, email, permissions=None):
        super().__init__(username, email)
        if permissions is None:
            permissions = []
        self.permissions = permissions

    def ban_user(self,ban_username):
        return f"{ban_username} has been banned from Login."

    def get_profile(self):
        return f"User : {self.username} ({self.email}) has permission : {self.permissions}"



# PremiumUser "is-a" User, a premium user is still a user of the system.
# It has a username and email and can use every User method,
# but it also has membership levels that only premium user has access to
class PremiumUser(User):
    allowed_levels = ["Silver", "Gold", "Platinum"]
    def __init__(self, username, email, membership_level):
        super().__init__(username, email)
        self.update_membership(membership_level)

    def update_membership(self, level):
        if level.title() not in self.allowed_levels:
            raise ValueError("Only Silver, Gold, Platinum are allowed")
        self.membership_level = level.title()

    def get_profile(self):
        return super().get_profile() + f" has {self.membership_level} membership"



user_1 = User("John", "john30@gmail.com")
user_2 = User("Alice", "alice30@gmail.com")
admin_user = AdminUser("Harry", "harry03@gmail.com", ["delete_users", "edit_posts"])
admin_user_1 = AdminUser("Hermione", "hermione01@gmail.com", ["grant_access"])
premium_user = PremiumUser("Ron", "ron05@yahoo.com", "Gold")

print("Printing common values present in base class")
for user in [user_1, user_2, admin_user, admin_user_1, premium_user]:
    print(f"{user.username} : {user.email}")

print("\nInheriting parent class method in child class")
for user in [user_1, user_2, admin_user, admin_user_1, premium_user]:
    print(f"Class : {type(user).__name__:<12} {user.username} => {user.get_email_domain()}")

print("\nGet profile method in parent class and overriden in child class")
for user in [user_1, user_2, admin_user, admin_user_1, premium_user]:
    print(f"{user.get_profile()}")


print("\nSubclass specific methods : ")

print("\nUpdating premium user membership using premium_user's own method")
print(f"Before : {premium_user.membership_level}")
premium_user.update_membership("Platinum")
print(f"After : {premium_user.membership_level}")

print("\nBanned user in admin_user's own method")
print(f"{admin_user_1.ban_user(user_2.username)}")

print("\nTesting validation")
try:
    bad_user = User("Johny", "johnygmail.com")
except ValueError as e:
    print(f"Error : {e}")

try:
    premium_user.update_membership("brass")
except ValueError as e:
    print(f"Membership Error in Premium User : {e}")

try:
    upgrade_user = PremiumUser("max", "max4@gmail.com", "Apple")
except ValueError as e:
    print(f"Error : {e}")
