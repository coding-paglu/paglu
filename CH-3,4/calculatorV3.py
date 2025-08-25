choice='yes'
while choice=='yes' or choice=='YES' or choice=='Yes':
    num1=int(input("Enter a number:"))
    num2=int(input("Enter another number:"))
    print("which operator would you like to use?")
    print("1.Addition +","2.Subtraction -","3.Multiplication *","4.Division /","5.Floor //","6.Mod %","7.Power **",sep="\n")
    op=input("Enter the operator serial number:")
    if op=="1":
        result=num1+num2
        print(num1,"+",num2,"=",result)
    elif op=="2":
        result=num1-num2
        print(num1,"-",num2,"=",result)
    elif op=="3":
        result=num1*num2
        print(num1,"*",num2,"=",result)
    elif op=="4":
        result=num1/num2
        print(num1,"/",num2,"=",result)
    elif op=="5":
        result=num1//num2
        print(num1,"//",num2,"=",result)
    elif op=="6":
        result=num1%num2
        print(num1,"%",num2,"=",result)
    elif op=="7":
        result=num1**num2
        print(num1,"**",num2,"=",result)
    else:
        print("Invalid selection,Choose a operator number from 1-7")
    choice=input('Do you want to continue? Yes or No?:')
    while choice not in ["YES","yes","Yes","no","No","NO"]:
        print("Invalid choice,Try again")
        choice=input('Do you want to continue? Yes or No?:')
    if choice=="no" or choice=="No" or choice=="NO":
        print("Thank You for using a calculator made by Divyam Shrivastav")
