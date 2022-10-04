from cmath import sqrt
import math
number = int(input("Enter a number: "))
res=sqrt(number)
res2=number**0.5
print("Square root of {0} = {1} using function".format(number,res))
print("Square root of {0} = {1} without function".format(number,res2))