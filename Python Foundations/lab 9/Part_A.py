class EmailNotification:
    def send(self):
        return "This is an Email notification"


class SMSNotification:
    def send(self):
        return "This is an SMS notification"


class PushNotification:
    def send(self):
        return "This is a Push notification"

notifications = [EmailNotification(), SMSNotification(), PushNotification()]

for notify in notifications:
    print(notify.send())


# The loop does not need to know the exact class of each object.
# It only needs every object to have a send() method.
# When notify.send() runs, Python uses the send() that belongs to that object's own class,
# so the same line of code gives a different message for each notification type.

# This is Polymorphism : same method name, different behaviour depending on the object.
# We can also add a new class later for example, WhatsAppNotification with its own send(),
# then put it in the list, and the loop keeps working without any changes.
