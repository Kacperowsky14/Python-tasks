number_bin = []
number_dec = int(input("Enter a number as decimal system and I will display it as binary system\n"))


while number_dec >= 1:
    modulo = number_dec % 2 
    if modulo == 0:
        number_dec /= 2
        number_bin.append(0)
    if modulo == 1:
        number_dec -= 1
        number_dec /= 2
        number_bin.append(1)

number_bin.reverse()

print("Your number as binary system is: ", number_bin)
