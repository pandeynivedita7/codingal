#take input from user
text = input(("Enter a sentence: "))
text = text.split()
bigWordLen = 0 #initialise

for wrd in text: #iterate loop
  wrdLen = len(wrd) #string operation
  if wrdLen>bigWordLen: #condition 1
    bigWordLen = wrdLen

print("\nLargest Word: ")
for wrd in text: 
  wrdLen = len(wrd)
  if wrdLen==bigWordLen: #condition 2
    print(wrd) #display result
