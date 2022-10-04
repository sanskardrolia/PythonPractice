def prime(m,n):
    for num in range(m,n+1):
        if num>1:
            for i in range(2,num):
                if(num%i)==0:
                    break
            else:
                print(num)
m=int(input("Enter the 1st value: "))
n=int(input("Enter the 2nd value: "))
prime(m,n)

