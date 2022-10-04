from os import rename


word="Sanskar"
for letter in word:
    print (letter)

list=[]
value=int(input("Enter number of element: "))
for ele in range(value):
    print("Enter {0}".format(ele),"Elemnet:")
    value1=input()
    list.append(value1)
for ele in list:
    print(ele)