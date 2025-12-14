def total_calc(bill_amount, tip_perc=10):
    # Define function to calculate the tip on bill
    total = bill_amount * (1 + 0.01 * tip_perc)
    total = round(total, 2)#decimal only till 2 digit
    print(f"Please pay ${total}")#print("please pay",total)

# specify only bill_amount
# default value of tip percentage is used if not provided

total_calc(150, 20)  # Uses 20% tip
# Or use total_calc(150) to use default 10% tip
total_calc(200)     # Uses default 10% tip
