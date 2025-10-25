# Initialize dictionary
test_dict = {'Codingal' : 2, 'is' : 2, 'best' : 2, 'for' : 2, 'Coding' : 1}
  
# printing original dictionary
print("The original dictionary : " +  str(test_dict))# typecasting is a method in whihc we change a dataype to another
#test_dict{} print("str") convert text_dict{} str str(test_dict)
  
# Initialize value 
K = 2
  
# Using loop
# Selective key values in dictionary
count = 0
for key in test_dict:
    if test_dict[key] == K:
        count = count + 1
      
# printing result 
print("Frequency of K is : " + str(count))

