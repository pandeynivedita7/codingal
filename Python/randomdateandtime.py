import random   # importing module
import time

# Function to generate random date
def getRandomDate(startDate, endDate):
    print("Printing random date between", startDate, "and", endDate)
    
    # Generate random number
    randomGenerator = random.random()
    dateFormat = '%Y/%d/%m'
    
    # Convert start and end dates into time
    startTime = time.mktime(time.strptime(startDate, dateFormat))
    endTime = time.mktime(time.strptime(endDate, dateFormat))
    
    # Generate random time between start and end
    randomTime = startTime + randomGenerator * (endTime - startTime)
    
    # Convert time to date format
    randomDate = time.strftime(dateFormat, time.localtime(randomTime))
    return randomDate

# Display result
print("Random Date =", getRandomDate("1/1/2016", "12/12/2018"))
