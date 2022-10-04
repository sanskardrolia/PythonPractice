#quadratic equation
import cmath
a=float(input("enter the value of a: 1"))
b=float(input("enter the value of b: "))
c=float(input("enter the value of c: "))
d=((b**2)-(4*a*c))
quad1=(-b-cmath.sqrt(d))/(2*a)
quad2=(-b+cmath.sqrt(d))/(2*a)
print("square root are {0} and {1}".format(quad1,quad2))