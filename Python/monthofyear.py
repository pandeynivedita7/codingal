import calendar

# Display all months
print("List of months:")

for month in calendar.month_name:
    if month:  # skip empty string at index 0
        print(month)
