# create class
class Vehicle:

    # create init method
    def __init__(self, max_speed, mileage):
        # bind the arguments to instance variables
        self.max_speed = max_speed
        self.mileage = mileage

# Object creation
modelX = Vehicle(240, 18)
modelX1=Vehicle(250,50)

# access the variables
print("Model Max Speed:", modelX.max_speed)#240
print("Model Mileage:", modelX1.mileage)#50
