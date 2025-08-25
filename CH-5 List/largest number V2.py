#WAP to find the largest element in a list version 2
limit=int(input("Enter the no. of total elements: "))
large=0
list1=[]
for i in range(limit):
    x=int(input("Enter a number: "))
    list1.append(x)
list1.sort()
print("The largest number in the list","\n",list1,"is",list1[-1])

