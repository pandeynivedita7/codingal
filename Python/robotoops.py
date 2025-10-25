# Robot Introduction using OOPs

class Robot:
    # Constructor to initialize robot details
    def __init__(self, name, model, purpose):
        self.name = name
        self.model = model
        self.purpose = purpose

    # Method to introduce the robot
    def introduce(self):
        print(f"🤖 Hello! I am {self.name}.")
        print(f"My model is {self.model}.")
        print(f"My main purpose is {self.purpose}.")

# Create robot objects
robot1 = Robot("RoboMax", "RX-101", "Helping with household chores")
robot2 = Robot("EduBot", "ED-202", "Teaching coding to students")

# Introduce the robots
robot1.introduce()
print()
robot2.introduce()
