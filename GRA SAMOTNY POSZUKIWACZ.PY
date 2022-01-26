# I will add english language soon
# GRA SAMOTNY POSZUKIWIACZ
import time
import random
ekwipunek = []
skarby = ("sztabka zlota", "mala sakiewka", "smieci", "dziwny kamien", "kalesony somsiada", "miecz", "sztylet")

print("Jestes samotnym poszukiwaczem, zobaczymy co odnajdziesz!\n")
time.sleep(2)
rozpoczecie_gry = str(input("Wpisz slowo start, zeby wyruszyc!\n"))
if (rozpoczecie_gry.upper()) == "START":
    print("Przed toba super podroz, juz na samym poczatku widzisz ze cos lezy kolo drzewa, zobaczmy co to!")
    x = random.choice(skarby)
    time.sleep(3)
    print("Super, znalazles", x ,)
    time.sleep(2)
    znaleziony_przedmiot = int(input("wcisnij 1, zeby dodac do ekwipunku, lub 0 zeby isc dalej \n"))
    if znaleziony_przedmiot == 1:
        ekwipunek.append(x)
        time.sleep(1)
        print("Dodano! ruszamy dalej\n")
        print("Ekwipunek- ", ekwipunek ,)
        time.sleep(2)
    else:
        time.sleep(1)
        print("No to ruszamy!")
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print("Kolejny skarb! Przed toba tajemniczy worek, zobaczmy co to!")
    time.sleep(2)
    a = random.choice(skarby)
    b = random.choice(skarby)
    print("Po otwarciu worka, okazalo sie, ze to " ,a ,", oraz ",b,)
    time.sleep(3)
    print("Zachowaj: ", a, " wcisnij 1" "\n"
    "Zachowaj: ", b, " wcisnij 2" "\n"
    "Zachowaj obie te rzeczy- wcisnij 3" "\n"
    "Idz dalej, nie biorac niczego - 0\n")
    znaleziony_przedmiot = int(input("Wybierz madrze!\n"))
    if znaleziony_przedmiot == 1:
        ekwipunek.append(a)
        print("Dodano " ,a, " do ekwipunku!")
        time.sleep(2)
    if znaleziony_przedmiot == 2:
        ekwipunek.append(b)
        print("Dodano " ,b, " do ekwipunku!")
        time.sleep(2)
    if znaleziony_przedmiot == 3:
        ekwipunek.append(a)
        ekwipunek.append(b)
        time.sleep(2)
        print("Dodano " ,a, "oraz" ,b, " do ekwipunku!\n")
        print("rzeczy w ekwipunku- ",ekwipunek,)
    time.sleep(3)
    print("Chcesz wyruszyc, ale slyszysz w oddali jakies dziwne dzwieki...")
    time.sleep(2)
    print("Podchodzisz blizej, halasy ktore slyszales to warczenie")
    time.sleep(2)
    print("TO WILK\n")
    wilk = int(input("Wcisnij 1- ucieczka, wcisnij 2- stan do walki z wilkiem.\n"))
    if wilk == 1:
        print("Uciekasz tak szybko jak tylko mozesz")
    if wilk == 2:
        if "kalesony somsiada" in ekwipunek:
            print("Uzywasz smierdzoncych kaleson somsiada i wilk zdycha")
        if "kalesony somsiada" not in ekwipunek:
            if "sztylet" in ekwipunek:
                print("Zabijasz wilka za pomoca sztyletu!")
            if "sztylet" not in ekwipunek:
                if "miecz" in ekwipunek:
                    print("Rozcinasz przeciwnika mieczem!")
                if "miecz" not in ekwipunek:
                    print("Nie masz przy sobie zadnej broni, byles smacznym kąksiem dla wilka, [*]")
print("Jest to wersja lite, zeby nauczyc sie uzywac krotek, oraz list ")
input("Wcisnij enter, zeby zakonczyc gre")

                   
