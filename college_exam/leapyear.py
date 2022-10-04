year=int(input("Enter a year: "))
if (year%4)==0:
    if(year%100)==0: #check for century year
        if(year%400)==0:
            print("{0} is a year".format(year))
        else:
            print("{0} is not a leap year".format(year))
    else:
        print("{0} is a leap year".format(year))
else:
    print("{0} is not a leap year".format(year))