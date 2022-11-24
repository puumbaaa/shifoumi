# DEBUT

import os
import random

tabmorpion = [
    ['□',"1","2","3"],
    ['1',2,2,2],
    ['2',2,2,2],
    ['3',2,2,2]
]

tabresultat = [
    ['□',"1","2","3"],
    ['1',' ',' ',' '],
    ['2',' ',' ',' '],
    ['3',' ',' ',' ']
]

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def displaytab(tab):
    cls()
    for x in range(len(tab)):
        for y in range(len(tab)):
            if tab[x][y] == 2:
                tabresultat[x][y] = ' '
            elif tab[x][y] == 1:
                tabresultat[x][y] = '⬤'
            elif tab[x][y] == 0:
                tabresultat[x][y] = '✚'
    for i in tabresultat:
        print(i)
def morpion2player():
    displaytab(tabmorpion)
    joueur = True
    while True:
        # victoire joueur1
        if (tabmorpion[1][1], tabmorpion[1][2], tabmorpion[1][3]) == (1,1,1) or (tabmorpion[2][1], tabmorpion[2][2], tabmorpion[2][3]) == (1,1,1) or (tabmorpion[3][1], tabmorpion[3][2], tabmorpion[3][3]) == (1,1,1):
            print("joueur1 a gagné")
            return
        elif (tabmorpion[1][1], tabmorpion[2][1], tabmorpion[3][1]) == (1,1,1) or (tabmorpion[1][2], tabmorpion[2][2], tabmorpion[3][2]) == (1,1,1) or (tabmorpion[1][3], tabmorpion[2][3], tabmorpion[3][3]) == (1,1,1):
            print("joueur1 a gagné")
            return
        elif (tabmorpion[1][3], tabmorpion[2][2], tabmorpion[3][1]) == (1,1,1) or (tabmorpion[1][1], tabmorpion[2][2], tabmorpion[3][3]) == (1,1,1):
            print("joueur1 a gagné")
            return
        # victoire joueur2
        elif (tabmorpion[1][1], tabmorpion[1][2], tabmorpion[1][3]) == (0,0,0) or (tabmorpion[2][1], tabmorpion[2][2], tabmorpion[2][3]) == (0,0,0) or (tabmorpion[3][1], tabmorpion[3][2], tabmorpion[3][3]) == (0,0,0):
            print("joueur2 a gagné")
            return
        elif (tabmorpion[1][1], tabmorpion[2][1], tabmorpion[3][1]) == (0,0,0) or (tabmorpion[1][2], tabmorpion[2][2], tabmorpion[3][2]) == (0,0,0) or (tabmorpion[1][3], tabmorpion[2][3], tabmorpion[3][3]) == (0,0,0):
            print("joueur2 a gagné")
            return
        elif (tabmorpion[1][3], tabmorpion[2][2], tabmorpion[3][1]) == (0,0,0) or (tabmorpion[1][1], tabmorpion[2][2], tabmorpion[3][3]) == (0,0,0):
            print("joueur2 a gagné")
            return
        else:
            i, j = int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
            if joueur == True:
                if tabmorpion[i][j] == 2:
                    tabmorpion[i][j] = 1
                    joueur = not joueur
                else : 
                    print("case déja utilisé")
                    print('rejouer')
            else:
                if tabmorpion[i][j] == 2:
                    tabmorpion[i][j] = 0
                    joueur = not joueur
                else : 
                    print("case déja utilisé")
                    print('rejouer')
            displaytab(tabmorpion)

tabmorpion = {1: ' ', 2: ' ', 3: ' ',
              4: ' ', 5: ' ', 6: ' ',
              7: ' ', 8: ' ', 9: ' '}
joueur = 'O'
ordi = 'X'
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

def PierreFeuilleCiseau(pfc_joueur):
    pfc=["pierre","feuille","ciseau"]
    pfc_ordi=random.randint(0,2)
    if pfc_ordi==pfc_joueur:
        print("égalité !")
        return
    elif (pfc_ordi==0 and pfc_joueur==2) or (pfc_ordi==1 and pfc_joueur==0) or (pfc_ordi==2 and pfc_joueur==1):
        print("perdu !")
        return
    elif (pfc_ordi==2 and pfc_joueur==0) or (pfc_ordi==0 and pfc_joueur==1) or (pfc_ordi==1 and pfc_joueur==2):
        print("gagné !")
        return

jeux=True
while jeux:
    game=int(input("pour jouer à 2 joueur taper 1, pour jouer contre l'ordi taper 2, pour arreter de jouer taper 0"))
    if game==1:
        continuer=True
        while continuer:
            morpion2player()
            question=int(input("pour continuer taper 1 sinon taper 0"))
            if question==0:
                continuer=False
    elif game==2:
        continuer=True
        while continuer:
            afficherTable(tabmorpion)
            print("les positions :")
            print("1, 2, 3 ")
            print("4, 5, 6 ")
            print("7, 8, 9 ")
            print("\n")
            start=int(input("pour commencer taper 1, sinon taper 0"))
            if start ==0:
                print("ordi commence")
                while not verificationVictoire():
                    cls()
                    choixOrdi()
                    choixJoueur()
            if start==1:
                print("joueur commence")
                while not verificationVictoire():
                    cls()
                    choixJoueur()
                    choixOrdi()
            question=int(input("pour continuer taper 1 sinon taper 0"))
            if question==0:
                continuer=False
    elif game==3:
            continuer=True
            while continuer:
                jouer=int(input("pierre = 0 | feuille = 1 | ciseau = 2"))
                PierreFeuilleCiseau(jouer)
                question=int(input("pour continuer taper 1 sinon taper 0"))
                if question==0:
                    continuer=False
    questionjeux=int(input("pour revenir au menu pricipal taper 1, sinon taper 0"))
    if questionjeux==0:
        jeux=False