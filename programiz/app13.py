#leap year checker
year=int(input("Enter the year: "))
if(year%4)==0 : 
    if (year%100)==0 : 
        if(year%400)==0 : 
            print("{0} is leap year".format(year))
        else : 
            print("{0} not a leap year".format(year))
    else:
        print("{0} is a leap year".format(year))
else :
    print("{0} not a leap year".format(year))