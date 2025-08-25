limit=int(input("Enter the limit: "))
list1=[]
if limit>0:
    for i in range(1,limit+1):
        num=int(input("Enter a numeric value: "))
        if num!=0 and num%2==0:
            list1.append(num)
    print(list1)
            
    
