# Existing frequency dictionary
freq_dict = {"apple": 3, "banana": 5, "orange": 2}

# Element to check
element = "banana"

# Check frequency
if element in freq_dict:
    print(f"{element} occurs {freq_dict[element]} times")
else:
    print(f"{element} not found")
