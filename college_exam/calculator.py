def addition(a,b):
    sum=a+b
    return sum
def subtraction(a,b):
    diff=a-b
    return diff
def multiplication(a,b):
    mul=a*b
    return mul
def division(a,b):
    if(b==0):
        print("enter valid number")
        exit()
    else:
        div=float(a/b)
    return div
num1=int(input("Enter 1st value: "))
select=input("Enter the operation + , - , * , /: ")
num2=int(input("Enter 2nd value: "))
if(select=="+"):
    res=addition(num1,num2)
elif(select=="-"):
    res=subtraction(num1,num2)
elif(select=="*"):
    res=multiplication(num1,num2)
elif(select=="/"):
    res=division(num1,num2)
else:
    print("enter the valid operation")
print("Result is: {0}".format(res))


