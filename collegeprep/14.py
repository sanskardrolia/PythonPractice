def operation(n):
    a=int(input("Enter A: "))
    b=int(input("Enter B: "))
    if n==1:
        c=a+b
    elif n==2:
        c=a-b
    elif n==3:
        c=a*b
    elif n==4:
        c=a/b
    else :
        print("Invalid")
    return c
a=int(input(" 1.Addition\n 2.Substraction\n 3.multiplication\n 4.Division :"))
ans=operation(a)
print(ans)
