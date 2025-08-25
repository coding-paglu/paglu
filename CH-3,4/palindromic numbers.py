num=int(input("Enter a number:"))
pal=num
reverse=0
while num!=0:
    digit=num%10
    reverse=reverse*10+digit
    num=num//10
if reverse==pal:
    print(pal,"is a palindrome")
else:
    print(pal,"is not a palindrome")
