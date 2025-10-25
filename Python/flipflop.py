# Function to check whether a tuple is a palindrome or not
def palind(r):# def function part code that can reused def funname (par):
    e = len(r) - 1#string which you read from start or end guve same vale 121
    s = 0# 0 empty
    while s < e:# true
        if r[s] != r[e]:
            return False
        s += 1
        e -= 1
    return True

# Tuple to check
r = (1, 2, 3, 3, 2, 1)

if palind(r):# funname
    print("The Tuple is Flip-Flop")
else:
    print("The Tuple is not Flip-Flop")


