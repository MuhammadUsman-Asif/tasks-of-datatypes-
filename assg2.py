#part 1 - Boolean Logic - AND, OR, NOT (Easy)

#1. **Library Entry System:**
def can_enter_library(is_member: bool, has_overdue_books: bool) -> bool:
    return is_member and not has_overdue_books

# Example Usage:
print(can_enter_library(True, False))  #  True (Can enter)
print(can_enter_library(True, True))   #  False (Has overdue books)
print(can_enter_library(False, False)) #  False (Not a member)
print(can_enter_library(False, True))  #  False (Not a member, has overdue books)


#2.**Smart Home Lights:**
def should_light_turn_on(is_dark: bool, person_present: bool) -> bool:
    return is_dark or person_present

# Example Usage:
print(should_light_turn_on(True, False))  #  True (It's dark)
print(should_light_turn_on(False, True))  #  True (Someone is in the room)
print(should_light_turn_on(True, True))   #  True (Both conditions met)
print(should_light_turn_on(False, False)) #  False (Neither condition met)

#3.**Email Notification Settings:**
def should_notify(email_alerts_on: bool, inbox_full: bool) -> bool:
    return email_alerts_on and not inbox_full

# Example Usage:
print(should_notify(True, False))  #  True (Notifications enabled, inbox not full)
print(should_notify(True, True))   #  False (Inbox is full)
print(should_notify(False, False)) #  False (Email alerts off)
print(should_notify(False, True))  #  False (Email alerts off, inbox full)

#4.**Weekend Discount Eligibility:**
def get_discount(is_weekend: bool, is_vip: bool) -> bool:
    return is_weekend or is_vip

# Example Usage:
print(get_discount(True, False))  #  True (Weekend discount)
print(get_discount(False, True))  #  True (VIP discount)
print(get_discount(True, True))   #  True (Both conditions met)
print(get_discount(False, False)) #  False (No discount)

#5.**Door Lock System:**
def can_unlock(entered_pin: int, correct_pin: int, is_authorized: bool) -> bool:
    return (entered_pin == correct_pin and is_authorized)

# Example Usage:
print(can_unlock(1234, 1234, True))  #  True (Correct pin & authorized)
print(can_unlock(1234, 5678, True))  #  False (Wrong pin)
print(can_unlock(1234, 1234, False)) #  False (Not authorized)
print(can_unlock(5678, 1234, False)) #  False (Wrong pin & not authorized)

#============================================================================
#part 2 - Boolean Logic - AND, OR, NOT (Medium)

#1. **Online Exam Eligibility:**
def can_take_exam(registered: bool, disqualified: bool) -> bool:
    return registered and not disqualified

# Example Usage:
print(can_take_exam(True, False))  #  True (Registered & not disqualified)
print(can_take_exam(True, True))   #  False (Disqualified)
print(can_take_exam(False, False)) #  False (Not registered)
print(can_take_exam(False, True))  #  False (Not registered & disqualified)

#2.**Smart Sprinkler System:**
def should_sprinkle(is_hot: bool, is_dry: bool, moisture_level: int) -> bool:
    return (is_hot and is_dry) or (moisture_level < 30)

# Example Usage:
print(should_sprinkle(True, True, 40))   #  True (Hot & Dry)
print(should_sprinkle(False, True, 20))  #  True (Moisture < 30%)
print(should_sprinkle(True, False, 25))  #  True (Moisture < 30%)
print(should_sprinkle(False, False, 35)) #  False (Not hot, not dry, moisture >= 30%)

#3.**Theater Booking System:**
def can_book_vip(vip_member: bool, premium_ticket: bool) -> bool:
    return vip_member or premium_ticket

# Example Usage:
print(can_book_vip(True, False))  #  True (VIP member)
print(can_book_vip(False, True))  #  True (Has a premium ticket)
print(can_book_vip(True, True))   #  True (Both conditions met)
print(can_book_vip(False, False)) #  False (Neither condition met)

#4.**Security Camera Activation:**
def should_record(motion_detected: bool, is_night: bool, security_mode: bool) -> bool:
    return (motion_detected and is_night) or security_mode

# Example Usage:
print(should_record(True, True, False))   #  True (Motion detected at night)
print(should_record(False, True, True))   #  True (Security mode is on)
print(should_record(True, False, False))  #  False (Motion detected but not night & no security mode)
print(should_record(False, False, False)) #  False (No motion, not night, security mode off)

#5.**Discount Eligibility Check:**
def get_discount(loyalty_member: bool, amount_spent: float, has_coupon: bool) -> bool:
    return (loyalty_member and amount_spent > 100) or has_coupon

# Example Usage:
print(get_discount(True, 150, False))  #  True (Loyalty member & spent > $100)
print(get_discount(False, 80, True))   #  True (Has a special coupon)
print(get_discount(True, 50, False))   #  False (Loyalty member but spent < $100)
print(get_discount(False, 120, False)) #  False (Not a loyalty member & no coupon)

#================================================================================
#part 3 - Boolean Logic - AND, OR, NOT (Hard)

#1. **Online Multiplayer Game Access:**
def can_play_game(subscription_active: bool, banned: bool, guest_pass: bool) -> bool:
    return (subscription_active and not banned) or guest_pass

# Example Usage:
print(can_play_game(True, False, False))  #  True (Active subscription, not banned)
print(can_play_game(True, True, False))   #  False (Banned)
print(can_play_game(False, False, True))  #  True (Has a guest pass)
print(can_play_game(False, False, False)) #  False (No subscription, no guest pass)

#2. **AI Chatbot Response:**
def should_respond(is_blocked: bool, confidence_score: float) -> bool:
    return not is_blocked and confidence_score > 70

# Example Usage:
print(should_respond(False, 80))  #  True (Not blocked & confidence > 70%)
print(should_respond(True, 90))   #  False (User is blocked)
print(should_respond(False, 65))  #  False (Confidence too low)
print(should_respond(True, 50))   #  False (Blocked & low confidence)

#3. **Traffic Light System:**
def should_turn_green(road_clear: bool, emergency_near: bool, manual_override: bool) -> bool:
    return (road_clear and not emergency_near) or manual_override

# Example Usage:
print(should_turn_green(True, False, False))  #  True (Road is clear, no emergency vehicle)
print(should_turn_green(True, True, False))   #  False (Road is clear but emergency vehicle nearby)
print(should_turn_green(False, False, True))  #  True (Manual override is activated)
print(should_turn_green(False, False, False)) #  False (Road not clear, no override)

#4. **Hotel Room Booking:**
def can_book_room(valid_id: bool, has_credit_card: bool, prior_reservation: bool) -> bool:
    return (valid_id and has_credit_card) or prior_reservation

# Example Usage:
print(can_book_room(True, True, False))   #  True (Valid ID and credit card)
print(can_book_room(True, False, True))   #  True (Has prior reservation)
print(can_book_room(True, False, False))  #  False (Valid ID but no credit card or reservation)
print(can_book_room(False, True, False))  #  False (No valid ID)
print(can_book_room(False, False, True))  #  True (Has prior reservation, ID and card don't matter)

#5. **Cybersecurity System:**
def is_login_blocked(ip_blacklisted: bool, correct_password: bool, failed_attempts: int) -> bool:
    return ip_blacklisted or (not correct_password and failed_attempts >= 3)

# Example Usage:
print(is_login_blocked(True, True, 0))   #  True (IP is blacklisted)
print(is_login_blocked(False, False, 3)) #  True (Wrong password & 3+ failed attempts)
print(is_login_blocked(False, False, 2)) #  False (Wrong password, but only 2 failed attempts)
print(is_login_blocked(False, True, 5))  #  False (Correct password, failed attempts don’t matter)
print(is_login_blocked(False, False, 5)) #  True (Wrong password & 3+ failed attempts)

#=============================================================================
#part 4 - OOP - Classes & Objects

#1. **Bank Account Management:**
class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount: float):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds or invalid amount.")

    def get_balance(self):
        return self.balance

# Example Usage:
acc = BankAccount("Alice", 100)
acc.deposit(50)   # Deposited $50. New balance: $150
acc.withdraw(30)  # Withdrew $30. New balance: $120
acc.withdraw(200) # Insufficient funds
print(acc.get_balance())  # Output: 120

#2. **Smartphone Features:**
class Smartphone:
    def __init__(self, brand: str, model: str, battery_level: int = 100):
        self.brand = brand
        self.model = model
        self.battery_level = max(0, min(battery_level, 100))  # Ensuring battery level stays between 0-100

    def charge(self, amount: int = 10):
        self.battery_level = min(100, self.battery_level + amount)
        print(f"Charged {amount}%. Battery level: {self.battery_level}%")

    def use_battery(self, amount: int = 10):
        if self.battery_level - amount >= 0:
            self.battery_level -= amount
            print(f"Used {amount}%. Battery level: {self.battery_level}%")
        else:
            print("Battery too low! Please charge your phone.")

    def get_battery_status(self):
        return f"Battery level: {self.battery_level}%"

# Example Usage:
phone = Smartphone("Apple", "iPhone 14", 50)
phone.use_battery(20)  # Used 20%. Battery level: 30%
phone.charge(50)       # Charged 50%. Battery level: 80%
phone.use_battery(90)  # Battery too low! Please charge your phone.
print(phone.get_battery_status())  # Battery level: 80%

#3. **Food Delivery Order:**
class Order:
    def __init__(self, customer_name: str):
        self.customer_name = customer_name
        self.items = []  # List of tuples (item, price)

    def add_item(self, item: str, price: float):
        self.items.append((item, price))
        print(f"Added {item} - ${price:.2f}")

    def calculate_total(self):
        return sum(price for _, price in self.items)

    def apply_discount(self, discount_percent: float):
        if 0 < discount_percent <= 100:
            discount = self.calculate_total() * (discount_percent / 100)
            return self.calculate_total() - discount
        else:
            print("Invalid discount value.")
            return self.calculate_total()

    def print_receipt(self):
        print(f"\nOrder for {self.customer_name}:")
        for item, price in self.items:
            print(f"- {item}: ${price:.2f}")
        print(f"Total: ${self.calculate_total():.2f}")

# Example Usage:
order = Order("John Doe")
order.add_item("Pizza", 12.99)
order.add_item("Soda", 2.50)
order.print_receipt()  # Prints order details
print(f"Total after 10% discount: ${order.apply_discount(10):.2f}")

#4. **Car Rental System:**
class Car:
    def __init__(self, model: str, rental_price: float):
        self.model = model
        self.rental_price = rental_price

    def rent(self, days: int):
        if days <= 0:
            print("Invalid number of days.")
            return 0
        return self.rental_price * days

    def apply_discount(self, days: int):
        total_cost = self.rent(days)
        if days >= 7:  # Apply discount for long rentals (e.g., 10% off for 7+ days)
            discount = total_cost * 0.10
            total_cost -= discount
            print(f"Applied 10% discount for long rental. Discounted total: ${total_cost:.2f}")
        return total_cost

    def __str__(self):
        return f"Car Model: {self.model}, Daily Rental Price: ${self.rental_price:.2f}"

# Example Usage:
car1 = Car("Toyota Camry", 40)
print(car1)  # Car Model: Toyota Camry, Daily Rental Price: $40.00

cost = car1.rent(5)
print(f"Total cost for 5 days: ${cost:.2f}")  # Output: $200.00

discounted_cost = car1.apply_discount(10)
print(f"Total cost after discount for 10 days: ${discounted_cost:.2f}")  # Output with discount applied

#5. **Movie Streaming Platform:**
class User:
    def __init__(self, name: str, subscription_type: str):
        self.name = name
        self.subscription_type = subscription_type.lower()  # Convert to lowercase for consistency

    def watch_movie(self, movie: str, is_premium: bool):
        if is_premium and self.subscription_type != "premium":
            print(f"Sorry, {self.name}. '{movie}' is only available for premium users.")
        else:
            print(f"{self.name} is watching '{movie}'.")

    def upgrade_subscription(self):
        if self.subscription_type != "premium":
            self.subscription_type = "premium"
            print(f"{self.name} has upgraded to Premium!")
        else:
            print(f"{self.name} is already a Premium user.")

    def __str__(self):
        return f"User: {self.name}, Subscription: {self.subscription_type.capitalize()}"

#=====================================================================================
# Example Usage:
user1 = User("Alice", "basic")
user2 = User("Bob", "premium")

user1.watch_movie("Inception", is_premium=True)  # Restricted
user1.upgrade_subscription()  # Upgrades to premium
user1.watch_movie("Inception", is_premium=True)  # Now allowed

user2.watch_movie("Avatar", is_premium=False)  # Allowed

#================================================================
#part 5 - OOP - Inheritance
#1. **Animal Sound System:**

class Animal:
    def make_sound(self):
        return "Some generic animal sound"

class Dog(Animal):
    def make_sound(self):
        return "Bark"

class Cat(Animal):
    def make_sound(self):
        return "Meow"

# Example Usage:
animals = [Dog(), Cat(), Animal()]

for animal in animals:
    print(f"{animal.__class__.__name__} makes sound: {animal.make_sound()}")

#2. **E-commerce Platform:**
class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def get_details(self):
        return f"Product: {self.name}, Price: ${self.price:.2f}"

class Electronics(Product):
    def __init__(self, name: str, price: float, warranty: int):
        super().__init__(name, price)
        self.warranty = warranty  # Warranty in months

    def get_details(self):
        return f"{super().get_details()}, Warranty: {self.warranty} months"

class Clothing(Product):
    def __init__(self, name: str, price: float, size: str, color: str):
        super().__init__(name, price)
        self.size = size
        self.color = color

    def get_details(self):
        return f"{super().get_details()}, Size: {self.size}, Color: {self.color}"

# Example Usage:
laptop = Electronics("Laptop", 1200, 24)
tshirt = Clothing("T-Shirt", 25, "M", "Blue")

print(laptop.get_details())  # Product: Laptop, Price: $1200.00, Warranty: 24 months
print(tshirt.get_details())  # Product: T-Shirt, Price: $25.00, Size: M, Color: Blue

#3. **Online Learning System:**
class Course:
    def __init__(self, course_name: str, duration: int):
        self.course_name = course_name
        self.duration = duration  # Duration in weeks

    def get_details(self):
        return f"Course: {self.course_name}, Duration: {self.duration} weeks"

class PythonCourse(Course):
    def __init__(self, duration: int, level: str):
        super().__init__("Python Programming", duration)
        self.level = level  # Beginner, Intermediate, Advanced

    def get_details(self):
        return f"{super().get_details()}, Level: {self.level}"

class DataScienceCourse(Course):
    def __init__(self, duration: int, tools: list):
        super().__init__("Data Science", duration)
        self.tools = tools  # List of tools used (e.g., Pandas, TensorFlow)

    def get_details(self):
        return f"{super().get_details()}, Tools: {', '.join(self.tools)}"

# Example Usage:
python_course = PythonCourse(8, "Intermediate")
ds_course = DataScienceCourse(12, ["Pandas", "Scikit-learn", "TensorFlow"])

print(python_course.get_details())  # Course: Python Programming, Duration: 8 weeks, Level: Intermediate
print(ds_course.get_details())      # Course: Data Science, Duration: 12 weeks, Tools: Pandas, Scikit-learn, TensorFlow

#4. **Company Employee Management:**
class Employee:
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary

    def get_details(self):
        return f"Employee: {self.name}, Salary: ${self.salary:.2f}"

class Manager(Employee):
    def __init__(self, name: str, salary: float, department: str):
        super().__init__(name, salary)
        self.department = department

    def get_details(self):
        return f"{super().get_details()}, Department: {self.department}"

class Developer(Employee):
    def __init__(self, name: str, salary: float, programming_language: str):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def get_details(self):
        return f"{super().get_details()}, Programming Language: {self.programming_language}"

# Example Usage:
manager = Manager("Alice", 90000, "HR")
developer = Developer("Bob", 75000, "Python")

print(manager.get_details())  # Employee: Alice, Salary: $90000.00, Department: HR
print(developer.get_details())  # Employee: Bob, Salary: $75000.00, Programming Language: Python

#5. **Vehicle Types:**
class Vehicle:
    def __init__(self, brand: str):
        self.brand = brand

    def max_speed(self):
        return "Unknown speed"

    def get_details(self):
        return f"Vehicle: {self.brand}, Max Speed: {self.max_speed()}"

class Car(Vehicle):
    def __init__(self, brand: str, horsepower: int):
        super().__init__(brand)
        self.horsepower = horsepower

    def max_speed(self):
        return f"{self.horsepower * 2} km/h"  # Example formula for speed estimation

class Bike(Vehicle):
    def __init__(self, brand: str, type_: str):
        super().__init__(brand)
        self.type = type_  # Example: Mountain, Road, Sports

    def max_speed(self):
        return "30 km/h" if self.type == "Mountain" else "50 km/h"

# Example Usage:
car = Car("Toyota", 150)
bike = Bike("Giant", "Road")

print(car.get_details())  # Vehicle: Toyota, Max Speed: 300 km/h
print(bike.get_details())  # Vehicle: Giant, Max Speed: 50 km/h

