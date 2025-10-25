import pandas as pd
import numpy as np
ser1=pd.Series([1.5,2.5,3,4.5,6,6.0])
print(ser1)
ser2=pd.Series(["India","candan"],name="Countries")
print(ser2)
ser4=pd.Series({"India":"New Delhi","Japan":"Tokyo"})
print(ser4)
print(ser1.head(1))
print(ser1.tail(2))