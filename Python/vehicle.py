class Vehicle:
    def __init__(self, name, capacity, fare_per_person):
        self.name = name
        self.capacity = capacity
        self.fare_per_person = fare_per_person

    def total_fare(self):#def display(self)print(self.name)
				#print(self.idnumber)
        return self.capacity * self.fare_per_person


class Bus(Vehicle):
    def total_fare(self):#self.salary = salary
				#self.post = post
        # Adding 10% extra charge for maintenance
        base_fare = super().total_fare()
        return base_fare + (0.10 * base_fare)


# Example usage
school_bus = Bus("School Bus", 50, 15)
print(f"Total Bus Fare: ₹{school_bus.total_fare()}")
