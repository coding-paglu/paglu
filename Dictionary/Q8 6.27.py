D1={}
customer=int(input("Enter the number of customers: "))
for i in range(customer):
    name=input("Enter name: ")
    item=int(input("Enter the number of items bought: "))
    cost=int(input("Enter the total cost of the items: "))
    phone=int(input("Enter your phone number: "))
    D1[phone]=(name,item,cost)
print(D1)
check=int(input("Enter your phone no."))
if check in D1:
    print(D1[check])
