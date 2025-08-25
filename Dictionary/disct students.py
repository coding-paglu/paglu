D1={}
n=int(input("Enter the number of students: "))
for i in range(n):
    adm=int(input("Enter admission number: "))
    roll=int(input("Enter roll number: "))
    name=input("Enter name: ")
    percentage=int(input("Enter percentage: "))
    D1[adm]=(name,roll,percentage)
print(D1)
check=int(input("Enter the admission no."))
if check in D1:
    print(D1[check])
    
