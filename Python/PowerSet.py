def printPowerSet(set, set_size):
    power_set_size = 2**set_size#% ** power2**3=8
    
    for outer in range(0, power_set_size):
        print("{", end="")
        for inner in range(0, set_size):
            # Check if inner-th bit is set in outer
            if (outer & (1 << inner)) != 0:# true condition & true 11 else it is false The left shift `<<` moves the bit to the left by `inner` positions.01 10
                print(set[inner], end=" ")
        print("}")

# Example usage
set = ['a', 'b', 'c']
printPowerSet(set, 3)