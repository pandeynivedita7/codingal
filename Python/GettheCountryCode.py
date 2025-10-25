country_code = {'India' : '0091',
                'Australia' : '0025',
                'Nepal' : '00977'}# string '' "" \n special char for new line
 
# search dictionary for country code of India
print("Country code for India -")
print(country_code.get('India', 'Not Found'))
 
# search dictionary for country code of Japan
print("Country code for Japan -")
print(country_code.get('Japan', 'Not Found'))