a=int(input("Enter 1st number : "))
b=int(input("Enter 2nd number : "))
c=int(input("Enter 3rd number : "))
if(a>b)and(a>c):
    print("Greatest number is {0}".format(a))
elif (b>a)and(b>c):
    print("Greatest number is {0}".format(b))
else:
    print("Greatest number is {0}".format(c))