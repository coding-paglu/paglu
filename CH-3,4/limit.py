#WAP to display even/odd numbers till a given limit along with their sum
limit=int(input("Enter limit:"))
total=0
for i in range(1,limit+1,2):
    total+=i
    print(i)
print("Total=",total)
    
