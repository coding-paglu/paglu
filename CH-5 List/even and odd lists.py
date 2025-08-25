limit=int(input("Enter the no. of total elements: "))
even=[]
odd=[]
for i in range(limit):
    x=int(input("Enter a number: "))
    if x!=0:
        if x%2==0:
            even.append(x)
        else:
            odd.append(x)
print("list containing even numbers ",even,sep="\n")
print("list containing odd numbers ",odd,sep="\n")

            
    
