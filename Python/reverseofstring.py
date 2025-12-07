#Input a word or sentence
string1 = input("Please enter your own String : ")# abc

string2 = ('')# this is nothing empty result
#loop for printing in reverse 
for i in string1:# traverse each character
    string2 = i + string2# adding and string cont
    
print("\nThe Original String = ", string1)
print("The Reversed String = ", string2)

# abc reverse cba