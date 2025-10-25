class Addition:
    # Defininf a constructor
    def __init__(self,x,y,z):
        # with the help of self.xyz 
		# we are initializing instance variable
        self.num1=x
        self.num2=y
        self.num3=z

    def result(self):
        self.num=self.num1+self.num2+self.num3
        print('Output:',self.num)


# Here we create the object for call 
# which calls the constructor
x = int(input("Enter 1st Number"))
y = int(input("Enter 2nd Number"))
z = int(input("Enter 3rd Number"))
Sum = Addition(x,y,z)

# calling the instance method 
# using the object Sum
Sum.result()
