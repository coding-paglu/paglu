import pandas as pd
import numpy as np
a = pd.Series([1,2,3,4], index=['a','b','c','d'])
b = pd.Series([10,20,30,40], index=['a','b','c','d'])
c = pd.Series([100,200,300,400], index=['a','b','c','d'])

f = pd.DataFrame(a)
print(f)

f = pd.DataFrame([a,b,c])
print(f)

