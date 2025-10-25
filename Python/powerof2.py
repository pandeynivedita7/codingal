def power2(number):# fun to reuse
  if number <= 0:#8 1000
      return False
  return (number & (number - 1)) == 0#8 & 7 1000 &and 0111 =0 11=1 or always 0

n = int(input("Enter a number: "))
if power2(n):
    print("\nThe number is a power of 2")
else:
    print("\nThe number is not a power of 2")


