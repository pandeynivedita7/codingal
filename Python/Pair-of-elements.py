# create a class
class pair_elements:
	
	def twoSum(self, nums, target):#num tuple target find
		# create an empty dictionary
		lookup = {}#store

		# Iterate through the tuple
		for i, num in enumerate(nums):#enumerate gives both the index i and the value num.
			if target - num in lookup:#For each number num, we check if the complement (target - num) is already in the dictionary.
				return (lookup[target - num], i )
			lookup[num] = i

# take input of dum from the user
value = int(input("Enter sum for which you want to make this search : "))
print("index1=%d, index2=%d" % pair_elements().twoSum((10,20,30,40,50,60,70),value))
#Numbers: (10,20,30,40,50,60,70)

#Target = 90

#While looping:

#10 storedO

#20 stored

#30 stored

#40 stored

#At 50 → complement = 90 - 50 = 40 (already in lookup!)

#Returns (index of 40, index of 50) → (3, 4)