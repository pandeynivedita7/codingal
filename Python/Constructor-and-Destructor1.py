class Employee:

	# Initializing (Constructor)
	def __init__(self):#memory constructor
		print('Employee created.')

	# Deleting (Destructor)
	def __del__(self):#del method
		print('Destructor called, Employee deleted.')

obj = Employee()#creating obj
del obj#deleting obj

