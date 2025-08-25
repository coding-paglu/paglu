word=input("Enter a string: ")
count={}
for i in word:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
print("Character counts:",count)
