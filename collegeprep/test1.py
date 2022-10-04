def operation():
    a=int(input("Enter A: "))
    b=int(input("Enter B: "))
    return a+b , a-b , a*b ,a/b
a,b,c,d=operation()
print("Addition: {0} Substraction: {1} Multiplication: {2} Division: {3}".format(a,b,c,d))