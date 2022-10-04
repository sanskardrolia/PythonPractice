from cmath import sqrt
#area of triangle

#herons
a=int(input("Enter 1st side : "))
b=int(input("Enter 2nd side : "))
c=int(input("Enter 3rd side : "))

s=(a+b+c)/2

area = sqrt((s*(s-a)*(s-b)*(s-c)))

print("Area of Triangle: {0} using Herons".format(area))

#right angle

base=int(input("Enter Base of triangle: "))
height=int(input("Enter Height of triangle: "))

area2=(0.5*base*height)
print("Area of Triangle: {0} right angle".format(area2))

