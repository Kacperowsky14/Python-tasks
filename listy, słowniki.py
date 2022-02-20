import pickle, shelve
def wyniki():
    wybor = 5
    while wybor != 0:
        if wybor == 5:
            wybor=int(input("Co chcesz zrobic? \n1-Pokaz wyniki\n2-Dodaj wynik\n3-Usun wynik\n4-Resetuj tablice wynikow \n0-Zakoncz \n"))
        if wybor == 4:
            plik = open("wyniki.bat" ,"wb")
            lista = []
            pickle.dump(lista, plik)
            print("Zresetowano!")
            plik.close
            wybor = 5
        if wybor == 2:
            plik = open("wyniki.bat" ,"rb")
            tablica = pickle.load(plik)
            plik.close
            gracz = str(input("Podaj imie\n"))
            wynik_gracza = str(input("Wprowadz wynik\n"))
            dodanie = [gracz, wynik_gracza]
            tablica.append(dodanie)
            plik = open("wyniki.bat" ,"wb") 
            pickle.dump(tablica, plik)
            plik.close
            print("Dodano!")
            wybor=5
        if wybor == 1:
            plik = open("wyniki.bat","rb")
            tablica = pickle.load(plik)
            print("Oto tablica z wynikami:\n")
            print(tablica)
            wybor=5
def slownik():
    print("Oto slownik! Co chcesz zrobic?")
    wybor = int(input("1- Dodaj termin i definicje \n2- Wyszukaj termin \n3- Resetuj slownik \n4- Odczytaj slownik \n5- Zakoncz\n"))
    while wybor != 5:
        if wybor == 0:
            wybor = int(input("1- Dodaj termin i definicje \n2- Wyszukaj termin \n3- Resetuj slownik \n4- Odczytaj slownik \n5- Zakoncz \n"))
        while wybor == 1:
            plik = open("slownik.bat" ,"rb")
            slownik = pickle.load(plik)
            termin = str(input("Dodaj nowy termin do slownika \n"))
            if termin not in slownik:
                plik.close
                definicja = str(input("Podaj definicje tego terminu \n"))
                slownik[termin] = definicja
                plik = open("slownik.bat" ,"wb")
                pickle.dump(slownik, plik)
                plik.close
                print("Dodano!")
                wybor = int(input("Wpisz 1, zeby dodac kolejny termin, lub 0 zeby wyjsc \n"))
            else:
                plik.close
                print("Istnieje juz taki termin!")
                wybor = int(input("Spobuj jeszcze raz (1) albo wyjdz (0)"))
        if wybor == 2:
            plik = open("slownik.bat" ,"rb")
            x = str(input("Jaki termin mam znalezc? \n"))
            slownik = pickle.load(plik)
            if x in slownik:
                print(slownik[x])
                plik.close
                wybor = 0
            else:
                print("Nie ma takiego terminu!")
                plik.close
                wybor = 0
        if wybor == 3:
            slownik = {}
            plik = open("slownik.bat" ,"wb")
            pickle.dump(slownik, plik)
            plik.close
            print("Slownik zresetowany.")
            wybor = 0
        if wybor == 4:
            plik = open("slownik.bat" ,"rb")
            slownik = pickle.load(plik)
            print(slownik)
            plik.close
            wybor = 0



print("Witaj w programie, ktory nie wiem jak nazwac.")
wybor = None
while wybor != 3:
    wybor = int(input("1-Tablica wyników \n2-Slownik \n3-Wyjdz z programu\n"))
    if wybor == 1:
        wyniki()
    if wybor == 2:
        slownik()
