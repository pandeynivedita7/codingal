def powerOf4(number):
    count = 0#count will store the number of right shifts (i.e., number of trailing zero bits) before we reach the single set bit 1.
    
    # If only 1 set bit exists
    if (number & (~(number & (number - 1)))):#& and and is true if both condition are true
        #~ invert opposite 1 it will give you 0
        # Count 0 bits before set bit
        while(number > 1):
            number >>= 1#>>= 1 shifts bits right by one, effectively dividing by 2 (floor).
            count += 1
        
        # If count is even return true else false
        if(count % 2 == 0):
            return True
        else:
            return False


number = int(input("Enter your number : "))
if(powerOf4(number)):
    print(number, 'is a power of 4')
else:
    print(number, 'is not a power of 4')