num=int(input("Enter a number:"))#read a number
count=0            #make a empty variable
for i in range(1,num+1):#from 1 and includes num
    if num%i==0:
        count+=1
if count==2:
    print(num,"is a prime number")
else:
    print(num,"is not a prime number")
