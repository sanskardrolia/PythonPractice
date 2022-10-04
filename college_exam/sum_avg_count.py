a=[10,20,4,99,8]
sum=0
avg=0.0
count=0
for i in a:
    sum=sum+i
    count=count+1
avg=sum/len(a)
print("Avg : {0} , Count : {1} , Sum : {2}".format(avg,count,sum))