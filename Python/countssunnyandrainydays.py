weather = (2,0,0,0,2,2,0,2,2)  
# Tuple representing weather:
# 2 = Sunny, 0 = Rainy
# Example: (Sunny, Rainy, Rainy, Rainy, Sunny, Sunny, Rainy, Sunny, Sunny)

sunny = 0   # Counter for sunny days
rainy = 0   # Counter for rainy days

for i in range(0,9):   # Loop over first 7 days (index 0 to 6)
    if weather[i] == 0:    # If the day is rainy
        rainy += 1
    else:                  # Otherwise, it's sunny
        sunny += 1

# Compare sunny vs rainy days
if sunny > rainy:
    print("Good weather")
else:
    print("Bad weather")
