# Match Point Sports Centre - Booking System

A small command-line booking system for a sports centre with tennis courts, padel courts and yoga classes. Customers can register, log in, book courts, join classes and manage their own bookings.

## How to run

You need Python 3.10 or newer. From the project folder, run:

    python main.py

## Features

1. Register as a new customer
2. Login with your email
3. See all courts and yoga classes with prices
4. Book a court (choose a court, day and a start hour)
5. Join a yoga class (shows how many spots are left)
6. See my Bookings
7. Cancel one of my bookings
8. Log out
9. Exit

## Booking rules

- You must be registered and logged in to book, join, view or cancel.
- An email can only be registered once.
- The centre is open 07:00-22:00, so a court can start at 7 at the earliest and 21 at the latest.
- The same court can't be booked twice on the same day and hour.
- Each yoga class has 12 spots. You can't join a full class, or the same class twice.
- You can only see and cancel your own bookings.
- You can't have two bookings at the same day and hour (for eg: a court and a yoga class).

## Project structure

- `matchpoint/customer.py` - the Customer class (id, name, email). It also checks that the name and email are valid.
- `matchpoint/resource.py` - courts and yoga classes. Both are a Resource; Court and GroupClass add their own details.
- `matchpoint/booking.py` - the Booking class. It links a customer, a resource, a day and an hour.
- `matchpoint/booking_system.py` - everything happens here, from registration and login to bookings and cancellations.

I kept all the booking rules in `BookingSystem` and all input/print in `main.py`, so that it will be easy when I extend with database and much more.

## Known limitations
- All customers and bookings get deleted once you choose Exit.
- Only one week is hardcoded, with no real dates.
