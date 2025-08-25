limit=int(input("Enter the limit: "))
flag=True
count=0
list1=[]
if limit>0:
    for i in range(limit):
        num=int(input("Enter a numeric value: "))
        list1.append(num)
    check=int(input("Enter a numeric value to be checked: "))
    for i in list1:
        if i==check:
            print(check,"is present in list ")
            flag=False
            break
    if flag==True:
        print(check,"is not present in list")
    
