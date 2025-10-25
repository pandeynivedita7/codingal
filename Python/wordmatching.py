# function to check whether 
# first and last character of words match
def match_words(words):# def funname(): use of fun is to define once and use multiple time
	ctr = 0# counter
	lst = []#store data that will not change your orginial list
	for word in words:# for is a loop that will be used for travse syt is for var in range: for i in range words
		if len(word) > 1 and word[0] == word[-1]:# if condition 
			ctr += 1#ctr=ctr+1
			lst.append(word)
	
	print("List of words with first and last character same\n", lst)
	return ctr
	
count = match_words(['abc', 'cfc','xyz', 'aba', '1221'])
print("Number of words having first and last character same:", count)
