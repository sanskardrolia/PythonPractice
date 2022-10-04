#prime number program
num = int(input("Enter a number: "))
flag = False
if num > 1:
    for i in range(2, num):
        if(num % i) == 0:
            flag = True
if flag:
    print("{0} is not prime".format(num))
else:
    print("{0} is prime".format(num))
