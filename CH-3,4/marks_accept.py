#input marks scored in 3 subjects and get total and percentage
sub1=int(input("marks scored in subject 1:"))
sub2=int(input("marks scored in subject 2:"))
sub3=int(input("marks scored in subject 3:"))
max=int(input("maximum marks:"))
print("total marks obtained:",sub1+sub2+sub3)
print("total percentage:",(sub1+sub2+sub3)/(3*max)*100,"%")
