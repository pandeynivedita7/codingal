# take marks as input from user
print("Enter Marks Obtained in 4 Subjects: ")
math = int(input("maths :"))
english = int(input("english :"))
science = int(input("science :"))
hindi = int(input("hindi :"))
games=float(input("ENter the marks in fraction"))

# Let's calculate the percentage of marks
sum = math+english+science+hindi+games
print("sun of math,english,science and hindi")

perc = (sum/500)*100

print(end="Percentage Mark = ")
print(perc)