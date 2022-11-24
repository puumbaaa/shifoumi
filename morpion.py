# DEBUT
#importation du module os et random
import os
import random
#liste du tableau utiliser pour le calcul du morpion
tabmorpion1 = [
    ['□',"1","2","3"],
    ['1',2,2,2],
    ['2',2,2,2],
    ['3',2,2,2]
]
#liste du tableau d'affichage du morpion
tabresultat = [
    ['□',"1","2","3"],
    ['1',' ',' ',' '],
    ['2',' ',' ',' '],
    ['3',' ',' ',' ']
]

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
#fonction qui permet d'afficher la table du morpion
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
#fonction qui permet de jouerau morpion à 2 joueurs
def morpion2player():
    displaytab(tabmorpion1)
    joueur = True
    while True:
        # victoire joueur1
        # vérification ligne  
        if (tabmorpion1[1][1], tabmorpion1[1][2], tabmorpion1[1][3]) == (1,1,1) or (tabmorpion1[2][1], tabmorpion1[2][2], tabmorpion1[2][3]) == (1,1,1) or (tabmorpion1[3][1], tabmorpion1[3][2], tabmorpion1[3][3]) == (1,1,1):
            print("joueur1 a gagné")
            return
        # vérification colonne
        elif (tabmorpion1[1][1], tabmorpion1[2][1], tabmorpion1[3][1]) == (1,1,1) or (tabmorpion1[1][2], tabmorpion1[2][2], tabmorpion1[3][2]) == (1,1,1) or (tabmorpion1[1][3], tabmorpion1[2][3], tabmorpion1[3][3]) == (1,1,1):
            print("joueur1 a gagné")
            return
        # vérification diagonale
        elif (tabmorpion1[1][3], tabmorpion1[2][2], tabmorpion1[3][1]) == (1,1,1) or (tabmorpion1[1][1], tabmorpion1[2][2], tabmorpion1[3][3]) == (1,1,1):
            print("joueur1 a gagné")
            return
        # victoire joueur2
        # vérification ligne
        elif (tabmorpion1[1][1], tabmorpion1[1][2], tabmorpion1[1][3]) == (0,0,0) or (tabmorpion1[2][1], tabmorpion1[2][2], tabmorpion1[2][3]) == (0,0,0) or (tabmorpion1[3][1], tabmorpion1[3][2], tabmorpion1[3][3]) == (0,0,0):
            print("joueur2 a gagné")
            return
        # vérification colonne
        elif (tabmorpion1[1][1], tabmorpion1[2][1], tabmorpion1[3][1]) == (0,0,0) or (tabmorpion1[1][2], tabmorpion1[2][2], tabmorpion1[3][2]) == (0,0,0) or (tabmorpion1[1][3], tabmorpion1[2][3], tabmorpion1[3][3]) == (0,0,0):
            print("joueur2 a gagné")
            return
        # vérification diagonale
        elif (tabmorpion1[1][3], tabmorpion1[2][2], tabmorpion1[3][1]) == (0,0,0) or (tabmorpion1[1][1], tabmorpion1[2][2], tabmorpion1[3][3]) == (0,0,0):
            print("joueur2 a gagné")
            return
        # sinon continuer à jouer
        else:
            i, j = int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
            # vérification case déjà prise ou non
            if joueur == True:
                if tabmorpion1[i][j] == 2:
                    tabmorpion1[i][j] = 1
                    joueur = not joueur
                else : 
                    print("case déja utilisé")
                    print('rejouer')
            else:
                if tabmorpion1[i][j] == 2:
                    tabmorpion1[i][j] = 0
                    joueur = not joueur
                else : 
                    print("case déja utilisé")
                    print('rejouer')
            displaytab(tabmorpion1)
# dictionnaire du tableau du morpion joueur contre ordi
tabmorpion = {1: ' ', 2: ' ', 3: ' ',
              4: ' ', 5: ' ', 6: ' ',
              7: ' ', 8: ' ', 9: ' '}
# joueur a le signe O et ordi a le signe X
joueur = 'O'
ordi = 'X'
#fonction qui affiche le tableau du morpion joueur contre ordi
def afficherTable(tabmorpion):
    print(tabmorpion[1] + '|' + tabmorpion[2] + '|' + tabmorpion[3])
    print('-+-+-')
    print(tabmorpion[4] + '|' + tabmorpion[5] + '|' + tabmorpion[6])
    print('-+-+-')
    print(tabmorpion[7] + '|' + tabmorpion[8] + '|' + tabmorpion[9])
    print("\n")

# fonction qui vérifie si la case est prise ou non
def espaceVide(position):
    if tabmorpion[position] == ' ':
        return True
    else:
        return False

#fonction qui insert le signe dans la position demandé
def insertLetter(signe, position):
    #si la case n'est pas prise
    if espaceVide(position):
        #inserer le signe dans le tableau
        tabmorpion[position] = signe
        afficherTable(tabmorpion)
        # si égalité
        if (verificationEgalite()):
            print("égalité !")
            return
        #si victoire du joueur ou de l'ordi
        elif verificationVictoire():
            if signe == 'X':
                print("perdu !!")
                return
            else:
                print("gagné !")
                return

        return

    # si la case est prise redemander la case
    else:
        print("déjà prise !")
        position = int(input("entrer nouvelle position:  "))
        insertLetter(signe, position)
        return

# fonction qui vérifie la victoire d'un joueur ou de l'ordi sans vérifier qui gagne
def verificationVictoire():
    # ligne 1
    if (tabmorpion[1] == tabmorpion[2] and tabmorpion[1] == tabmorpion[3] and tabmorpion[1] != ' '):
        return True
    # ligne 2
    elif (tabmorpion[4] == tabmorpion[5] and tabmorpion[4] == tabmorpion[6] and tabmorpion[4] != ' '):
        return True
    # ligne 3
    elif (tabmorpion[7] == tabmorpion[8] and tabmorpion[7] == tabmorpion[9] and tabmorpion[7] != ' '):
        return True
    # colonne 1
    elif (tabmorpion[1] == tabmorpion[4] and tabmorpion[1] == tabmorpion[7] and tabmorpion[1] != ' '):
        return True
    # colonne 2
    elif (tabmorpion[2] == tabmorpion[5] and tabmorpion[2] == tabmorpion[8] and tabmorpion[2] != ' '):
        return True
    # colonne 3
    elif (tabmorpion[3] == tabmorpion[6] and tabmorpion[3] == tabmorpion[9] and tabmorpion[3] != ' '):
        return True
    # diagonale 1
    elif (tabmorpion[1] == tabmorpion[5] and tabmorpion[1] == tabmorpion[9] and tabmorpion[1] != ' '):
        return True
    # diagonale 2
    elif (tabmorpion[7] == tabmorpion[5] and tabmorpion[7] == tabmorpion[3] and tabmorpion[7] != ' '):
        return True
    # sinon
    else:
        return False

#vérification du gagnant
def verificationGagnant(signe):
    # ligne 1
    if tabmorpion[1] == tabmorpion[2] and tabmorpion[1] == tabmorpion[3] and tabmorpion[1] == signe:
        return True
    # ligne 2
    elif (tabmorpion[4] == tabmorpion[5] and tabmorpion[4] == tabmorpion[6] and tabmorpion[4] == signe):
        return True
    # ligne 3
    elif (tabmorpion[7] == tabmorpion[8] and tabmorpion[7] == tabmorpion[9] and tabmorpion[7] == signe):
        return True
    # colonne 1
    elif (tabmorpion[1] == tabmorpion[4] and tabmorpion[1] == tabmorpion[7] and tabmorpion[1] == signe):
        return True
    # colonne 2
    elif (tabmorpion[2] == tabmorpion[5] and tabmorpion[2] == tabmorpion[8] and tabmorpion[2] == signe):
        return True
    # colonne 3
    elif (tabmorpion[3] == tabmorpion[6] and tabmorpion[3] == tabmorpion[9] and tabmorpion[3] == signe):
        return True
    # diagonale 1
    elif (tabmorpion[1] == tabmorpion[5] and tabmorpion[1] == tabmorpion[9] and tabmorpion[1] == signe):
        return True
    # diagonale 2
    elif (tabmorpion[7] == tabmorpion[5] and tabmorpion[7] == tabmorpion[3] and tabmorpion[7] == signe):
        return True
    # sinon
    else:
        return False

# fonction qui vérifie une égalité
def verificationEgalite():
    for key in tabmorpion.keys():
        if (tabmorpion[key] == ' '):
            return False
    return True

# fonction qui demande au joueur de choisir sa case
def choixJoueur():
    position = int(input("entrer position pour 'O':  "))
    insertLetter(joueur, position)
    return

# fonction récursive qui permet le choix de l'ordi
def choixOrdi():
    # définition des variables meilleurScore et meilleurCoup qui définie un score à chaque coup de base très bas 
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
# fonction qui permet de jouer au pierre feuille ciseau contre un ordi
def PierreFeuilleCiseau(pfc_joueur):
    pfc=["pierre","feuille","ciseau"]
    # le coup jouer par l'ordi
    pfc_ordi=random.randint(0,2)
    # vérification égalité
    if pfc_ordi==pfc_joueur:
        print("égalité !")
        return
    # vérification défaite
    elif (pfc_ordi==0 and pfc_joueur==2) or (pfc_ordi==1 and pfc_joueur==0) or (pfc_ordi==2 and pfc_joueur==1):
        print("perdu !")
        return
    # vérification défaite
    elif (pfc_ordi==2 and pfc_joueur==0) or (pfc_ordi==0 and pfc_joueur==1) or (pfc_ordi==1 and pfc_joueur==2):
        print("gagné !")
        return
#on définie un variable jeux à True 
jeux=True
while jeux:
    game=int(input("pour jouer à 2 joueur taper 1, pour jouer contre l'ordi taper 2, pour arreter de jouer taper 0"))
    if game==0:
        jeux=False

    #tant que game est égal à 1
    elif game==1:
        continuer=True
        while continuer:
            morpion2player()
            question=int(input("pour continuer taper 1 sinon taper 0"))
            if question==0:
                continuer=False
        questionjeux=int(input("pour revenir au menu pricipal taper 1, sinon taper 0"))
        if questionjeux==0:
            jeux=False
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
                    choixOrdi()
                    choixJoueur()
                question=int(input("pour continuer taper 1 sinon taper 0"))
                if question==0:
                    continuer=False
            if start==1:
                print("joueur commence")
                while not verificationVictoire():
                    choixJoueur()
                    choixOrdi()
                question=int(input("pour continuer taper 1 sinon taper 0"))
                if question==0:
                    continuer=False
        questionjeux=int(input("pour revenir au menu pricipal taper 1, sinon taper 0"))
        if questionjeux==0:
            jeux=False
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
    