year=int(input("enter the year"));
if year%4==0 and year%100!=0:
    print(year, " It's a leap year");
elif year%100==0:
    print(year," It's not a leap year");
elif year%400==0:
    print(year," It's a leap year");
else:
    print(year," It's Not a leap year")