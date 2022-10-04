def febonacci(n):
    if n<0:
        print('enter the positive number')
    elif n==0:
        return 0
    elif n==1:
        return 1
    else:
        return febonacci(n-1)+febonacci(n-2)

n = 4
x = febonacci(n)
print(x)