a=int(input("Enter the initial value:"))
b=int(input("Enter the end value:"))
for x in range(a+1,b):
    prime=True
    for y in range(2,x):
        if x%y==0:
            prime=False
            break
    if prime==True:
        print(x,"is a prime number")
            

