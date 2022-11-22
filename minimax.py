def afficherTable(tabmorpion):
    print(tabmorpion[1] + '|' + tabmorpion[2] + '|' + tabmorpion[3])
    print('-+-+-')
    print(tabmorpion[4] + '|' + tabmorpion[5] + '|' + tabmorpion[6])
    print('-+-+-')
    print(tabmorpion[7] + '|' + tabmorpion[8] + '|' + tabmorpion[9])
    print("\n")


def espaceVide(position):
    if tabmorpion[position] == ' ':
        return True
    else:
        return False


def insertLetter(signe, position):
    if espaceVide(position):
        tabmorpion[position] = signe
        afficherTable(tabmorpion)
        if (verificationEgalite()):
            print("égalité !")
            exit()
        if verificationVictoire():
            if signe == 'X':
                print("perdu !!")
                exit()
            else:
                print("gagné !")
                exit()

        return


    else:
        print("déjà prise !")
        position = int(input("entrer nouvelle position:  "))
        insertLetter(signe, position)
        return


def verificationVictoire():
    if (tabmorpion[1] == tabmorpion[2] and tabmorpion[1] == tabmorpion[3] and tabmorpion[1] != ' '):
        return True
    elif (tabmorpion[4] == tabmorpion[5] and tabmorpion[4] == tabmorpion[6] and tabmorpion[4] != ' '):
        return True
    elif (tabmorpion[7] == tabmorpion[8] and tabmorpion[7] == tabmorpion[9] and tabmorpion[7] != ' '):
        return True
    elif (tabmorpion[1] == tabmorpion[4] and tabmorpion[1] == tabmorpion[7] and tabmorpion[1] != ' '):
        return True
    elif (tabmorpion[2] == tabmorpion[5] and tabmorpion[2] == tabmorpion[8] and tabmorpion[2] != ' '):
        return True
    elif (tabmorpion[3] == tabmorpion[6] and tabmorpion[3] == tabmorpion[9] and tabmorpion[3] != ' '):
        return True
    elif (tabmorpion[1] == tabmorpion[5] and tabmorpion[1] == tabmorpion[9] and tabmorpion[1] != ' '):
        return True
    elif (tabmorpion[7] == tabmorpion[5] and tabmorpion[7] == tabmorpion[3] and tabmorpion[7] != ' '):
        return True
    else:
        return False


def verificationGagnant(signe):
    if tabmorpion[1] == tabmorpion[2] and tabmorpion[1] == tabmorpion[3] and tabmorpion[1] == signe:
        return True
    elif (tabmorpion[4] == tabmorpion[5] and tabmorpion[4] == tabmorpion[6] and tabmorpion[4] == signe):
        return True
    elif (tabmorpion[7] == tabmorpion[8] and tabmorpion[7] == tabmorpion[9] and tabmorpion[7] == signe):
        return True
    elif (tabmorpion[1] == tabmorpion[4] and tabmorpion[1] == tabmorpion[7] and tabmorpion[1] == signe):
        return True
    elif (tabmorpion[2] == tabmorpion[5] and tabmorpion[2] == tabmorpion[8] and tabmorpion[2] == signe):
        return True
    elif (tabmorpion[3] == tabmorpion[6] and tabmorpion[3] == tabmorpion[9] and tabmorpion[3] == signe):
        return True
    elif (tabmorpion[1] == tabmorpion[5] and tabmorpion[1] == tabmorpion[9] and tabmorpion[1] == signe):
        return True
    elif (tabmorpion[7] == tabmorpion[5] and tabmorpion[7] == tabmorpion[3] and tabmorpion[7] == signe):
        return True
    else:
        return False


def verificationEgalite():
    for key in tabmorpion.keys():
        if (tabmorpion[key] == ' '):
            return False
    return True


def choixJoueur():
    position = int(input("entrer position pour 'O':  "))
    insertLetter(joueur, position)
    return


def choixOrdi():
    meilleurScore = -800
    meilleurCoup = 0
    for key in tabmorpion.keys():
        if (tabmorpion[key] == ' '):
            tabmorpion[key] = ordi
            score = minimax(tabmorpion, 0, False)
            tabmorpion[key] = ' '
            if (score > meilleurScore):
                meilleurScore = score
                meilleurCoup = key

    insertLetter(ordi, meilleurCoup)
    return


def minimax(tabmorpion, profondeur, isMaximizing):
    if (verificationGagnant(ordi)):
        return 1
    elif (verificationGagnant(joueur)):
        return -1
    elif (verificationEgalite()):
        return 0

    if (isMaximizing):
        bestScore = -800
        for key in tabmorpion.keys():
            if (tabmorpion[key] == ' '):
                tabmorpion[key] = ordi
                score = minimax(tabmorpion, profondeur + 1, False)
                tabmorpion[key] = ' '
                if (score > bestScore):
                    bestScore = score
        return bestScore

    else:
        bestScore = 800
        for key in tabmorpion.keys():
            if (tabmorpion[key] == ' '):
                tabmorpion[key] = joueur
                score = minimax(tabmorpion, profondeur + 1, True)
                tabmorpion[key] = ' '
                if (score < bestScore):
                    bestScore = score
        return bestScore


tabmorpion = {1: ' ', 2: ' ', 3: ' ',
              4: ' ', 5: ' ', 6: ' ',
              7: ' ', 8: ' ', 9: ' '}

afficherTable(tabmorpion)
print("ordi commence")
print("les positions :")
print("1, 2, 3 ")
print("4, 5, 6 ")
print("7, 8, 9 ")
print("\n")
joueur = 'O'
ordi = 'X'

start=int(input("pour commencer taper 1, sinon taper 0"))
if start ==0:
    while not verificationVictoire():
        choixOrdi()
        choixJoueur()
if start==1:
    while not verificationVictoire():
        choixJoueur()
        choixOrdi()
        