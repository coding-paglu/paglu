# data Series
'''
0 adi
1 vaibhav
2 bhavik
# one dimemsional array which can hold homogeneous data
'''
# CREATION OF EMPTY SERIES
'''
import pandas as pd
a=pd.Series()
#a=pandas.Series()
print(a)# output: Series([], dtype: float64)
'''

# creation of series with list
# 1 method without using alias
'''
import pandas # pandas is a name of module
a=pandas.Series([10,20,30])# values given in square bracket is called list
print(a) # 0    10
         # 1    20
         # 2    30
         # dtype: int64
'''
#or
'''
import pandas as pd
a=pd.Series(['akshay','taksham','tanu'])
print (a)
'''
#2 method using alias
'''
import pandas as pd
a=pd.Series([10,20,30])# values given in square bracket is called list
print(a)
'''
# 3 Create series putting data on specific index
'''
import pandas as pd
a=pd.Series(['kanan','naina','bhavik'], index=[3,5,1])# values given in square bracket is called list
print(a)
'''
'''
output
   3     kanan
   5     naina
   1    bhavik
dtype: object'''

# 4. Creating series with multiple list and indexing
'''
import pandas as pd
name=['AAA','BBB','CCC']
marks=[90,89,78]
a=pd.Series(name,index=marks)
#a=pd.Series(name)
print(a)
'''
# Indexing
'''
import pandas as pd
a=pd.Series([1002,1004,456,7234],index=[45,48,78,90])
print(a)
'''
# or
'''
import pandas as pd
a=pd.Series(['NEW DELHI','WASHINGTON DC','LONDON'],index=['India','USA','UK'])
print(a)
'''
# 5. Creating Series with range and for loop
'''
import pandas as pd
a=pd.Series(range(2,20,3), index=[i for i in 'abcdef'])
print(a)# if abcdef is not matching with 2,5,8,11,14,17 then error will come
'''
'''
output
a     2
b     5
c     8
d    11
e    14
f    17
dtype: int64
'''

# 6. Creating Series with floating value
'''
import pandas as pd
a=pd.Series([2,20,'aa'])# will convert all the values in float
print(a)
'''

'''
output
0     2.0
1    20.0
2     3.5
dtype: float64
'''
# 7. Creating a series with missing values(NaN)Not a Number
    # NaN is an attribute of Numpy
'''
import pandas as pd
import numpy as np
a=pd.Series([10,45,34,8.5,np.NaN,30])
print(a)
'''
''' Output
0    10.0
1    45.0
2    34.0
3     8.5
4     NaN
5    30.0
dtype: float64
'''
# 8 Assessing specific values by specifying index values
'''
import pandas as pd
a=pd.Series(['NEW DELHI','WASHINGTON DC','LONDON'],
            index=['India','USA','UK'])
print(a[1],a[0])
print(a['India'])
'''

    # 0   india   new delhi
    #1   usa       washington

# output : WASHINGTON DC





# or

# if the value in double square bracket contains string then we can
#use index position like[1,2] whereas if it is numeric the double
#square bracket should include same index value as[11,12],
#if index=[11,12,13]
# Note data is fetched only through index

'''
import pandas as pd
a=pd.Series(['NEW DELHI','WASHINGTON DC','LONDON'],index=['India','USA','UK'])
print(a[[1,2]])# two square brackets are used to display country and capital
# [[ ]] means both index and data will be displayed
'''
''' output
USA    WASHINGTON DC
UK            LONDON
dtype: object
'''
# or
'''
import pandas as pd
a=pd.Series(['NEW DELHI','WASHINGTON DC','LONDON'],
index=['India','USA','UK'])
print(a[['USA','UK']])# two square brackets
'''
'''
output
USA    WASHINGTON DC
UK            LONDON
dtype: object
'''
#------------------------------
# 9.iloc[] and loc[] indexing functions
# iloc- default index,will exclude last value,indexing based on
# position
# loc- exact index,will include all values, indexing based on name
'''
import pandas as pd
a=pd.Series([11,12,13,14],index=[45,48,78,90])
# 0=45, 1=48, 2=78, 3=90
#print(a.iloc[1:3])# default index
print(a.loc[45:90])#  exact index will include all index from 45-90
'''
# 10.Creating series with scalar constant

'''
import pandas as pd
a=pd.Series(77,index=[45,48,78,90])
print(a)
'''

# 11.Creating series with string as constant
'''
import pandas as pd
a=pd.Series('Good morning',index=[45,48,78,90])
print(a)
'''
# 12. Creating series using dictionary
'''
import pandas as pd
dict1={1:'naina',2:'bhavik', 3:'roman'}
a=pd.Series(dict1)
print(a)
'''
# 13. Creating series with mathematical expression
'''
import pandas as pd
import numpy as np
a=np.arange(2,10)# starts from 2-9
print(a)
s=pd.Series(data=a+4,index=a)
print(s)
'''
'''output
[2 3 4 5 6 7 8 9]
2     6
3     7
4     8
5     9
6    10
7    11
8    12
9    13
dtype: int32
'''
# 14.Creating series using arrays.....we require numpy
'''
import pandas as pd
import numpy as np
b=np.array([10,20,30,40])
a=pd.Series(b)
print(a)
'''
# or
'''
import pandas as pd
import numpy as np
b=np.array(['kanan','naina','bhavik','roman'])
a=pd.Series(b)
print(a)
'''
# Write a program to create a Series object using
#an ndarray that has elements AT THE GAP OF 5 in the range 30 to 50.

'''
import numpy as np

x = np.arange(30, 50,5)
print("Array from 30 to 50:")
print(x)
'''


# WAP  to modify the existingvalue 5000 by 7000
# WE WILL USE DEFAULT INDEX
'''
import pandas as pd
S1=pd.Series([2000,3000,4000,5000,6000], index=[11,12,31,14,51])
#S1[3]=7000 # DEFAULT INDEX
S1[14]=7000 # USER DEFINED INDEX
print(S1)
'''
# series Attributes
'''
1. Series.index- returns inde of the Series
2. Series.values- Returns ndarray
3. Series.dtype- Returns dtype object of the underlying data
4. Series.shape- Returns tuple of the shape of the underlying data
5. Series.nbytes- Returns number of bytes of the underlying data i.e 1 int = 8 bits
6. Series.ndim - Retutns the number of dimension
7. Series.size - Returns number of elements
8. Series.hasnans- Returns true if there are any Nan
9. Series.empty- Returns true if series is empty
'''
'''
import pandas as pd
a=pd.Series(range(2,20,3), index=[i for i in 'abcdef'])
print(a)
#print(a.index)
#print(a.values)
#print(a.dtype)
#print(a.shape)
#print(a.nbytes)
#print(a.ndim)
#print(a.size)
#print(a.hasnans)
#print(a.empty)
'''
'''
a     2
b     5
c     8
d    11
e    14
f    17
dtype: int64
Index(['a', 'b', 'c', 'd', 'e', 'f'], dtype='object')
[ 2  5  8 11 14 17]
int64
(6,)
48
1
6
False
False
'''
# FETCHING VALUES USINGHEAD AND TAIL

import pandas as pd
S1=pd.Series([2000,3000,4000,5000,6000,8000,5666], index=[1,2,3,4,5,6,7])
print(S1)
print(S1.head())
print(S1.tail())
print(S1.head(2))
print(S1.tail(2))

'''
1    2000
2    3000
3    4000
4    5000
5    6000
dtype: int64
1    2000
2    3000
dtype: int64
4    5000
5    6000
dtype: int64
'''
# mathematical operations using two series
'''
import pandas as pd
S1=pd.Series([2000,3000,4000,5000,6000], index=[1,2,3,4,5])
print(S1)
S2=pd.Series([200,300,400,500,600], index=[1,2,3,4,5])
print(S2)
print(S1+S2)
print(S1-S2)
print(S1*S2)
print(S1/S2)
'''
# Vector operations on Series(operations performed
#on every single value of series)
'''
import pandas as pd
S1=pd.Series([2000,3000,4000,5000,6000], index=[1,2,3,4,5])
print(S1)
print(S1+2)
print(S1**2)
print(S1>2000)
'''
'''
1    2000
2    3000
3    4000
4    5000
5    6000
dtype: int64
1    2002
2    3002
3    4002
4    5002
5    6002
dtype: int64
1     4000000
2     9000000
3    16000000
4    25000000
5    36000000
dtype: int64
1    False
2     True
3     True
4     True
5     True
dtype: bool
'''

# displaying values on the basis of condition
'''
import pandas as pd
S1=pd.Series([2000,3000,4000,5000,6000], index=[1,2,3,4,5])
print(S1)
print(S1[S1==4000])
print(S1[S1<4000])
'''
'''
1    2000
2    3000
3    4000
4    5000
5    6000
dtype: int64
3    4000
dtype: int64
1    2000
2    3000
dtype: int64
'''
# deleting values from series
'''
import pandas as pd
S1=pd.Series([2000,3000,4000,5000,6000], index=[1,2,3,4,5])
print(S1)
print(S1.drop(3))
'''
'''
1    2000
2    3000
3    4000
4    5000
5    6000
dtype: int64
1    2000
2    3000
4    5000
5    6000
dtype: int64
'''
