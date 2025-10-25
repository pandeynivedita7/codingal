# Taking total amount as input from user
Amount =int(input("Please Enter Amount for Withdraw :"))#565

# Calculating the number of notes of different denominations
note_1 = Amount//100 # floor division use 565//100 5 
note_2 = (Amount%100)//50 # (565%100)//50 65//50 1 
note_3 = ((Amount%100)%50)//10#((565%100)%50)//10 65%50 15//10 1


print( "notes of 100 rupee" , note_1)
print("notes of 50 rupee" , note_2)
print("notes of 10 rupee" , note_3)
