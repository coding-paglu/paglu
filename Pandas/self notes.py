import pandas as pd;
import numpy as np;
##a="Hello,World!"
##while a!=2:
##    print(a)
##    print("Bye, World!")
##for i in "a b c d e f":
##    print(i)
##a=pd.Series(range(2,20,3),index=[i for i in "abcdef"])
##print(a)
##a=pd.Series([2,20,13.3])
##print(a)
##a=pd.Series([2,20,13.3,"test"])
##print(a)
##a=pd.Series([2,20,13,np.nan])
##print(a)
##nan is a float value
a=pd.Series(["New delhi","Washington DC",'London'],index=['India','USA','UK'])
##print(a[1],a[0],a['India'])
print(a[[1,2]])
print(a[["India"]])
##a=pd.Series([11,12,13,14,15],index=[45,48,42,78,90])
##print(a.iloc[1:3])
##print(a.loc[48:90])
##a=pd.Series(77,index=[1,2,3,4])
##print(a)
