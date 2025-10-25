class student:# students is the class name
	grade = 10
	name = "Penguin"
	
	def introduction(self):# def function funcation introcuction(self parameter) self manaadatory 
		print("Hi I am a student")

	def details(self):# def function name details
		print("My name is", self.name)#My name is prnguin . dot to access something
		print("I study in Grade", self.grade)#i study in grade 10

ob = student()#object name ob class name student
ob.introduction()# methid access introduction
ob.details()#method access details

