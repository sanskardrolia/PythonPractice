#voting using function
def voting():
    age =int(input("Enter Your Age"))
    if(age>=18):
        print("eligible")
    else:
        print("not eligible")
print("Voting Eligibility Check")
voting()