# Taking total amount as input from user
Amount =int(input("Please Enter Amount for Withdraw :"))# type casting converting 1 data type to another

# Calculating the number of notes of different denominations
note_1 = Amount//100 # floor division fraction value whole number
note_2 = (Amount%100)//50# % modulus give reminder
note_3 = ((Amount%100)%50)//10 


print( "notes of 100 rupee" , note_1)
print("notes of 50 rupee" , note_2)
print("notes of 10 rupee" , note_3)
