
import random
rzut1= random.randint(1,6)
rzut2= random.randint(1,6)
rzut3= random.randint(1,6)
suma = rzut1+ rzut2+ rzut3
input('Nacisnij enter, zeby rzucic koscmi!')
print("Wyrzuciles nastepujacaliczbe oczek: ", suma )
x=int(input("Teraz pomnóż ta liczbe przez dwa, dodaj 15, potem dodaj 35 jezeli dobrze to wyliczysz bedzie nagroda!\n"))
suma *= 2
suma += 50

if x==suma:
    print("\n Zgadles! Oto twoja nagroda! :" )
    print(
    """
. . . . . . . . . . /'¯/)
. . . . . . . . . /¯ ./
. . . . . . . . /. . /
. . . . . /'¯`/'. .'/'¯¯`·¸
. . . . ./'/. /. . /. . /¨. /¯
. . . . ('(. . '. . '. .¯'/'. .')
. . . . .\. . . . . . . . .'. ./
. . . . ..'\'. .\. . . . . ..·'
. . . . . . \. . . . . . . (
. . . . . . . \. . . . . . .
    """
)
else:
    print("Twoja matma jest naprawde slaba xD")
