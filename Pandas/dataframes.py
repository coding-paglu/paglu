#PANDAS DATA FRAME

# Pandas store tabular data using Data Frame.
# a dataframe is a two dimensional labelled data structure having
#rows and columns.
# rows and columns are accessed by their indexes
# both rows and columns contain indexes

# 1.  Creation of empty Data Frame
'''
import pandas as pd
a=pd.DataFrame()
print(a)
'''


#2. Creation of Data Frame from Numpy ndarrays-
#(ndarrays-N dimensional array)
'''
import numpy as np
import pandas as pd
a1=np.array([10,20,30])
a2=np.array([100,200,300])
a3=np.array([-10,-20,-30])
f1=pd.DataFrame(a1)
print(f1)

f2=pd.DataFrame(a2)
print(f2)
print(f1,f2)
'''

# Creating DataFrame with more than 1 ndarray'''
'''
import numpy as np
import pandas as pd
a1=np.array([10,20,30])
a2=np.array([100,200,300])
a3=np.array([-10,-20,-30])
f1=pd.DataFrame([a1,a2,a3],columns=['A','B','C'])
print(f1)
'''

#4. Creating DataFrame from list of Dictionary(multiple dictionaries)
'''
import numpy as np
import pandas as pd
a1=[{'a':10, 'b':20},{'a':5, 'b':15, 'c':20} ]
# keys in dictionary one are a, b.........keys in dictionary 2
#are a,b,c dictionary keys are used as column label
f1=pd.DataFrame(a1)
print(f1)
'''

#5. Creating DataFrame from  Dictionary containg lists
'''
import numpy as np
import pandas as pd
# keys in a dictionary are written before the :
a1={'state':['delhi', 'haryana','assam'],             
    'population':[8990,9995,98765],
    'forestarea':[2797,6.72,9.82]}

f1=pd.DataFrame(a1)
print(f1)
'''
# 6 Creation of Data Frames from Series
'''
import numpy as np
import pandas as pd
a=pd.Series([1,2,3,4], index=['a','b','c','d'])
b=pd.Series([10,20,30,40], index=['a','b','c','d'])
c=pd.Series([100,200,300,400], index=['a','b','c','d'])

f=pd.DataFrame(a)
print(f)

f=pd.DataFrame(b)
#print(f)

f=pd.DataFrame(c)
#print(f)

f=pd.DataFrame([a,b,c])
print(f)
#if single series is passed to create a dataframe then it will be created as series with default calumn 0
#whereas if series are passed as a list then row names will become column heading.

       a    b    c    d
0    1    2    3    4
1   10   20   30   40
2  100  200  300  400
'''

# 7 Creation of Data Frames from Dictionary containing Series

'''
import numpy as np
import pandas as pd
marks={1:pd.Series([99,98,97],index =['eng', 'hindi', 'maths']),
       2:pd.Series([93,78,67],index =['eng', 'hindi', 'maths']),
       3:pd.Series([49,58,77],index =['eng', 'hindi', 'maths'])}
# key :- 1, 2, 3
# keys will work as column headings and eng,hindi,maths will be row headings
# value :- [99,98,97]
# key : value pair ----1: [99,98,97]
#                      2: [93,78, 67]
#                      3:[49,58,77]

f=pd.DataFrame(marks)


print(f)
'''

# Operations

# 7. Adding new Column to Data Frame


'''

import numpy as np
import pandas as pd
marks={1:pd.Series([99,98,97],index =['eng', 'hindi', 'maths']),
       2:pd.Series([93,78,67],index =['eng', 'hindi', 'maths']),
       3:pd.Series([49,58,77],index =['eng', 'hindi', 'maths'])}
f=pd.DataFrame(marks)
print(f)
f[4]=[69,68,47]
print(f)
'''

# 8. Adding a new row to Data Frame
# DataFrame.loc[] method is used to add a row

'''
import numpy as np
import pandas as pd
marks={1:pd.Series([99,98,97],index =['eng', 'hindi', 'maths']),
       2:pd.Series([93,78,67],index =['eng', 'hindi', 'maths']),
       3:pd.Series([49,58,77],index =['eng', 'hindi', 'maths'])}
f=pd.DataFrame(marks)
print(f)
f.loc['computers']=[98,97,96]

print(f)
'''

#9. To set all values of a data frame with specific value
'''
import numpy as np
import pandas as pd
marks={1:pd.Series([99,98,97],index =['eng', 'hindi', 'maths']),
       2:pd.Series([93,78,67],index =['eng', 'hindi', 'maths']),
       3:pd.Series([49,58,77],index =['eng', 'hindi', 'maths'])}
f=pd.DataFrame(marks)
print(f)
f[:]=0
print(f)

'''

# 10.Deleting row or column drom Data Frame
# Dataframe.drop() is used to delete row
# to delete row axis=0, for column axis=1
'''
import numpy as np
import pandas as pd
marks={1:pd.Series([99,98,97],index =['eng', 'hindi', 'maths']),
       2:pd.Series([93,78,67],index =['eng', 'hindi', 'maths']),
       3:pd.Series([49,58,77],index =['eng', 'hindi', 'maths'])}
f=pd.DataFrame(marks)
print(f)

# axis = 0 ----demonstrates horizontal     1= demonstrates vertical


f=f.drop('maths',axis=0)
print(f)
#f=f.drop([1],axis=1)
#print(f)
'''

# 11 Renaming row label
'''
import numpy as np
import pandas as pd
marks={1:pd.Series([99,98,97],index =['eng', 'hindi', 'maths']),
       2:pd.Series([93,78,67],index =['eng', 'hindi', 'maths']),
       3:pd.Series([49,58,77],index =['eng', 'hindi', 'maths'])}
f=pd.DataFrame(marks)
print(f)
f=f.rename({'eng':'sub1','hindi':'sub2','maths':'sub3'},axis='index')
print(f)
'''

# 12 Renaming column label

'''
import numpy as np
import pandas as pd
marks={1:pd.Series([99,98,97],index =['eng', 'hindi', 'maths']),
       2:pd.Series([93,78,67],index =['eng', 'hindi', 'maths']),
       3:pd.Series([49,58,77],index =['eng', 'hindi', 'maths'])}
f=pd.DataFrame(marks)
print(f)
f=f.rename({1:'bhavik',2:'naina',3:'arav'},axis='columns')
print(f)
'''
# 13. Accessing Datas frame elements through indexing
#   two parts   a) Label based indexing
#               b) Boolean indexing

# Label based indexing
# on the basis of row labels
'''
import numpy as np
import pandas as pd
marks={1:pd.Series([99,98,97],index =['eng', 'hindi', 'maths']),
       2:pd.Series([93,78,67],index =['eng', 'hindi', 'maths']),
       3:pd.Series([49,58,77],index =['eng', 'hindi', 'maths'])}
f=pd.DataFrame(marks)
print(f)
print(f.loc['eng'])# exact location of the index onlyi.e row heading
'''
# boolean indexing

'''
import numpy as np
import pandas as pd
marks={1:pd.Series([99,98,97],index =['eng', 'hindi', 'maths']),
       2:pd.Series([93,78,67],index =['eng', 'hindi', 'maths']),
       3:pd.Series([49,58,77],index =['eng', 'hindi', 'maths'])}
f=pd.DataFrame(marks)

print(f)

print(f.loc['eng']>90)  # 99, 93,49.......T,T, F
'''

#14 JOINING  DATA FRAMES
'''
import numpy as np
import pandas as pd
marks1={1:pd.Series([99,98,97],index =['eng', 'hindi', 'maths']),
       2:pd.Series([93,78,67],index =['eng', 'hindi', 'maths']),
       3:pd.Series([49,58,77],index =['eng', 'hindi', 'maths'])}
f1=pd.DataFrame(marks1)
print(f1)
marks2={4:pd.Series([59,57,87],index =['eng', 'hindi', 'maths']),
       5:pd.Series([83,78,67],index =['eng', 'hindi', 'maths']),
       6:pd.Series([66,88,77],index =['eng', 'hindi', 'maths'])}
f2=pd.DataFrame(marks2)
print(f2)

f1=f1.join(f2)# f1=f1.join(f2)
print(f1)
'''
#OR
'''
import numpy as np
import pandas as pd
marks1={1:pd.Series([99,98,97],index =['eng', 'hindi', 'maths']),
       2:pd.Series([93,78,67],index =['eng', 'hindi', 'maths']),
       3:pd.Series([49,58,77],index =['eng', 'hindi', 'maths'])}
f1=pd.DataFrame(marks1)
print(f1)
marks2={1:pd.Series([59,57,87],index =['CS', 'EP', 'PE']),
       2:pd.Series([83,78,67],index =['CS', 'EP', 'PE']),
       3:pd.Series([66,88,77],index =['CS', 'EP', 'PE'])}
f2=pd.DataFrame(marks2)
print(f2)

f1=f1._append(f2)
print(f1)
'''
#15 SORTING (will arrange the column heading in ascending order) 

import numpy as np
import pandas as pd

marks1={1:pd.Series([99,98,97],index =['eng', 'hindi', 'maths']),
       3:pd.Series([93,78,67],index =['eng', 'hindi', 'maths']),
       2:pd.Series([49,58,77],index =['eng', 'hindi', 'maths'])}
f1=pd.DataFrame(marks1)
#print(f1)

marks2={2:pd.Series([59,57,87],index =['CS', 'EP', 'PE']),
       3:pd.Series([83,78,67],index =['CS', 'EP', 'PE']),
       1:pd.Series([66,88,77],index =['CS', 'EP', 'PE'])}
f2=pd.DataFrame(marks2)
#print(f2)
#print('***************')
f1=f1._append(f2)
print(f1)
#print('***************')

f1=f1._append(f2,sort=True)
print(f1)

#16ATTRIBUTES OF PANDAS (total 11)
#1 INDEX- will display name of rows

'''
import pandas as pd
marks={1:pd.Series([99,98,97],index =['eng', 'hindi', 'maths']),
       2:pd.Series([93,78,67],index =['eng', 'hindi', 'maths']),
       3:pd.Series([49,58,77],index =['eng', 'hindi', 'maths'])}
f=pd.DataFrame(marks)
print(f)
print(f.index)

'''

#2 COLUMNS- displays index name of columns
'''
import pandas as pd
marks={1:pd.Series([99,98,97],index =['eng', 'hindi', 'maths']),
       2:pd.Series([93,78,67],index =['eng', 'hindi', 'maths']),
       3:pd.Series([49,58,77],index =['eng', 'hindi', 'maths'])}
f=pd.DataFrame(marks)
print(f)
print(f.columns)
'''
# 3 dtypes- displays data types
'''
import pandas as pd
marks={1:pd.Series([99,98,97],index =['eng', 'hindi', 'maths']),
       2:pd.Series([93,78,67],index =['eng', 'hindi', 'maths']),
       3:pd.Series([49,58,77],index =['eng', 'hindi', 'maths'])}
f=pd.DataFrame(marks)
print(f)
print(f.dtypes)
'''

# 4 values- displays the data rowwise in list
# result is displayed as list in a list
'''
import pandas as pd
marks={1:pd.Series([99,98,97],index =['eng', 'hindi', 'maths']),
       2:pd.Series([93,78,67],index =['eng', 'hindi', 'maths']),
       3:pd.Series([49,58,77],index =['eng', 'hindi', 'maths'])}
f=pd.DataFrame(marks)
print(f)
print(f.values)
'''

# 5 shape-Return a tuple representing the dimensionsof the DataFrame.
'''
import pandas as pd
marks={1:pd.Series([99,98,97],index =['eng', 'hindi', 'maths']),
       2:pd.Series([93,78,67],index =['eng', 'hindi', 'maths']),
       3:pd.Series([49,58,77],index =['eng', 'hindi', 'maths'])}
f=pd.DataFrame(marks)
print(f)
print(f.shape)# will give(no. of rows,no.of columns)
'''

# 6 size- displays total no of elements are in data frame

'''
import pandas as pd
marks={1:pd.Series([99,98,97],index =['eng', 'hindi', 'maths']),
       2:pd.Series([93,78,67],index =['eng', 'hindi', 'maths']),
       3:pd.Series([49,58,77],index =['eng', 'hindi', 'maths'])}
f=pd.DataFrame(marks)
print(f)
print(f.size)  # 3rows x 3 columns=9
'''

# 7 transpose- converting row to column and vice versa
'''
import pandas as pd
marks={1:pd.Series([99,98,97],index =['eng', 'hindi', 'maths']),
       2:pd.Series([93,78,67],index =['eng', 'hindi', 'maths']),
       3:pd.Series([49,58,77],index =['eng', 'hindi', 'maths'])}
f=pd.DataFrame(marks)
print(f)
print(f.T)
'''

# 8 head(n)-displays first n rows
'''
import pandas as pd
marks={1:pd.Series([99,98,97],index =['eng', 'hindi', 'maths']),
       2:pd.Series([93,78,67],index =['eng', 'hindi', 'maths']),
       3:pd.Series([49,58,77],index =['eng', 'hindi', 'maths'])}
f=pd.DataFrame(marks)
print(f)
print(f.head(2))
'''
# 9 tail (n)- displays last n rows
'''
import pandas as pd
marks={1:pd.Series([99,98,97],index =['eng', 'hindi', 'maths']),
       2:pd.Series([93,78,67],index =['eng', 'hindi', 'maths']),
       3:pd.Series([49,58,77],index =['eng', 'hindi', 'maths'])}
f=pd.DataFrame(marks)
print(f)
print(f.tail(2))
'''

# 10 axes-Return a list representing the axes of the DataFrame.
'''
import pandas as pd
marks={1:pd.Series([99,98,97],index =['eng', 'hindi', 'maths']),
       2:pd.Series([93,78,67],index =['eng', 'hindi', 'maths']),
       3:pd.Series([49,58,77],index =['eng', 'hindi', 'maths'])}
f=pd.DataFrame(marks)
print(f)
print(f.axes)
'''

# 11 ndim-Return an int representing the number of axes / array dimensions
'''
import pandas as pd
marks={1:pd.Series([99,98,97],index =['eng', 'hindi', 'maths']),
       2:pd.Series([93,78,67],index =['eng', 'hindi', 'maths']),
       3:pd.Series([49,58,77],index =['eng', 'hindi', 'maths'])}
f=pd.DataFrame(marks)
print(f)
print(f.ndim)# no. of axes
'''



