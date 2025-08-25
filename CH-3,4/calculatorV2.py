choice='yes'
while choice=='yes' or choice=='YES' or choice=='Yes':
    num1=int(input("Enter a number:"))
    num2=int(input("Enter another number:"))
    op=str(input("Enter a operator:"))
    if op=="+":
        sum=num1+num2
        print(num1,"+",num2,"=",sum)
    elif op=="-":
        sub=num1-num2
        print(num1,"-",num2,"=",sub)
    elif op=="*":
        mult=num1*num2
        print(num1,"*",num2,"=",mult)
    elif op=="/":
        div=num1/num2
        print(num1,"/",num2,"=",div)
    else:
        print("Invalid operator")
    print('Do you want to continue?')
    choice=input('Yes or no?:')
