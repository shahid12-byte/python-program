a = int(input("enter number"))
b = int(input("enter number"))
c= int(input("enter number"))
if(a>b and a>c):
    print("maximum is",a)
elif(b>c and b>a):
    print("maximum is",b)
else:
    print("maximum is",c)
