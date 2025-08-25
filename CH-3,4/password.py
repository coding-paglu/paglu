#program to make a password and confirm it
password=input("Enter your password:")
incorrect=0
while incorrect<3:
    confirm=input("Confirm your password:")
    if confirm==password:
        print("password sucessfully created")
        incorrect+=4
    else:
        print("Incorrect password, Try again")
        incorrect+=1
        print("you have",3-incorrect,"retries remaining")
if incorrect==3:
    print("maximum retries reached")
        
