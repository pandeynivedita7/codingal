# Class 1
class BMW:
    def brand(self):
        print("This is BMW")

    def fuel_type(self):
        print("BMW uses Petrol and Diesel engines.")

    def transmission(self):
        print("BMW has Automatic and Manual transmission.")


# Class 2
class Ferrari:
    def brand(self):
        print("This is Ferrari")

    def fuel_type(self):
        print("Ferrari mostly uses Petrol engines.")

    def transmission(self):
        print("Ferrari has Automatic transmission only.")


# Object Creation
car1 = BMW()
car2 = Ferrari()

# Polymorphism in action (same interface for different classes)
for car in (car1, car2):
    car.brand()
    car.fuel_type()
    car.transmission()
