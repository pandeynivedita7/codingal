# Program to calculate due amount after bill payment

# Taking the total bill amount
total_bill = float(input("Enter the total bill amount: ₹"))

# Taking the amount paid by the customer
amount_paid = float(input("Enter the amount paid: ₹"))

# Calculating due amount
due_amount = total_bill - amount_paid

# Displaying result
if due_amount > 0:
    print(f"The customer still owes ₹{due_amount:.2f}")
elif due_amount == 0:
    print("The bill is fully paid. No due amount.")
else:
    print(f"Extra payment of ₹{abs(due_amount):.2f} received. Return the excess.")
