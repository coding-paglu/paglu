num1=int(input("Enter number 1:"))
num2=int(input("Enter number 2:"))
counter=0
for i in range(num1,num2):
    for x in range(2,i):
        if i%x==0:
            counter+=1
        if counter==0:
            print(i,"is a prime number")
            counter-=1
