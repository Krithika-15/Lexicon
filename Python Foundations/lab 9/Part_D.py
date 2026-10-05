class User:
    def __init__(self, name):
        self.name = name


class AdminUser(User):
    pass


admin_1 = AdminUser("Alex")

print(f"Is admin user an AdminUser ? {isinstance(admin_1, AdminUser)}")
print(f"Is admin user a User ? {isinstance(admin_1, User)}")
print(f"Is admin user a string ? {isinstance(admin_1, str)}")


# AdminUser IS-A User, because AdminUser(User) inherits from User.
# So an AdminUser object is also an instance of User: isinstance() returns True for the parent class too.
# AdminUser is not an instance of str, because AdminUser doesn't inherit from str, so there is no IS-A link.
