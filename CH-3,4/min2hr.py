time=int(input("Enter time in minutes:"))
hr=time//60
min=time%60
if min!=0 and min!=1:
    print(hr,"Hours","and",min,"Minutes")
elif min==1:
    print(hr,"Hours","and",min,"Minute")
else:
    print(hr,"Hours")
