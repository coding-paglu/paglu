#WAP to find the maximum out of the 3 entered numbers
num1=int(input("Enter value of number 1:"))
num2=int(input("Enter value of number 2:"))
num3=int(input("Enter value of number 3:"))
if num1>=num2 and num1>=3:
    print("maximum number =",num1)
elif num2>=num1 and num2>=num3:
    print("maximum number =",num2)
else:
    print("maximum number =",num3)
