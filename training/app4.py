from cmath import sqrt


a=int(input("Enter a value : "))
b=int(input("Enter b value : "))
c=int(input("Enter c value : "))

d=b**2-4*a*c

sol1=(-b+sqrt(d))/2*a
sol2=(-b-sqrt(d))/2*a

print("Quadratic equation of {0}x^2 + {1}x + {2} = {3} & {4}".format(a,b,c,sol1,sol2))