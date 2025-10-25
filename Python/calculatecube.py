# Define function to calculate cube
def cube(number):
    return number * number * number #return output

# Define a function which executes cube function only if number is divisible by 3
def by_three(number):
    if number % 3 == 0: #modulus reminder true
        return cube(number)# print statement
    else:
        return False

# Display results
print(by_three(9))  # Should print 729
print(by_three(4))  # Should print False
