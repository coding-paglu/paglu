limit=int(input("Enter the limit:"))
a=0
b=1
print(a,b,end=" ")
for i in range(limit):
    print(a+b,end=" ")
    dupe=a
    a=b
    b+=dupe

