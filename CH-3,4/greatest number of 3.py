num1=int(input("value of number 1:"))
num2=int(input("value of number 2:"))
num3=int(input("value of number 3:"))
if num1>num2 and num1>num3:
    print("number1",num1,"is the greatest number")
elif num1<num2 and num2>num3:
    print("number2",num2,"is the greatest number")
elif num3>num2 and num1<num3:
    print("number3",num3,"is the greatest number")
else:
    print("all numbers all equal")
