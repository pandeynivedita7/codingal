weather=(2,0,0,0,2,2,0,2,2)# create a tuple(Sunny, Rainy, Rainy, Rainy, Sunny, Sunny, Rainy)
sunny=0# var name sunny and rainy with value 0
rainy=0
for i in range(0,7):# using for loop to travel from start 0 end 7
	if(weather[i]==0):# using if condition (true)
		rainy+=1# rainy=rainy+1 counter 4
	else:
		sunny+=1#sunny=sunny+1 3

if(sunny>rainy):
	print("Good weather")
else:
	print("Bad weather")