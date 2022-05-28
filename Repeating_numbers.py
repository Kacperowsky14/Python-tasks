a=(1,2,3,4,5,6,7,6,5,4,5,7,8,9,5,4,3,2)
b = []

for number in a:
    if number in b:
        continue
    else:
        b.append(number)
print(b)
