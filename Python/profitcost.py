costprice =int(input("enter the cp: "))
sellingprice =int(input("enter the sp: "))

if(sellingprice>costprice):#true
  print("profit")
  pt=sellingprice-costprice
  print(pt)
else :#false
  print("No profit")