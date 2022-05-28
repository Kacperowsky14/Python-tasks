#Frizzbuss
for i in range(1,21):
    if i % 3 == 0 and i % 5 == 0:
        print("Fizz buss")
    if i % 3 == 0:
        print("Fizz")
    if i % 5 == 0:
        print("buss")
    else:
        print(i)
