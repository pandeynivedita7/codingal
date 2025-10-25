class Animal:
 
    def __init__(self, age):
        self.__age = age
 
    def setage(self, age):#set and get function set function when we create a private var and if we wanted to change the vale of private variable we use setter function
        self.__age = age
  
    def getage(self):
        return self.__age
 
 
    def __add__(self, predict):
        return Animal( self.__age + predict.__age )
 
    def __gt__(self, predict):
        return self.__age > predict.__age
 
    def __lt__(self, predict):
        return self.__age < predict.__age
 
    def __str__(self):
        return "Combined age of the two animals " + str(self.__age)
 
c1 = Animal(5)
print(c1.getage())
 
c2 = Animal(6)
print(c2.getage())
 
c3 = c1 + c2# int
print(c3.getage())
 
print( c3 > c2) 
 
print( c1 < c2) 
 
print(c3) #string