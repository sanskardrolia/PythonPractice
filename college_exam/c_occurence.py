import pprint
x=input("Enter a String: ")
count={}
for character in x:
    count.setdefault(character,0)
    count[character]=count[character]+1
pprint.pprint(count)