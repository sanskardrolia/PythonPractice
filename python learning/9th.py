def voting():
    age = int(input("Enter Your Age"))
    if(age>=18):
        a=0
    else:
        a=1
    return a
def Main():
    output=voting()
    if(output==0):
        print("Eligible")
    else:
        print("Not Eligible")
if __name__=="__main__":
    Main()
