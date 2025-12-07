def weather_condition():#without a parameter
    print('The weather is pleasant in:', spring)
    print('The weather is same in', autumn)
    
spring = "autumn"# function inside other function
autumn = spring
weather_condition()

