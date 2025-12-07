# Create Class
class Employee:
  
    # Initializing 
    def __init__(self):
        print('Employee created')#pass
  
    # Calling destructor
    def __del__(self):
        print("Destructor called")
  
def Create_obj():#def a method function reusedability
    print('Making Object...')
    obj = Employee()# cerareting a object
    print('function end...')
    return obj
    del obj
    #obj.Create_obj()# calling function inside function
print('Calling Create_obj() function...')
obj = Create_obj()# call function
print('Program End...')
