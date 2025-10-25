# Parent Class
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        # Base fare = capacity * 100
        return self.capacity * 100


# Child Class
class Bus(Vehicle):
    bus = Vehicle("Volvo", 15, 50)
    print(f"Vehicle Name: {bus.name}, Capacity: {bus.capacity}")
    print("Bus Fare:", bus.fare())
