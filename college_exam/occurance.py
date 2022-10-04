str = "MD Saif0zqN"
digit = letter = u = l = 0
for ch in str:
    if ch.isdigit():
        digit = digit+1
    elif ch.isalpha():
        letter = letter+1
        if ch.isupper():
            u += 1
        if ch.islower():
            l += 1
    else:
        pass
l1 = str.split(" ")

print("Word:", len(l1))
print("Letters:", letter)
print("Digits:", digit)
print("Upper:", u)
print("Lower:", l)
