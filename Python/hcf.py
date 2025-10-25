#Take input from user
num1 = float(input(" Please Enter the First Value  Num1 : "))#24
num2 = float(input(" Please Enter the Second Value Num2 : "))#36

#calculate the HCF of user entered number
while(num2 != 0):#36!=0
    temp = num2#temp=36
    num2 = num1 % num2#num2  =24
    num1 = temp #num1=36

hcf = num1   
#display the result
print("HCF of num1 and num2 is",hcf)


