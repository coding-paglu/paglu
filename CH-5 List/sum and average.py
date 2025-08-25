#WAP to find the sum and average of all the elements of a list
limit=int(input("Enter the no. of total elements: "))
list1=[]
sum=0
for i in range(limit):
    x=int(input("Enter a number: "))
    list1.append(x)
    sum+=x
avg=sum/limit
print("sum of all the elements in the list","\n",list1,"=",sum)
print("average of all the elements in the list","\n",list1,"=",avg)
