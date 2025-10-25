def  checkIfSame(number1,number2): # function use d to reuse any data 
  # 1 !=0 False
  if((number1 ^ number2)!= 0):# ^ bitwise or operator For each bit position, XOR returns TRue 1 if the bits are different and 0 if they are the same.! not 5 0101 bitwise or  3 0011
    print("numbers are not equal")

  else: #false
    print("both numbers are equal")

number1 = int(input("Enter first number to compare"))# input string convert int
number2 = int(input("Enter second number to compare"))
checkIfSame(number1,number2)
#def funname(par,par):