age = int(input("Enter your age: "))

if age >= 18:
    nationality = input("Enter your nationality: ")
    if nationality.lower() == "indian":
        print("You are eligible to vote.")
    else:
        print("You must be an Indian citizen to vote.")
else:
    print("You are not old enough to vote.")
