#Take input of a string
str1 = input("Please Enter a sentence: ")
total = 1 #initialise

for i in range(len(str1)): 
#loop will run to calculate the length using string operation
    if(str1[i] == ' ' ):
    #condition 1
        total = total + 1

print("Total Number of Words in this String = ", total)

