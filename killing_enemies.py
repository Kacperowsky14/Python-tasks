import random
import time
print("Hello, i have game for you ( ͡° ͜ʖ ͡°)")
time.sleep(1)
print("Choose your hero! (King Arthur - 1, Anubis - 2, Gigant potato - 3")
time.sleep(3)
hero = int(input("Choose the number!\n"))
while hero > 3:
    print("Bad number")
    hero = int(input("let's try again\n"))
while hero < 0:
    print("Bad number")
    hero = int(input("let's try again\n"))
if hero == 1:
    print(
    """
    Nice! it's your stats:
    Health= 60
    damage= 4
    """)
    health_hero=60
    damage_hero=4
    enemies = random.randint(1,15)
    dmg_enemies = random.randint(1,10)
    time.sleep(3)
    x = enemies
    print("U have ", enemies , " enemies")
    time.sleep(2)
    print("They're have a different amount of health points but all they're deals ", dmg_enemies ," damage")
    time.sleep(3)
    print("Let's fight!")
    time.sleep(2)
    while health_hero > 0: #Pierwsza petla, ktora trwa dopoki licznik zdrowia nie spadnie ponizej zera
        while enemies > 0: #Petla, w petli ktora trwa dopoki liczba przeciwnikow jest wieksza od zera
            health_enemies = random.randint(1,5)
            while health_enemies >= 1: #Kolejna petla, ktora konczy sie kiedy zabijemy przeciwnika
                #Po wyjsciu z petli health enemies wynosi 0 albo mniej, musimy sprowadzic je spowrotem do wartosci poczatkowej zeby mozna bylo walczyc z kolejnym przeciwnikiem. Wiec zanim wejdziemy w ta petle, musimy wylosowac ilosc zycia naszym przeciwnikom
                health_hero -= dmg_enemies
                health_enemies -= damage_hero  
                if health_hero <= 0: #Petla konczy sie, kiedy health hero spadnie do 0
                    break
            if health_hero <=0: #Jesli health hero spadnie do zera, to musi zakonczyc sie rowniez druga petla
                    break
            enemies -= 1
            print("Nice, you are deal damage to enemy! Your health is ", health_hero , " now") 
            print(enemies, "enemies left")
            time.sleep(1)
        if enemies <= 0:
            break
    if health_hero <=0:
        print("You die!") 
        if x >= 1:
            print("U can't kill ", enemies, " enemies!")
        else:
            print("U can't kill only one enemy!")
    else:
        print("You win!") 
        print("Great job! You kill all", x , " enemies!")
#Po opuszczeniu wszystkich petli musimy podac wynik
#Zeby program sie zakonczyl musimy wyjsc ze wszystkich 3 petli

elif hero == 2:
    print(
    """
    Nice! it's your stats:
    Health= 20
    damage= 12
    """)
    health_hero=30
    damage_hero=12
    enemies = random.randint(1,10)
    dmg_enemies = random.randint(1,4)
    time.sleep(3)
    x = enemies
    print("U have ", enemies , " enemies")
    time.sleep(2)
    print("They're have a different amount of health points but all they're deals ", dmg_enemies ," damage")
    time.sleep(3)
    print("Let's fight!")
    time.sleep(2)
    while health_hero > 0: #Pierwsza petla, ktora trwa dopoki licznik zdrowia nie spadnie ponizej zera
        while enemies > 0: #Petla, w petli ktora trwa dopoki liczba przeciwnikow jest wieksza od zera
            health_enemies = random.randint(1,20)
            while health_enemies >= 1: #Kolejna petla, ktora konczy sie kiedy zabijemy przeciwnika
                #Po wyjsciu z petli health enemies wynosi 0 albo mniej, musimy sprowadzic je spowrotem do wartosci poczatkowej zeby mozna bylo walczyc z kolejnym przeciwnikiem. Wiec zanim wejdziemy w ta petle, musimy wylosowac ilosc zycia naszym przeciwnikom
                health_hero -= dmg_enemies
                health_enemies -= damage_hero  
                if health_hero <= 0: #Petla konczy sie, kiedy health hero spadnie do 0
                    break
            if health_hero <=0: #Jesli health hero spadnie do zera, to musi zakonczyc sie rowniez druga petla
                    break
            enemies -= 1
            print("Nice, you are deal damage to enemy! Your health is ", health_hero , " now") 
            print(enemies, "enemies left")
            time.sleep(1)
        if enemies <= 0:
            break
    if health_hero <=0:
        print("You die!") 
        if x >= 1:
            print("U can't kill ", enemies, " enemies!")
        else:
            print("U can't kill only one enemy!")
    else:
        print("You win!") 
        print("Great job! You kill all", x , " enemies!")
elif hero == 3:
    print(
    """
    Great, potato is fucking op!
    Your Health is 1500
    Your damage is 120
    """
    )
    time.sleep(2)
    print(
    """
                IT 
               WILL 
                BE 
                AN 
               EPIC 
              BATTLE
    """)
    health_hero=1500
    damage_hero=120
    enemies = random.randint(1,20)
    dmg_enemies = random.randint(1,120)
    time.sleep(3)
    x = enemies
    print("U have ", enemies , " enemies")
    time.sleep(2)
    print("They're have a different amount of health points but all they're deals ", dmg_enemies ," damage")
    time.sleep(3)
    print("Let's fight!")
    time.sleep(2)
    while health_hero > 0: #Pierwsza petla, ktora trwa dopoki licznik zdrowia nie spadnie ponizej zera
        while enemies > 0: #Petla, w petli ktora trwa dopoki liczba przeciwnikow jest wieksza od zera
            health_enemies = random.randint(1,180)
            while health_enemies >= 1: #Kolejna petla, ktora konczy sie kiedy zabijemy przeciwnika
                #Po wyjsciu z petli health enemies wynosi 0 albo mniej, musimy sprowadzic je spowrotem do wartosci poczatkowej zeby mozna bylo walczyc z kolejnym przeciwnikiem. Wiec zanim wejdziemy w ta petle, musimy wylosowac ilosc zycia naszym przeciwnikom
                health_hero -= dmg_enemies
                health_enemies -= damage_hero  
                if health_hero <= 0: #Petla konczy sie, kiedy health hero spadnie do 0
                    break
            if health_hero <=0: #Jesli health hero spadnie do zera, to musi zakonczyc sie rowniez druga petla
                    break
            enemies -= 1
            print("Nice, you are deal damage to enemy! Your health is ", health_hero , " now") 
            print(enemies, "enemies left")
            time.sleep(1)
        if enemies <= 0:
            break
    if health_hero <=0:
        print("You die!") 
        if x >= 1:
            print("U can't kill ", enemies, " enemies!")
        else:
            print("U can't kill only one enemy!")
    else:
        print("You win!") 
        print("Great job! You kill all", x , " enemies!")


input("Click enter to end the game")  