import pickle, shelve

print("Operation on text files")
file = open("file.txt", "a+")
text = str(input("Enter the text you want to put in the file\n"))
file.write(text)
file.write("\n")
file.close()

print("Reading data from a file")
file = open("file.txt", "r")
print(file.read())
file.close()

print("Used car dealer")

year_of_production = ["2010", "2016", "2022"]
brand = ["Audi", "BWM", "Volksfagen"]
meter_status = ["100k", "45k", "50k"]

used_car_dealer = open("plik2.dat", "wb")
pickle.dump(year_of_production, used_car_dealer)
pickle.dump(brand, used_car_dealer)
pickle.dump(meter_status, used_car_dealer)

used_car_dealer = open("plik2.dat", "rb")
meter_status = pickle.load(used_car_dealer)
brand = pickle.load(used_car_dealer)
year_of_production = pickle.load(used_car_dealer)

print(brand)
print(meter_status)
print(year_of_production)
used_car_dealer.close()
