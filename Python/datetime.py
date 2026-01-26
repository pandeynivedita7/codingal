import datetime

now = datetime.datetime.now()
formatted_date = now.strftime("%d-%m-%Y")
print("Formatted Date:", formatted_date)


import datetime

month = datetime.datetime.now().month
print("Current Month Number:", month)

import calendar

year = 2025
month = 1

print(calendar.month(year, month))
