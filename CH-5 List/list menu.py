list1=[22,4,16,38,13]
choice=0
while True:
    print("\n L I S T  O P E R A T I O N S ")
    print("1. Append an element")
    print("2. Insert an element at the desired position")
    print("3. Append a list to the given list")
    print("4. Modify an existing element")
    print("5. Delete an existing element by its position")
    print("6. Delete an existing element by its value")
    print("7. Sort the list in ascending order")
    print("8. Sort the list in descending order")
    print("9. Display the list")
    print("10. Exit")
    choice=int(input("ENTER YOUR CHOICE (1-10): "))
    if choice==1:
        element=int(input("Enter the element to be appended: "))
        list1.append(element)
        print("The element has been appended\n")
    elif choice==2:
        element=int(input("Enter the element to be inserted: "))
        pos=int(input("Enter the position: "))
        list.insert(pos.element)
        print("The element has been inserted\n")
    elif choice==3:
        newlist=int(input("Enter the list to be appended: "))
        list1.extend(newlist)
        print("The list has been appended\n")
    elif choice==4:
        i=int(input("Enter the position of the element to be modified: "))
        if i < len(mylist):
            newelement=int(input("Enter the new element: "))
            oldelement=list[i]
            list1[i]=newelement
            print("The element",oldelement,"has been modified\n")
        else:
            print("Position of the element is more than the length of list")
    elif choice==5:
        i=int(input("Enter the position of the element to be deleted: "))
        if i < len(list1):
            element=list1.pop(i)
            print("The element",element,"has been deleted\n")
        else:
            print("\nPosition of the element is more than the length of list")
    elif choice==6:
        element=int(input("Enter the element to be deleted: "))
        if element in list1:
            list1.remove(element)
            print("\nThe element",element,"has been deleted\n")
        else:
            print("\nThe element",element,"is not present in the list")
    elif choice==7:
        list1.sort()
        print("\nThe list has been sorted")
    elif choice==8:
        list1.sort(reverse=True)
        print("\nThe list has been sorted in reverse order")
    elif choice==9:
        print("\n The list is:",list1)
    elif choice==10:
        break
    else:
        print("Choice is not valid")
        print("\n\nPress any key to continue.......")
        ch=input()
            
        
        
    
    
        
