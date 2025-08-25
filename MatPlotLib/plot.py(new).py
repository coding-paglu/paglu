import numpy as np
import matplotlib.pyplot as p1
# Line graph
'''
x=np.arange(7)#(0,1,2,3,4,5,6)
y=np.arange(1,20,3)# works like range function
p1.plot(x,y)
p1.show()
'''

#******************
# line graph with labels and title using arange
'''
x=np.arange(7)
y=np.arange(1,20,3)
print(x)
print(y)
p1.xlabel("Data from list x")
p1.ylabel("Data from list y")
p1.title("My PyPlot 1")
p1.plot(x,y)
p1.show()

'''
#******************
#same as above
#line graph with labels and title using list
'''
x=[ 1,2,3, 4,5, 6,7, 8, 9,10]
y=[13,7,2,11,0,17,1,11,22,14]
print(x)
print(y)
p1.xlabel("Overs")
p1.ylabel("Score")
p1.title("IPL 2019")
p1.plot(x,y)
p1.show()
'''

#******************

'''
x=[1,2,3,4,5,6,7,8,9,10]
y=[13,7,2,11,0,17,1,11,22,14]
print(x)
print(y)
p1.xlabel("Overs")
p1.ylabel("Score")
p1.title("IPL 2019")
p1.plot(x,y,'b')# b indicates line of colour as blue
p1.plot(x,y,"g^") # g indicates the points as green colour
p1.show()
'''
#******************

x=[ 1,2,3, 4,5, 6,7, 8, 9,10]
y=[13,7,2,11,0,17,1,11,22,14]
print(x)
print(y)
p1.xlabel("Overs")
p1.ylabel("Score")
p1.title("IPL 2019")
p1.plot(x,y)
p1.plot(x,y,"ro")# points are depicted in red colour round shape
#Player out
p1.plot([4],[11],"b^")#major point is highlighted with arrow mark with blue colour  on point 
p1.show()

#******************
'''
a=np.arange(0,10,0.1)
x=np.cos(a)# moves from peak to valley........high to low
y=np.sin(a) # moves from valley to peak.......low to high
print(x)
print(y)
p1.xlabel("DATA FROM A")
p1.ylabel("DATA FROM B")
p1.title("DATA ALL")
p1.plot(a,x,'b',linewidth=10)
p1.plot(a,y,'r',linewidth=2)
p1.show()
'''

#******************
# to begin
'''
a=np.arange(0,10,0.1)
x=np.cos(a)
y=np.sin(a)
print(x)
print(y)
p1.xlabel("DATA FROM A")
p1.ylabel("DATA FROM B")
p1.title("DATA ALL")
p1.plot(a,x,'b',linewidth=5,linestyle='dashed')#dashed,solid,dashdot,dotted
p1.plot(a,y,'r',linewidth=2)
p1.show()
'''
#******************
# alternative method to display line style
'''
a=np.arange(0,10,0.1)
x=np.cos(a)
y=np.sin(a)
print(x)
print(y)
p1.xlabel("DATA FROM A")
p1.ylabel("DATA FROM B")
p1.title("DATA ALL")
p1.plot(a,x,'b',linewidth=5,linestyle=':')# '-', '--', '-.', ':'
p1.plot(a,y,'r',linewidth=2)
p1.show()

'''        
#******************
'''
a=np.arange(0,10,0.1)
x=np.cos(a)
y=np.sin(a)
print(x)
print(y)
p1.xlabel("DATA FROM A")
p1.ylabel("DATA FROM B")
p1.title("DATA ALL")
p1.plot(x, y, 'y^--', linewidth=1,markersize=8)
p1.show()
'''
#*******************************************
# bar graph
'''
p1.bar([1,2,3,4,5],[6,7,8,9,10])# one list is for x axis and second list is for y axis
p1.show()
'''

#***********************
'''
x=[1,2,3,4,5]
y=[6,7,8,9,10]
p1.xlabel("DATA FROM A")
p1.ylabel("DATA FROM B")
p1.title("DATA ALL")
p1.bar(x,y)
p1.savefig("data.jpg") # here the graph will be saved as data.pdf
p1.show()
'''
#***********************
'''
# width of each bar
x=[1,2,3,4,5]
y=[6,7,8,9,10]
p1.xlabel("DATA FROM A")
p1.ylabel("DATA FROM B")
p1.title("DATA ALL")
p1.bar(x,y,width=0.3)#width=0.1 to 0.9
p1.show()
'''
#***********************
'''
# colour of the bar
x=[1,2,3,4,5]
y=[6,7,8,9,10]
p1.xlabel("DATA FROM A")
p1.ylabel("DATA FROM B")
p1.title("DATA ALL")
p1.bar(x,y,width=0.3,color="red")#width =0.1 to 0.9......default colour of bar is blue

p1.show()
'''
#***********************
'''
# bars with different thickness
x=[1,2,3,4,5]
y=[6,7,8,9,10]
p1.xlabel("DATA FROM A")
p1.ylabel("DATA FROM B")
p1.title("DATA ALL")
p1.bar(x,y,width=[0.3,0.2,0.4,0.1,0.5],color="red")#width=0.1 to 0.9
p1.show()
'''
#***********************

'''
# bars with different width and colours
x=[1,2,3,4,5]
y=[6,7,8,9,10]
p1.xlabel("DATA FROM A")
p1.ylabel("DATA FROM B")
p1.title("DATA ALL")
p1.bar(x,y,width=[0.3,0.2,0.4,0.1,0.5],color=["red","black","b","g","y",])#width=0.1 to 0.9
p1.show()
'''
#***********************
'''
x=np.arange(0,10,2)
y=[6,7,8,9,10]
p1.xlabel("DATA FROM A")
p1.ylabel("DATA FROM B")
p1.title("DATA ALL")
p1.bar(x,y,width=0.2,color="b")
p1.bar(x+0.3,y,width=0.2,color="r")
p1.show()
'''
#***********************
'''
x=np.arange(4)
v=[[6,7,8,9],[5,6,7,8],[7,8,9,10]]# [6,7,8,9],  ARE SAY MARKS OF ENG FOR EXAMPLE CHILD 1 HAS SCORED 6 IN ENG, CHILD 2 SCORED 7,CHILD 3 SCORED 8 , CHILD 4 SCORED 9
# [5,6,7,8,9] SAY FOR HINDI
# [ 7,8,9,10] SAY FOR MATHS
p1.xlabel("DATA FROM A")
p1.ylabel("DATA FROM B")
p1.title("DATA ALL")
p1.bar(x+0.00,v[0],width=0.2,color="y")# ENGLISH
p1.bar(x+0.25,v[1],width=0.2,color="b")# HINDI
p1.bar(x+0.50,v[2],width=0.2,color="r") # MATHS
p1.show()
'''
#****************************
# PIE CHART
'''
x=np.arange(10,100,20)# 10, 30, 50, 70, 90
L=["A","B","C","D","E"]
p1.title("DATA ALL")
#p1.pie(x)
p1.pie(x,labels=L)
p1.show()
'''
#***********************

'''
x=np.arange(10,100,20)
print(x)
L=["Python","PHP","CSS","C++","HTML"]
mcolor=['red','black','pink','yellow','silver']
p1.title("DATA ALL")
p1.pie(x,labels=L,colors=['red','black','pink','yellow','silver'])
p1.show()
'''

#***********************
'''
#or
x=np.arange(10,100,20)
print(x)
L=["Python","PHP","CSS","C++","HTML"]
mcolor=['red','black','pink','yellow','silver']
p1.title("DATA ALL")
p1.pie(x,labels=L,colors=mcolor)
p1.show()
#***********************
'''
'''
x=np.arange(10,100,20)
print(x)
L=["Python","PHP","CSS","C++","HTML"]
mcolor=['red','black','pink','yellow','silver']
p1.title("DATA ALL")
p1.pie(x,labels=L,colors=mcolor,autopct="%3d%%")
p1.show()
'''
#***********************
'''
x=np.arange(10,100,20)
print(x)
L=["Python","PHP","CSS","C++","HTML"]
mcolor=['red','black','pink','yellow','silver']
p1.title("DATA ALL")
p1.pie(x,labels=L,colors=mcolor,autopct="%03d%%")
p1.show()
'''
#***********************
'''
x=np.arange(10,100,20)
print(x)
L=["Python","PHP","CSS","C++","HTML"]
mcolor=['red','black','pink','yellow','silver']
p1.title("DATA ALL")
p1.pie(x,labels=L,colors=mcolor,autopct="%05.3f%%")
p1.show()
'''
#***********************
'''
x=np.arange(10,100,20)
print(x)
L=["Python","PHP","CSS","C++","HTML"]
mcolor=['red','black','pink','yellow','silver']
p1.title("DATA ALL")
p1.pie(x,labels=L,colors=mcolor,autopct="%05.3f%%",explode=[0,0.2,0,0.5,0])
p1.show()

'''
#*********************
#A histogram is a graphical display of data using bars of different heights
#In histogram, each bar groups members into ranges. Taller bars show that more data falls
#in that range

# difference between bar and histogram
#Bar chart represents a single value whereas Histogram represents range of value

'''
p1.hist([1,4,7,12,13,15],bins=[1,5,10,15])
# [1,4,7,12,13,15]  are the values which are to be adjusted as per the range

#  [1,5,10,15] is the range i.e. 1-5, 6-10,11-15
# 1-5 (2 elements), 6-10 (1 element),11-15 (3 element)

p1.show()
'''
# histogram with default bin value
'''
#randn()- function creates an array of specified
#shape and fills it with random values as per standard normal distribution
y=np.random.randn(1000)
p1.hist(y)
p1.show()
# this graph is called as normal distribution curve as it has bell shape.
# by default the histogram can draw only 10 bars so the bin value is 10
# bin value can be customised
'''
#**********************

#histogram with changed bin value
'''
y=np.random.randn(1000)
p1.hist(y,25) # bins=25
p1.show()
# very fine grained bar will appear

'''
#**********************
# histogram with well defined edge
'''
y=np.random.randn(1000)
p1.hist(y,25, edgecolor="red") # bins=25
p1.show()
'''
#*********************************
# histogram with  number of students lying in the same weight range
'''
y=[5,15,25,35,15,55]
p1.hist(y, bins=[0,10,20,30,40,50,60],weights=[20,10,45,33,6,8],edgecolor="red")
p1.show()

'''
# histogram with different color and labels
'''
y=[5,15,25,35,15,55]
p1.hist(y, bins=[0,10,20,30,40,50,60],weights=[20,10,45,33,6,8],
        edgecolor="red",facecolor='c')
p1.title("histogram for students")
p1.xlabel('Value')
p1.ylabel('Frequency')
p1.savefig('student.png')
p1.show()
'''
'''
x=np.arange(3)
v=[[92,87,95],[82,89,88],[72,87,97]]# [6,7,8,9],  ARE SAY MARKS OF ENG FOR EXAMPLE CHILD 1 HAS SCORED 6 IN ENG, CHILD 2 SCORED 7,CHILD 3 SCORED 8 , CHILD 4 SCORED 9
# [5,6,7,8,9] SAY FOR HINDI
# [ 7,8,9,10] SAY FOR MATHS
#p1.xlabel("DATA FROM A")
#p1.ylabel("DATA FROM B")
p1.title("DATA ALL")
p1.bar(x+0.00,v[0],width=0.2,color="y")# ENGLISH
p1.bar(x+0.25,v[1],width=0.2,color="b")# HINDI
p1.bar(x+0.50,v[2],width=0.2,color="r") # MATHS
p1.show()
p
'''
'''
import pandas as pd
def df_operations():
    dt=({'Name':['Akshit','Bharat','Chetan','Dhaval','Gaurang'],
         'English':[74,79,48,53,68],
         'Physics':[76,78,80,76,73],
         'Chemistry':[57,74,55,89,70],
         'Biology':[76,85,63,68,59],
         'IP':[82,93,69,98,79]})
    df=pd.DataFrame(dt)
    print(df[1:])
df_operations()
'''
'''
a=[2,9,20,25,30]
b=[12,24,25,27,29]
p1.plot(a,b)
p1.xticks(a)
p1.show()
'''


