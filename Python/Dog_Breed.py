# create class
class Dog:
    # class variable
    species = "Canis familiaris"

    # instance variables
    def __init__(self, breed, name):
        self.breed = breed
        self.name = name
  

# create two dog objects
dog1 = Dog("Labrador Retriever", "Buddy")
dog2 = Dog("German Shepherd", "Max")

