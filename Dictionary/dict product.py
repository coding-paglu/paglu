products={}
n=int(input("How many products do you want to add? "))
for i in range(n):
    name=input("Enter product name: ")
    price=int(input("Enter price of the product: "))
    products[name]=price
search=input("Enter the product name to search: ")
if search in products:
    print("The price of",search,"is",products[search])
else:
    print("Product not found.")
print(products)
