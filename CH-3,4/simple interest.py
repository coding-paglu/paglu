#program to calculate simple interest
principal=int(input("Enter the principal amount:"))
time=float(input("Enter the time duration in years:"))
if principal<25000:
    rate=5
else:
    rate=8
simple_interest=(principal*rate*time)/100
print("SImple interest= Rs.",simple_interest)
total=simple_interest+principal
print("total amount to be payed= Rs.",total)
