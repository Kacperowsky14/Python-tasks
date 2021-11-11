import random

print('Odpowiedz na kilka pytan...')
print("Odpowiadaj na pytania uzywajac cyfr- 1(tak), 0(nie)")
x=int(input("(Pytanie 1) Czy cyfra '1' zalicza sie do liczb pierwszych? \n"))
y=int(input("(Pytanie 2) Czy jezyk c jest nowszy od jezyka c++? \n"))
z=int(input("(Pytanie 3)Informatyka jest dziedzina nauki, skupiajaca sie na analizowaniu danych\n"))
w=int(input("(Pytanie 4) Nazwa jezyka Python powstala w wyniku inspiracji zespolu komikow Monty Python\n"))
p=int(input("(Pytanie 5- ostatnie) Python zostal po raz pierwszy opublikowany w 2007 roku\n"))
d=0

#To teraz policzmy sume zdobytych punktow.

if x==0:
    d+=1
if y==0:
    d+=1
if z==1:
    d+=1
if w==1:
    d+=1
if p==0:
    d+=1

#No i zaprezentujmy wyniki
if d==5:
    print("Odpowiedziales poprawnie na wszystkie pytania! \n")
elif d==4:
    print('Poszlo Ci niezle, ale popelniles jeden blad\n')
elif d==3:
    print("Popelniles az dwa bledy!\n")
elif d==2:
    print("Musisz troche pociwczyc, odpowiedziales dobrze tylko na dwa pytania\n")
elif d==1:
    print("Tylko jedna dobra odpowiedz, slabo...\n")
else:
    print("Odpowiedziales niepoprawnie na wszystkie pytania!\n")

#Zobaczmy, ktore odpowiedzi byly poprawne

if d <=4:
    a = int(input("Wcisnij 1, a pokaze Ci twoje prawidlowe odpowiedzi, jesli nie chcesz tego widziec wpisz 0 \n"))
    if a==1:
        print("Na te pytania odpowiedziales poprawnie:\n")
    if x==0:
        print("Pytanie nr 1")
    if y==0:
        print("Pytanie nr 2")
    if z==1:
        print("Pytanie nr 3")
    if w==1:
      print("Pytanie nr 4")
    if p==0:
        print("Pytanie nr 5")

    if x==1:
        print("Mimo iz 1 dzieli sie przez sama siebie i... 1 to wedlug definicji nie jest liczba pierwsza")
    if y==1:
        print("Najpier powstal jezyk c, potem c++ a nastepnie c#")
    if z==0:
        print("Informatyka z definicji to po prostu analiza danych")
    if w==0:
      print("Monty Python byli inspiracja, do powstania jezyka, dopiero pozniej waz zostal 'znakiem rozpoznawczym' tego jezyka.")
    if p==1:
        print("Data pierwszej publikacji Pythona to rok 1991.")

print("Mam dla Ciebie jeszcze jedno zadanie! \n")

#Teraz wygenerujmy pseudoloswa liczbe i dajmy uzytkownikowi jedna szanse na jej odgadniecie

losowa = random.randrange(1,10)

q=int(input("Zgadnij o jakiej liczbie pomyslalem z przedzialu od 1 do 10.. Masz tylko jedna probe! \n"))

if q==losowa:
    print("Zgadles!")
elif q!=losowa:
    print("Niestety, nie udalo Ci sie, pomyslalem o: ", losowa ,)

print("No coz, to tyle, mam nadzieje ze podobal ci sie moj pierwszy program :)")
input("Nacisnij enter, zeby zakonczyc.")
