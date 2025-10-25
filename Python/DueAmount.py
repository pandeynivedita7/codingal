# Input total bill amount
total_bill = float(input("Enter the total bill amount: ₹"))

# Input amount paid by the customer
amount_paid = float(input("Enter the amount paid by the customer: ₹"))

# Calculate due amount
due_amount = total_bill - amount_paid

# Display the result
if due_amount > 0:
    print(f"The customer still owes ")
elif due_amount < 0:
    print(f"Customer has overpaid ₹. Please return the excess.")
else:
    print("The bill is fully paid. No due amount.")
