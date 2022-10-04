def area_circle():
    r=int(input("Enter radius: "))
    area=3.14*r*r
    print("area is {0}".format(area))
    
def area_square():
    a=int(input("enter the side: "))
    area=a*a
    print("area of square with side {0} is {1}".format(a,area))

def area_rectangle():
    l=int(input("enter the length:"))
    b=int(input("enter the breadth:"))
    area=l*b
    print("area of rectangle with length {0}, breadth {1} is {2}".format(l,b,area))

print("Select opertaion: ")
select=input("1.circle 2.square 3.rectangle : ")
if(select=="1"):
    area_circle()
elif(select=="2"):
    area_square()
elif(select=="3"):
    area_rectangle()
else:
    print("enter valid operation")