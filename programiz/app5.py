#swap two number
a=int(input("Enter a : "));
b=int(input("Enter b : "));
c=a+b;
a=c-a;
b=c-b;
print("a :",a);
print("b :",b);