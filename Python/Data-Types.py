name = "NIvedita"# name variable container for storage string str
age = 15# integer int
is_student = True# boolean boolean
weight = 38.5# float float
#type(varname)
print("Name :", name)# type(varname) 
print("Data Type of Name is", type(name))#type(varname)
print("Age :", age)
print("Data Type of Age is", type(age))
print("is_student :", is_student)
print("Data Type of is_student is", type(is_student))
print("Weight :", weight)
print("Data Type of weight is", type(weight))

print("\n After Type Casting....")# 1 datatype to another
age = str(age)# datatype(varname) flaot(age)
age=int(age)
print(age)
print("Data Type of age is", type(age))
weight = int(weight)
print(weight)
print("Data Type of Weight is", type(weight))
