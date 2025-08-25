#WAP to read a list and find their median
limit=int(input("Enter the no. of total elements: "))
list1=[]
#[1,2,3,4,5,6,7,8,9,10]
for i in range(limit):
    x=int(input("Enter a number: "))
    list1.append(x)
list1.sort()
if limit%2==0:
    mid1=list1[int((limit/2)-1)]
    mid2=list1[int(limit/2)]
    print("median =",mid1,mid2)
else:
    mid=list1[int(limit/2)]
    print("median =",mid)

    
    
