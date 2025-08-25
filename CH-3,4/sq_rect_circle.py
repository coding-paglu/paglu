choice="yes"
while choice in ["yes","Yes","YES"]:
    print("1.Area and perimeter of a square")
    print("2.Area and perimeter of a rectangle")
    print("3.Area and circumference of a circle")
    opt=int(input("Choose an option:"))
    if opt==1:
        s=int(input("Enter side:"))
        ar=s*s
        peri=4*s
        print("Area =",ar,"Perimeter =",peri)
    elif opt==2:
        l=int(input("Enter length:"))
        b=int(input("Enter breadth:"))
        ar=l*b
        peri=2*(l+b)
        print("Area =",ar,"Perimeter =",peri)
    elif opt==3:
        r=int(input("Enter radius:"))
        ar=22/7*r*r
        circ=2*22/7*r
        print("Area =",ar,"Circumference =",circ)
    else:
        print("Invalid option,Try again")
    choice=input("Do you want to restart?,Yes or No:")
    while choice not in ["no","No","NO","yes","Yes","YES"]:
        print("Invalid choice,Try again")
        choice=input("Do you want to restart?,Yes or No:")
    if choice in ["no","No","NO"]:
        print("Thanks for using this program")
        
