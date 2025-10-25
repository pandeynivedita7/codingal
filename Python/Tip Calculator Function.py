def total_calc(bill_amount, tip_perc=10):
    # Define function to calculate the tip on bill
    total = bill_amount * (1 + 0.01 * tip_perc)
    total = round(total, 2)
    print(f"Please pay ${total}")

# Call with bill amount and tip percentage
total_calc(150, 20)

# You can also call with default tip percentage
# total_calc(150)
