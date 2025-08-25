salary=int(input("Enter your salary:"))
gender=input("Enter your gender, male/female:").lower()
if gender=="male" or gender=="m":
    if salary<50000:
        bonus=salary/100*10
        print("You will recieve",bonus,"as bonus")
    elif salary>=50000:
        bonus=salary/100*15
        print("You will recieve",bonus,"as bonus")
    print("Fun fact: Women recieve 10% more bonus than YOU")
elif gender=="female" or gender=="f":
    if salary<50000:
        bonus=salary/100*20
        print("You will recieve",bonus,"as bonus")
    elif salary>=50000:
        bonus=salary/100*25
        print("You will recieve",bonus,"as bonus")
else:
    print("No bonus for you")

        
    
