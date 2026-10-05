class Notification:
    def send(self):
        return f"(Class : {type(self).__name__})  From Parent Class : This is a Notification"


class EmailNotification(Notification):
    def send(self):
        return f"(Class : {type(self).__name__})  From Child Class : This is an Email Notification"


class SMSNotification(Notification):
    def send(self):
        return f"(Class : {type(self).__name__})  From Child Class : This is an SMS Notification"


class TestNotification(Notification):
    pass


notification_1 = Notification()
email_notification = EmailNotification()
sms_notification = SMSNotification()
test_notification = TestNotification()

for notify in [notification_1, email_notification, sms_notification, test_notification]:
    print(notify.send())


# note :
# no __init__ needed if there's nothing to set up

# notification_1 object created from Notification Parent class so uses its own send method
# both email_notification and sms_notification have their own send method so python uses them (overrides parent class's send method),
# and uses parent class's send method only when send method is not available in the child class.

# even though test notification inherited send() method from parent, it is just borrowing
# so the type(self).__name__ shows its own class TestNotification. because object is created from TestNotification class
