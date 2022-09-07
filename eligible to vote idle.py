age=int(input("enter age:"))
if(age>=18):
    print("eligible to vote:")
elif(age>0 and age<18):
    print("not eligible to vote:\n",18-age,"years left to eligible")
else:
    print("invalid input:")
