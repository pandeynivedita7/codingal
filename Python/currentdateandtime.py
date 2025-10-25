from datetime import date, datetime

# calling the today function of date class
today = date.today()
now = datetime.now()

# Printing today's date
print("Today's date is:", today)

# Printing current date and time
print("\nCurrent Date and Time is:", now)

# Printing date's components
print("\nDate components -> Year:", today.year, " Month:", today.month, " Day:", today.day)

