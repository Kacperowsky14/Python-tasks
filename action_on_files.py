import pickle, shelve
def results():
    choice = 5
    while choice != 0:
        if choice == 5:
            choice=int(input("What u want to do? \n1- Show results \n 2-Add the result\n3-Remove result\n4-reset scoreboards \n0-Exit \n"))
        if choice == 4:
            file = open("results.bat" ,"wb")
            list = []
            pickle.dump(list, file)
            print("The reset was successful!")
            file.close
            choice = 5
        if choice == 2:
            file = open("results.bat" ,"rb")
            board = pickle.load(file)
            file.close
            user = str(input("Name\n"))
            user_score = str(input("Score\n"))
            add = [user, user_score]
            board.append(add)
            file = open("results.bat" ,"wb") 
            pickle.dump(board, file)
            file.close
            print("Added!")
            choice=5
        if choice == 1:
            file = open("results.bat","rb")
            board = pickle.load(file)
            print("Here is the scoreboard\n")
            print(board)
            choice=5
def dictionary():
    print("Here is the dictionary! What you want to do?")
    choice = int(input("1-Add term and definitions \n2-Search term \n3-Reset dictionary \n4-Read dictionary \n5-Exit\n"))
    while choice != 5:
        if choice == 0:
            choice = int(input("1-Add term and definitions \n2-Search term \n3-Reset dictionary \n4-Read dictionary \n5-Exit\n"))
        while choice == 1:
            file = open("dictionary.bat" ,"rb")
            dictionary = pickle.load(file)
            term = str(input("Add new term\n"))
            if term not in dictionary:
                file.close
                definition = str(input("Give me definition \n"))
                dictionary[term] = definition
                file = open("dictionary.bat" ,"wb")
                pickle.dump(dictionary, file)
                file.close
                print("Added!")
                wybor = int(input("Enter 1 to add another appointment or enter 0 to exit \n"))
            else:
                file.close
                print("There is already such a term!")
                wybor = int(input("Try again (1) or leave (0)"))
        if choice == 2:
            file = open("dictionary.bat" ,"rb")
            x = str(input("What term should I find?\n"))
            dictionary = pickle.load(file)
            if x in dictionary:
                print(dictionary[x])
                file.close
                choice = 0
            else:
                print("There is no such term!")
                file.close
                choice = 0
        if choice == 3:
            dictionary = {}
            file = open("dictionary.bat" ,"wb")
            pickle.dump(dictionary, file)
            file.close
            print("dictionary reset.")
            choice = 0
        if choice == 4:
            file = open("dictionary.bat" ,"rb")
            dictionary = pickle.load(file)
            print(dictionary)
            file.close
            choice = 0



print("Hello, let's go")
choice = None
while choice != 3:
    choice = int(input("1-Scoreboard \n2-dictionary \n3-Exit\n"))
    if choice == 1:
        results()
    if choice == 2:
        dictionary()