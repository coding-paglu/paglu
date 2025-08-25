#WAP to find the largest element in a list
limit=int(input("Enter the no. of total elements: "))
large=0
list1=[]
for i in range(limit):
    x=int(input("Enter a number: "))
    list1.append(x)
    if x>large:
        large=x
print("The largest number in the list","\n",list1,"is",large)

