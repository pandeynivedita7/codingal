car1 = int(input("Enter the speed of car 1: "))
car2 = int(input("Enter the speed of car 2: "))
car3 = int(input("Enter the speed of car 3: "))

# Correct average calculation
avg = (car1 + car2 + car3) / 3
print("The average speed of the three cars is:", avg)

# Now compare average with individual car speeds
if avg > car1 and avg > car2 and avg > car3:
    print("Average speed is greater than all car speeds.")
elif avg > car1 and avg > car2:
    print("Average speed is greater than car1 and car2.")
elif avg > car1 and avg > car3:
    print("Average speed is greater than car1 and car3.")
elif avg > car2 and avg > car3:
    print("Average speed is greater than car2 and car3.")
elif avg > car1:
    print("Average speed is greater than car1.")
elif avg > car2:
    print("Average speed is greater than car2.")
elif avg > car3:
    print("Average speed is greater than car3.")
else:
    print("Average speed is not greater than any individual car speed.")
