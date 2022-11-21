# DEBUT

import os

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


def ordi_morpion():
    start=int(input("pour commencer taper 1, sinon taper 0"))
    if start==0:
        tabmorpion[2][1]=1
        displaytab(tabmorpion)
        coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
        tabmorpion[coupJoueurX][coupJoueurY]=0
        displaytab(tabmorpion)    
        if tabmorpion[2][3]==0:
            tabmorpion[1][1]=1
            displaytab(tabmorpion)
            coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
            tabmorpion[coupJoueurX][coupJoueurY]=0
            displaytab(tabmorpion)
            if tabmorpion[3][1]==0:
                tabmorpion[3][3]=1
                displaytab(tabmorpion)
                coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                tabmorpion[coupJoueurX][coupJoueurY]=0
                displaytab(tabmorpion)
                if tabmorpion[2][2]==2:
                    tabmorpion[2][2]=1
                    displaytab(tabmorpion)
                    print("perdu !")
                    return
                else:
                    tabmorpion[1][3]=1
                    displaytab(tabmorpion)
                    coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                    tabmorpion[coupJoueurX][coupJoueurY]=0
                    displaytab(tabmorpion)
                    if tabmorpion[1][2]==2:
                        tabmorpion[1][2]=1
                        displaytab(tabmorpion)
                        print("perdu !")
                        return
                    else:
                        tabmorpion[3][2]=1
                        displaytab(tabmorpion)
                        print("égalité !")
                        return
            else:
                tabmorpion[3][1]=1
                displaytab(tabmorpion)
                print("perdu !")
                return
        
        elif tabmorpion[2][2]==0:
            tabmorpion[1][1]=1
            displaytab(tabmorpion)
            coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
            tabmorpion[coupJoueurX][coupJoueurY]=0
            displaytab(tabmorpion)
            if tabmorpion[3][1]==2:
                tabmorpion[3][1]=1
                displaytab(tabmorpion)
                print("perdu !")
                return
            else:
                tabmorpion[1][3]=1
                displaytab(tabmorpion)
                coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                tabmorpion[coupJoueurX][coupJoueurY]=0
                displaytab(tabmorpion)        
                if tabmorpion[1][2]==2:
                    tabmorpion[1][2]=1
                    displaytab(tabmorpion)
                    print("perdu !")
                    return
                else:
                    tabmorpion[3][2]=1
                    displaytab(tabmorpion)
                    coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                    tabmorpion[coupJoueurX][coupJoueurY]=0
                    displaytab(tabmorpion)
                    if tabmorpion[3][3]==2:
                        tabmorpion[3][3]=1
                        displaytab(tabmorpion)
                        print("égalité !")
                        return
                    else:
                        tabmorpion[2][3]=1
                        displaytab(tabmorpion)
                        print("égalité !")
                        return
        elif tabmorpion[1][1]==0:
            tabmorpion[2][2]=1
            displaytab(tabmorpion)
            coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
            tabmorpion[coupJoueurX][coupJoueurY]=0
            displaytab(tabmorpion)
            if tabmorpion[2][3]==2:
                tabmorpion[2][3]=1
                displaytab(tabmorpion)
                print("perdu !")
                return
            else:
                tabmorpion[1][3]=1
                displaytab(tabmorpion)
                coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                tabmorpion[coupJoueurX][coupJoueurY]=0
                displaytab(tabmorpion)
                if tabmorpion[3][1]==2:
                    tabmorpion[3][1]=1
                    displaytab(tabmorpion)
                    print("perdu !")
                    return
                else:
                    tabmorpion[3][2]=1
                    displaytab(tabmorpion)
                    coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                    tabmorpion[coupJoueurX][coupJoueurY]=0
                    displaytab(tabmorpion)
                    if tabmorpion[1][2]==2:
                        tabmorpion[1][2]=1
                        displaytab(tabmorpion)
                        print("perdu !")
                        return
                    else:
                        tabmorpion[3][3]=1
                        displaytab(tabmorpion)
                        print("égalité !")
                        return
        elif tabmorpion[3][1]==0:
            tabmorpion[2][2]=1
            displaytab(tabmorpion)
            coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
            tabmorpion[coupJoueurX][coupJoueurY]=0
            displaytab(tabmorpion)
            if tabmorpion[2][3]==2:
                tabmorpion[2][3]=1
                displaytab(tabmorpion)
                print("perdu !")
                return
            else:
                tabmorpion[3][3]=1
                displaytab(tabmorpion)
                coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                tabmorpion[coupJoueurX][coupJoueurY]=0
                displaytab(tabmorpion)
                if tabmorpion[1][1]==2:
                    tabmorpion[1][1]=1
                    displaytab(tabmorpion)
                    print("perdu !")
                    return
                else:
                    tabmorpion[3][2]=1
                    displaytab(tabmorpion)
                    coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                    tabmorpion[coupJoueurX][coupJoueurY]=0
                    displaytab(tabmorpion)
                    if tabmorpion[1][2]==2:
                        tabmorpion[1][2]=1
                        displaytab(tabmorpion)
                        print("perdu !")
                        return
                    else:
                        tabmorpion[1][3]=1
                        displaytab(tabmorpion)
                        print("égalité !")
                        return
        if tabmorpion[3][3]==0 or tabmorpion[3][2]==0:
            tabmorpion[3][1]=1
            displaytab(tabmorpion)
            coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
            tabmorpion[coupJoueurX][coupJoueurY]=0
            displaytab(tabmorpion)
            if tabmorpion[1][1]==2:
                tabmorpion[1][1]=1
                displaytab(tabmorpion)
                print("perdu !")
                return
            else:
                tabmorpion[2][2]=1
                displaytab(tabmorpion)
                coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                tabmorpion[coupJoueurX][coupJoueurY]=0
                displaytab(tabmorpion)
                if tabmorpion[1][3]==2:
                    tabmorpion[1][3]=1
                    displaytab(tabmorpion)
                    print("perdu !")
                    return
                else:
                    tabmorpion[2][3]=1
                    displaytab(tabmorpion)
                    print("perdu !")
                    return
        else:
            tabmorpion[1][1]=1
            displaytab(tabmorpion)
            coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
            tabmorpion[coupJoueurX][coupJoueurY]=0
            displaytab(tabmorpion)
            if tabmorpion[3][1]==2:
                tabmorpion[3][1]=1
                displaytab(tabmorpion)
                print("perdu !")
                return
            else:
                tabmorpion[2][2]=1
                displaytab(tabmorpion)
                coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                tabmorpion[coupJoueurX][coupJoueurY]=0
                displaytab(tabmorpion)
                if tabmorpion[2][3]==2:
                    tabmorpion[2][3]=1
                    displaytab(tabmorpion)
                    print("perdu !")
                    return
                else:
                    tabmorpion[3][3]=1
                    displaytab(tabmorpion)
                    print("perdu !")
                    return
    elif start==1:
        displaytab(tabmorpion)
        coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
        tabmorpion[coupJoueurX][coupJoueurY]=0
        displaytab(tabmorpion)
        if tabmorpion[1][1]==0:
            tabmorpion[2][2]=1
            displaytab(tabmorpion)
            coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
            tabmorpion[coupJoueurX][coupJoueurY]=0
            displaytab(tabmorpion)
            if tabmorpion[3][1]==0:
                tabmorpion[2][1]=1
                displaytab(tabmorpion)
                coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                tabmorpion[coupJoueurX][coupJoueurY]=0
                displaytab(tabmorpion)
                if tabmorpion[2][3]==2:
                    tabmorpion[2][3]=1
                    displaytab(tabmorpion)
                    print("perdu !")
                    return
                else:
                    tabmorpion[3][2]=1
                    displaytab(tabmorpion)
                    coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                    tabmorpion[coupJoueurX][coupJoueurY]=0
                    displaytab(tabmorpion)
                    if tabmorpion[1][2]==2:
                        tabmorpion[1][2]=1
                        displaytab(tabmorpion)
                        print("perdu !")
                        return
                    else:
                        tabmorpion[1][3]=1
                        displaytab(tabmorpion)
                        coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                        tabmorpion[coupJoueurX][coupJoueurY]=0
                        displaytab(tabmorpion)
                        print("égalité !")
                        return
            elif tabmorpion[2][1]==0:
                tabmorpion[3][1]=1
                displaytab(tabmorpion)
                coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                tabmorpion[coupJoueurX][coupJoueurY]=0
                displaytab(tabmorpion)
                if tabmorpion[1][3]==2:
                    tabmorpion[1][3]=1
                    displaytab(tabmorpion)
                    print("perdu !")
                    return
                else:
                    tabmorpion[1][2]=1
                    displaytab(tabmorpion)
                    coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                    tabmorpion[coupJoueurX][coupJoueurY]=0
                    displaytab(tabmorpion)
                    if tabmorpion[3][2]==2:
                        tabmorpion[3][2]=1
                        displaytab(tabmorpion)
                        print("perdu !")
                        return
                    else:
                        tabmorpion[3][3]=1
                        displaytab(tabmorpion)
                        coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                        tabmorpion[coupJoueurX][coupJoueurY]=0
                        displaytab(tabmorpion)
                        print("égalité !")
                        return
            elif tabmorpion[1][2]==0:
                tabmorpion[1][3]=1
                displaytab(tabmorpion)
                coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                tabmorpion[coupJoueurX][coupJoueurY]=0
                displaytab(tabmorpion)
                if tabmorpion[3][1]==2:
                    tabmorpion[3][1]=1
                    displaytab(tabmorpion)
                    print("perdu !")
                    return
                else:
                    tabmorpion[2][1]=1
                    displaytab(tabmorpion)
                    coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                    tabmorpion[coupJoueurX][coupJoueurY]=0
                    displaytab(tabmorpion)
                    if tabmorpion[2][3]==2:
                        tabmorpion[2][3]=1
                        displaytab(tabmorpion)
                        print("perdu !")
                        return
                    else:
                        tabmorpion[3][3]=1
                        displaytab(tabmorpion)
                        coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                        tabmorpion[coupJoueurX][coupJoueurY]=0
                        displaytab(tabmorpion)
                        print("égalité !")
                        return
            elif tabmorpion[1][3]==0:
                tabmorpion[1][2]=1
                displaytab(tabmorpion)
                coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                tabmorpion[coupJoueurX][coupJoueurY]=0
                displaytab(tabmorpion)
                if tabmorpion[3][2]==2:
                    tabmorpion[3][2]=1
                    displaytab(tabmorpion)
                    print("perdu !")
                    return 
                else:
                    tabmorpion[2][3]=1
                    displaytab(tabmorpion)
                    coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                    tabmorpion[coupJoueurX][coupJoueurY]=0
                    displaytab(tabmorpion)
                    if tabmorpion[2][1]==2:
                        tabmorpion[2][1]=1
                        displaytab(tabmorpion)
                        print("perdu !")
                        return
                    else:
                        tabmorpion[3][1]=1
                        displaytab(tabmorpion)
                        coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                        tabmorpion[coupJoueurX][coupJoueurY]=0
                        displaytab(tabmorpion)
                        print("égalité !")
                        return
            elif tabmorpion[2][3]==0:
                tabmorpion[1][3]=1
                displaytab(tabmorpion)
                coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                tabmorpion[coupJoueurX][coupJoueurY]=0
                displaytab(tabmorpion)
                if tabmorpion[3][1]==2:
                    tabmorpion[3][1]=1
                    displaytab(tabmorpion)
                    print("perdu !")
                    return 
                else:
                    tabmorpion[2][1]=1
                    displaytab(tabmorpion)
                    coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                    tabmorpion[coupJoueurX][coupJoueurY]=0
                    displaytab(tabmorpion)
                    if tabmorpion[3][2]==0:
                        tabmorpion[3][3]=1
                        displaytab(tabmorpion)
                        coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                        tabmorpion[coupJoueurX][coupJoueurY]=0
                        displaytab(tabmorpion)
                        print("égalité !")
                        return
                    elif tabmorpion[3][3]==0:
                        tabmorpion[3][2]=1
                        displaytab(tabmorpion)
                        coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                        tabmorpion[coupJoueurX][coupJoueurY]=0
                        displaytab(tabmorpion)
                        print("égalité !")
                        return
                    else:
                        tabmorpion[3][3]=1
                        displaytab(tabmorpion)
                        coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                        tabmorpion[coupJoueurX][coupJoueurY]=0
                        displaytab(tabmorpion)
                        print("égalité !")
                        return
            elif tabmorpion[3][3]==0:
                tabmorpion[3][2]=1
                displaytab(tabmorpion)
                coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                tabmorpion[coupJoueurX][coupJoueurY]=0
                displaytab(tabmorpion)
                if tabmorpion[1][2]==2:
                    tabmorpion[1][2]=1
                    displaytab(tabmorpion)
                    print("perdu !")
                    return 
                else:
                    tabmorpion[1][3]=1
                    displaytab(tabmorpion)
                    coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                    tabmorpion[coupJoueurX][coupJoueurY]=0
                    displaytab(tabmorpion)
                    if tabmorpion[3][1]==0:
                        tabmorpion[3][1]=1
                        displaytab(tabmorpion)
                        print("perdu !")
                        return
                    else:
                        tabmorpion[2][3]=1
                        displaytab(tabmorpion)
                        coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                        tabmorpion[coupJoueurX][coupJoueurY]=0
                        displaytab(tabmorpion)
                        print("égalité !")
                        return
            elif tabmorpion[3][2]==0:
                tabmorpion[3][1]=1
                displaytab(tabmorpion)
                coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                tabmorpion[coupJoueurX][coupJoueurY]=0
                displaytab(tabmorpion)
                if tabmorpion[1][3]==2:
                    tabmorpion[1][3]=1
                    displaytab(tabmorpion)
                    print("perdu !")
                    return 
                else:
                    tabmorpion[1][2]=1
                    displaytab(tabmorpion)
                    coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                    tabmorpion[coupJoueurX][coupJoueurY]=0
                    displaytab(tabmorpion)
                    if tabmorpion[3][3]==0:
                        tabmorpion[2][3]=1
                        displaytab(tabmorpion)
                        coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                        tabmorpion[coupJoueurX][coupJoueurY]=0
                        displaytab(tabmorpion)
                        print("égalité !")
                        return
                    elif tabmorpion[2][3]==0:
                        tabmorpion[3][3]=1
                        displaytab(tabmorpion)
                        coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                        tabmorpion[coupJoueurX][coupJoueurY]=0
                        displaytab(tabmorpion)
                        print("égalité !")
                        return
                    else:
                        tabmorpion[3][3]=1
                        displaytab(tabmorpion)
                        coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                        tabmorpion[coupJoueurX][coupJoueurY]=0
                        displaytab(tabmorpion)
                        print("égalité !")
                        return
        elif tabmorpion[1][3]==0:
            tabmorpion[2][2]=1
            displaytab(tabmorpion)
            coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
            tabmorpion[coupJoueurX][coupJoueurY]=0
            displaytab(tabmorpion)
            if tabmorpion[3][3]==0:
                tabmorpion[2][3]=1
                displaytab(tabmorpion)
                coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                tabmorpion[coupJoueurX][coupJoueurY]=0
                displaytab(tabmorpion)
                if tabmorpion[2][1]==2:
                    tabmorpion[2][1]=1
                    displaytab(tabmorpion)
                    print("perdu !")
                    return
                else:
                    tabmorpion[3][2]=1
                    displaytab(tabmorpion)
                    coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                    tabmorpion[coupJoueurX][coupJoueurY]=0
                    displaytab(tabmorpion)
                    if tabmorpion[1][2]==2:
                        tabmorpion[1][2]=1
                        displaytab(tabmorpion)
                        print("perdu !")
                        return
                    else:
                        tabmorpion[1][1]=1
                        displaytab(tabmorpion)
                        coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                        tabmorpion[coupJoueurX][coupJoueurY]=0
                        displaytab(tabmorpion)
                        print("égalité !")
                        return
            elif tabmorpion[2][3]==0:
                tabmorpion[3][3]=1
                displaytab(tabmorpion)
                coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                tabmorpion[coupJoueurX][coupJoueurY]=0
                displaytab(tabmorpion)
                if tabmorpion[1][1]==2:
                    tabmorpion[1][1]=1
                    displaytab(tabmorpion)
                    print("perdu !")
                    return
                else:
                    tabmorpion[1][2]=1
                    displaytab(tabmorpion)
                    coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                    tabmorpion[coupJoueurX][coupJoueurY]=0
                    displaytab(tabmorpion)
                    if tabmorpion[3][2]==2:
                        tabmorpion[3][2]=1
                        displaytab(tabmorpion)
                        print("perdu !")
                        return
                    else:
                        tabmorpion[3][1]=1
                        displaytab(tabmorpion)
                        coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                        tabmorpion[coupJoueurX][coupJoueurY]=0
                        displaytab(tabmorpion)
                        print("égalité !")
                        return
            elif tabmorpion[1][2]==0:
                tabmorpion[1][1]=1
                displaytab(tabmorpion)
                coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                tabmorpion[coupJoueurX][coupJoueurY]=0
                displaytab(tabmorpion)
                if tabmorpion[3][3]==2:
                    tabmorpion[3][3]=1
                    displaytab(tabmorpion)
                    print("perdu !")
                    return
                else:
                    tabmorpion[2][3]=1
                    displaytab(tabmorpion)
                    coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                    tabmorpion[coupJoueurX][coupJoueurY]=0
                    displaytab(tabmorpion)
                    if tabmorpion[2][1]==2:
                        tabmorpion[2][1]=1
                        displaytab(tabmorpion)
                        print("perdu !")
                        return
                    else:
                        tabmorpion[3][1]=1
                        displaytab(tabmorpion)
                        coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                        tabmorpion[coupJoueurX][coupJoueurY]=0
                        displaytab(tabmorpion)
                        print("égalité !")
                        return
            elif tabmorpion[1][1]==0:
                tabmorpion[1][2]=1
                displaytab(tabmorpion)
                coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                tabmorpion[coupJoueurX][coupJoueurY]=0
                displaytab(tabmorpion)
                if tabmorpion[3][2]==2:
                    tabmorpion[3][2]=1
                    displaytab(tabmorpion)
                    print("perdu !")
                    return 
                else:
                    tabmorpion[2][3]=1
                    displaytab(tabmorpion)
                    coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                    tabmorpion[coupJoueurX][coupJoueurY]=0
                    displaytab(tabmorpion)
                    if tabmorpion[2][1]==2:
                        tabmorpion[2][1]=1
                        displaytab(tabmorpion)
                        print("perdu !")
                        return
                    else:
                        tabmorpion[3][1]=1
                        displaytab(tabmorpion)
                        coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                        tabmorpion[coupJoueurX][coupJoueurY]=0
                        displaytab(tabmorpion)
                        print("égalité !")
                        return
            elif tabmorpion[2][1]==0:
                tabmorpion[1][1]=1
                displaytab(tabmorpion)
                coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                tabmorpion[coupJoueurX][coupJoueurY]=0
                displaytab(tabmorpion)
                if tabmorpion[3][3]==2:
                    tabmorpion[3][3]=1
                    displaytab(tabmorpion)
                    print("perdu !")
                    return 
                else:
                    tabmorpion[2][3]=1
                    displaytab(tabmorpion)
                    coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                    tabmorpion[coupJoueurX][coupJoueurY]=0
                    displaytab(tabmorpion)
                    if tabmorpion[3][1]==0:
                        tabmorpion[3][2]=1
                        displaytab(tabmorpion)
                        coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                        tabmorpion[coupJoueurX][coupJoueurY]=0
                        displaytab(tabmorpion)
                        print("égalité !")
                        return
                    elif tabmorpion[3][2]==0:
                        tabmorpion[3][1]=1
                        displaytab(tabmorpion)
                        coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                        tabmorpion[coupJoueurX][coupJoueurY]=0
                        displaytab(tabmorpion)
                        print("égalité !")
                        return
                    else:
                        tabmorpion[3][1]=1
                        displaytab(tabmorpion)
                        coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                        tabmorpion[coupJoueurX][coupJoueurY]=0
                        displaytab(tabmorpion)
                        print("égalité !")
                        return
            elif tabmorpion[3][1]==0:
                tabmorpion[3][2]=1
                displaytab(tabmorpion)
                coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                tabmorpion[coupJoueurX][coupJoueurY]=0
                displaytab(tabmorpion)
                if tabmorpion[1][2]==2:
                    tabmorpion[1][2]=1
                    displaytab(tabmorpion)
                    print("perdu !")
                    return 
                else:
                    tabmorpion[1][1]=1
                    displaytab(tabmorpion)
                    coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                    tabmorpion[coupJoueurX][coupJoueurY]=0
                    displaytab(tabmorpion)
                    if tabmorpion[3][3]==0:
                        tabmorpion[3][3]=1
                        displaytab(tabmorpion)
                        print("perdu !")
                        return
                    else:
                        tabmorpion[2][3]=1
                        displaytab(tabmorpion)
                        coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                        tabmorpion[coupJoueurX][coupJoueurY]=0
                        displaytab(tabmorpion)
                        print("égalité !")
                        return
            elif tabmorpion[3][2]==0:
                tabmorpion[3][3]=1
                displaytab(tabmorpion)
                coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                tabmorpion[coupJoueurX][coupJoueurY]=0
                displaytab(tabmorpion)
                if tabmorpion[1][1]==2:
                    tabmorpion[1][3]=1
                    displaytab(tabmorpion)
                    print("perdu !")
                    return 
                else:
                    tabmorpion[1][2]=1
                    displaytab(tabmorpion)
                    coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                    tabmorpion[coupJoueurX][coupJoueurY]=0
                    displaytab(tabmorpion)
                    if tabmorpion[3][1]==0:
                        tabmorpion[2][1]=1
                        displaytab(tabmorpion)
                        coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                        tabmorpion[coupJoueurX][coupJoueurY]=0
                        displaytab(tabmorpion)
                        print("égalité !")
                        return
                    elif tabmorpion[2][1]:
                        tabmorpion[3][1]=1
                        displaytab(tabmorpion)
                        coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                        tabmorpion[coupJoueurX][coupJoueurY]=0
                        displaytab(tabmorpion)
                        print("égalité !")
                        return
                    else:
                        tabmorpion[3][1]=1
                        displaytab(tabmorpion)
                        coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                        tabmorpion[coupJoueurX][coupJoueurY]=0
                        displaytab(tabmorpion)
                        print("égalité !")
                        return
        elif tabmorpion[3][1]==0:
            tabmorpion[2][2]=1
            displaytab(tabmorpion)
            coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
            tabmorpion[coupJoueurX][coupJoueurY]=0
            displaytab(tabmorpion)
            if tabmorpion[1][1]==0:
                tabmorpion[2][1]=1
                displaytab(tabmorpion)
                coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                tabmorpion[coupJoueurX][coupJoueurY]=0
                displaytab(tabmorpion)
                if tabmorpion[2][3]==2:
                    tabmorpion[2][3]=1
                    displaytab(tabmorpion)
                    print("perdu !")
                    return
                else:
                    tabmorpion[3][2]=1
                    displaytab(tabmorpion)
                    coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                    tabmorpion[coupJoueurX][coupJoueurY]=0
                    displaytab(tabmorpion)
                    if tabmorpion[1][2]==2:
                        tabmorpion[1][2]=1
                        displaytab(tabmorpion)
                        print("perdu !")
                        return
                    else:
                        tabmorpion[1][3]=1
                        displaytab(tabmorpion)
                        coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                        tabmorpion[coupJoueurX][coupJoueurY]=0
                        displaytab(tabmorpion)
                        print("égalité !")
                        return
            elif tabmorpion[2][1]==0:
                tabmorpion[1][1]=1
                displaytab(tabmorpion)
                coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                tabmorpion[coupJoueurX][coupJoueurY]=0
                displaytab(tabmorpion)
                if tabmorpion[3][3]==2:
                    tabmorpion[3][3]=1
                    displaytab(tabmorpion)
                    print("perdu !")
                    return
                else:
                    tabmorpion[3][2]=1
                    displaytab(tabmorpion)
                    coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                    tabmorpion[coupJoueurX][coupJoueurY]=0
                    displaytab(tabmorpion)
                    if tabmorpion[1][2]==2:
                        tabmorpion[1][2]=1
                        displaytab(tabmorpion)
                        print("perdu !")
                        return
                    else:
                        tabmorpion[3][1]=1
                        displaytab(tabmorpion)
                        coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                        tabmorpion[coupJoueurX][coupJoueurY]=0
                        displaytab(tabmorpion)
                        print("égalité !")
                        return
            elif tabmorpion[3][2]==0:
                tabmorpion[3][3]=1
                displaytab(tabmorpion)
                coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                tabmorpion[coupJoueurX][coupJoueurY]=0
                displaytab(tabmorpion)
                if tabmorpion[1][1]==2:
                    tabmorpion[1][1]=1
                    displaytab(tabmorpion)
                    print("perdu !")
                    return
                else:
                    tabmorpion[2][1]=1
                    displaytab(tabmorpion)
                    coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                    tabmorpion[coupJoueurX][coupJoueurY]=0
                    displaytab(tabmorpion)
                    if tabmorpion[2][3]==2:
                        tabmorpion[2][3]=1
                        displaytab(tabmorpion)
                        print("perdu !")
                        return
                    else:
                        tabmorpion[3][1]=1
                        displaytab(tabmorpion)
                        coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                        tabmorpion[coupJoueurX][coupJoueurY]=0
                        displaytab(tabmorpion)
                        print("égalité !")
                        return
            elif tabmorpion[3][3]==0:
                tabmorpion[3][2]=1
                displaytab(tabmorpion)
                coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                tabmorpion[coupJoueurX][coupJoueurY]=0
                displaytab(tabmorpion)
                if tabmorpion[1][2]==2:
                    tabmorpion[1][2]=1
                    displaytab(tabmorpion)
                    print("perdu !")
                    return 
                else:
                    tabmorpion[2][1]=1
                    displaytab(tabmorpion)
                    coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                    tabmorpion[coupJoueurX][coupJoueurY]=0
                    displaytab(tabmorpion)
                    if tabmorpion[2][3]==2:
                        tabmorpion[2][3]=1
                        displaytab(tabmorpion)
                        print("perdu !")
                        return
                    else:
                        tabmorpion[1][1]=1
                        displaytab(tabmorpion)
                        coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                        tabmorpion[coupJoueurX][coupJoueurY]=0
                        displaytab(tabmorpion)
                        print("égalité !")
                        return
            elif tabmorpion[2][3]==0:
                tabmorpion[3][3]=1
                displaytab(tabmorpion)
                coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                tabmorpion[coupJoueurX][coupJoueurY]=0
                displaytab(tabmorpion)
                if tabmorpion[1][1]==2:
                    tabmorpion[1][1]=1
                    displaytab(tabmorpion)
                    print("perdu !")
                    return 
                else:
                    tabmorpion[2][1]=1
                    displaytab(tabmorpion)
                    coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                    tabmorpion[coupJoueurX][coupJoueurY]=0
                    displaytab(tabmorpion)
                    if tabmorpion[1][2]==0:
                        tabmorpion[1][3]=1
                        displaytab(tabmorpion)
                        coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                        tabmorpion[coupJoueurX][coupJoueurY]=0
                        displaytab(tabmorpion)
                        print("égalité !")
                        return
                    elif tabmorpion[1][2]==0:
                        tabmorpion[1][2]=1
                        displaytab(tabmorpion)
                        coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                        tabmorpion[coupJoueurX][coupJoueurY]=0
                        displaytab(tabmorpion)
                        print("égalité !")
                        return
                    else:
                        tabmorpion[1][3]=1
                        displaytab(tabmorpion)
                        coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                        tabmorpion[coupJoueurX][coupJoueurY]=0
                        displaytab(tabmorpion)
                        print("égalité !")
                        return
            elif tabmorpion[1][3]==0:
                tabmorpion[1][2]=1
                displaytab(tabmorpion)
                coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                tabmorpion[coupJoueurX][coupJoueurY]=0
                displaytab(tabmorpion)
                if tabmorpion[3][2]==2:
                    tabmorpion[3][2]=1
                    displaytab(tabmorpion)
                    print("perdu !")
                    return 
                else:
                    tabmorpion[3][3]=1
                    displaytab(tabmorpion)
                    coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                    tabmorpion[coupJoueurX][coupJoueurY]=0
                    displaytab(tabmorpion)
                    if tabmorpion[1][1]==0:
                        tabmorpion[1][1]=1
                        displaytab(tabmorpion)
                        print("perdu !")
                        return
                    else:
                        tabmorpion[2][3]=1
                        displaytab(tabmorpion)
                        coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                        tabmorpion[coupJoueurX][coupJoueurY]=0
                        displaytab(tabmorpion)
                        print("égalité !")
                        return
            elif tabmorpion[1][2]==0:
                tabmorpion[1][1]=1
                displaytab(tabmorpion)
                coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                tabmorpion[coupJoueurX][coupJoueurY]=0
                displaytab(tabmorpion)
                if tabmorpion[3][3]==2:
                    tabmorpion[3][3]=1
                    displaytab(tabmorpion)
                    print("perdu !")
                    return 
                else:
                    tabmorpion[3][2]=1
                    displaytab(tabmorpion)
                    coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                    tabmorpion[coupJoueurX][coupJoueurY]=0
                    displaytab(tabmorpion)
                    if tabmorpion[1][3]==0:
                        tabmorpion[2][3]=1
                        displaytab(tabmorpion)
                        coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                        tabmorpion[coupJoueurX][coupJoueurY]=0
                        displaytab(tabmorpion)
                        print("égalité !")
                        return
                    elif tabmorpion[2][3]:
                        tabmorpion[1][3]=1
                        displaytab(tabmorpion)
                        coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                        tabmorpion[coupJoueurX][coupJoueurY]=0
                        displaytab(tabmorpion)
                        print("égalité !")
                        return
                    else:
                        tabmorpion[1][3]=1
                        displaytab(tabmorpion)
                        coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                        tabmorpion[coupJoueurX][coupJoueurY]=0
                        displaytab(tabmorpion)
                        print("égalité !")
                        return
        elif tabmorpion[3][3]==0:
            tabmorpion[2][2]=1
            displaytab(tabmorpion)
            coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
            tabmorpion[coupJoueurX][coupJoueurY]=0
            displaytab(tabmorpion)
            if tabmorpion[1][3]==0:
                tabmorpion[2][3]=1
                displaytab(tabmorpion)
                coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                tabmorpion[coupJoueurX][coupJoueurY]=0
                displaytab(tabmorpion)
                if tabmorpion[2][1]==2:
                    tabmorpion[2][1]=1
                    displaytab(tabmorpion)
                    print("perdu !")
                    return
                else:
                    tabmorpion[3][2]=1
                    displaytab(tabmorpion)
                    coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                    tabmorpion[coupJoueurX][coupJoueurY]=0
                    displaytab(tabmorpion)
                    if tabmorpion[1][2]==2:
                        tabmorpion[1][2]=1
                        displaytab(tabmorpion)
                        print("perdu !")
                        return
                    else:
                        tabmorpion[1][1]=1
                        displaytab(tabmorpion)
                        coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                        tabmorpion[coupJoueurX][coupJoueurY]=0
                        displaytab(tabmorpion)
                        print("égalité !")
                        return
            elif tabmorpion[2][3]==0:
                tabmorpion[1][3]=1
                displaytab(tabmorpion)
                coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                tabmorpion[coupJoueurX][coupJoueurY]=0
                displaytab(tabmorpion)
                if tabmorpion[3][1]==2:
                    tabmorpion[3][1]=1
                    displaytab(tabmorpion)
                    print("perdu !")
                    return
                else:
                    tabmorpion[3][2]=1
                    displaytab(tabmorpion)
                    coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                    tabmorpion[coupJoueurX][coupJoueurY]=0
                    displaytab(tabmorpion)
                    if tabmorpion[1][2]==2:
                        tabmorpion[1][2]=1
                        displaytab(tabmorpion)
                        print("perdu !")
                        return
                    else:
                        tabmorpion[1][1]=1
                        displaytab(tabmorpion)
                        coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                        tabmorpion[coupJoueurX][coupJoueurY]=0
                        displaytab(tabmorpion)
                        print("égalité !")
                        return
            elif tabmorpion[3][2]==0:
                tabmorpion[3][1]=1
                displaytab(tabmorpion)
                coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                tabmorpion[coupJoueurX][coupJoueurY]=0
                displaytab(tabmorpion)
                if tabmorpion[1][3]==2:
                    tabmorpion[1][3]=1
                    displaytab(tabmorpion)
                    print("perdu !")
                    return
                else:
                    tabmorpion[2][3]=1
                    displaytab(tabmorpion)
                    coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                    tabmorpion[coupJoueurX][coupJoueurY]=0
                    displaytab(tabmorpion)
                    if tabmorpion[2][1]==2:
                        tabmorpion[2][1]=1
                        displaytab(tabmorpion)
                        print("perdu !")
                        return
                    else:
                        tabmorpion[1][1]=1
                        displaytab(tabmorpion)
                        coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                        tabmorpion[coupJoueurX][coupJoueurY]=0
                        displaytab(tabmorpion)
                        print("égalité !")
                        return
            elif tabmorpion[3][1]==0:
                tabmorpion[3][2]=1
                displaytab(tabmorpion)
                coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                tabmorpion[coupJoueurX][coupJoueurY]=0
                displaytab(tabmorpion)
                if tabmorpion[1][2]==2:
                    tabmorpion[1][2]=1
                    displaytab(tabmorpion)
                    print("perdu !")
                    return 
                else:
                    tabmorpion[2][3]=1
                    displaytab(tabmorpion)
                    coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                    tabmorpion[coupJoueurX][coupJoueurY]=0
                    displaytab(tabmorpion)
                    if tabmorpion[2][1]==2:
                        tabmorpion[2][1]=1
                        displaytab(tabmorpion)
                        print("perdu !")
                        return
                    else:
                        tabmorpion[1][3]=1
                        displaytab(tabmorpion)
                        coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                        tabmorpion[coupJoueurX][coupJoueurY]=0
                        displaytab(tabmorpion)
                        print("égalité !")
                        return
            elif tabmorpion[2][1]==0:
                tabmorpion[3][1]=1
                displaytab(tabmorpion)
                coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                tabmorpion[coupJoueurX][coupJoueurY]=0
                displaytab(tabmorpion)
                if tabmorpion[1][3]==2:
                    tabmorpion[1][3]=1
                    displaytab(tabmorpion)
                    print("perdu !")
                    return 
                else:
                    tabmorpion[2][3]=1
                    displaytab(tabmorpion)
                    coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                    tabmorpion[coupJoueurX][coupJoueurY]=0
                    displaytab(tabmorpion)
                    if tabmorpion[1][2]==0:
                        tabmorpion[1][1]=1
                        displaytab(tabmorpion)
                        coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                        tabmorpion[coupJoueurX][coupJoueurY]=0
                        displaytab(tabmorpion)
                        print("égalité !")
                        return
                    elif tabmorpion[1][1]==0:
                        tabmorpion[1][2]=1
                        displaytab(tabmorpion)
                        coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                        tabmorpion[coupJoueurX][coupJoueurY]=0
                        displaytab(tabmorpion)
                        print("égalité !")
                        return
                    else:
                        tabmorpion[1][1]=1
                        displaytab(tabmorpion)
                        coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                        tabmorpion[coupJoueurX][coupJoueurY]=0
                        displaytab(tabmorpion)
                        print("égalité !")
                        return
            elif tabmorpion[1][1]==0:
                tabmorpion[1][2]=1
                displaytab(tabmorpion)
                coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                tabmorpion[coupJoueurX][coupJoueurY]=0
                displaytab(tabmorpion)
                if tabmorpion[3][2]==2:
                    tabmorpion[3][2]=1
                    displaytab(tabmorpion)
                    print("perdu !")
                    return 
                else:
                    tabmorpion[3][1]=1
                    displaytab(tabmorpion)
                    coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                    tabmorpion[coupJoueurX][coupJoueurY]=0
                    displaytab(tabmorpion)
                    if tabmorpion[1][3]==0:
                        tabmorpion[1][3]=1
                        displaytab(tabmorpion)
                        print("perdu !")
                        return
                    else:
                        tabmorpion[2][3]=1
                        displaytab(tabmorpion)
                        coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                        tabmorpion[coupJoueurX][coupJoueurY]=0
                        displaytab(tabmorpion)
                        print("égalité !")
                        return
            elif tabmorpion[1][2]==0:
                tabmorpion[1][3]=1
                displaytab(tabmorpion)
                coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                tabmorpion[coupJoueurX][coupJoueurY]=0
                displaytab(tabmorpion)
                if tabmorpion[3][1]==2:
                    tabmorpion[3][1]=1
                    displaytab(tabmorpion)
                    print("perdu !")
                    return 
                else:
                    tabmorpion[3][2]=1
                    displaytab(tabmorpion)
                    coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                    tabmorpion[coupJoueurX][coupJoueurY]=0
                    displaytab(tabmorpion)
                    if tabmorpion[1][1]==0:
                        tabmorpion[2][1]=1
                        displaytab(tabmorpion)
                        coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                        tabmorpion[coupJoueurX][coupJoueurY]=0
                        displaytab(tabmorpion)
                        print("égalité !")
                        return
                    elif tabmorpion[2][1]==0:
                        tabmorpion[1][1]=1
                        displaytab(tabmorpion)
                        coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                        tabmorpion[coupJoueurX][coupJoueurY]=0
                        displaytab(tabmorpion)
                        print("égalité !")
                        return
                    else:
                        tabmorpion[1][1]=1
                        displaytab(tabmorpion)
                        coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                        tabmorpion[coupJoueurX][coupJoueurY]=0
                        displaytab(tabmorpion)
                        print("égalité !")
                        return
        elif tabmorpion[2][1]==0:
            tabmorpion[2][2]=1
            displaytab(tabmorpion)
            coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
            tabmorpion[coupJoueurX][coupJoueurY]=0
            displaytab(tabmorpion)
            if tabmorpion[1][1]==0:
                tabmorpion[3][1]=1
                displaytab(tabmorpion)
                coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                tabmorpion[coupJoueurX][coupJoueurY]=0
                displaytab(tabmorpion)
                if tabmorpion[1][3]==2:
                    tabmorpion[1][3]=1
                    displaytab(tabmorpion)
                    print("perdu !")
                    return
                else:
                    tabmorpion[1][2]=1
                    displaytab(tabmorpion)
                    coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                    tabmorpion[coupJoueurX][coupJoueurY]=0
                    displaytab(tabmorpion)
                    if tabmorpion[3][2]==2:
                        tabmorpion[3][2]=1
                        displaytab(tabmorpion)
                        print("perdu !")
                        return
                    else:
                        tabmorpion[3][3]=1
                        displaytab(tabmorpion)
                        coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                        tabmorpion[coupJoueurX][coupJoueurY]=0
                        displaytab(tabmorpion)
                        print("égalité !")
                        return
            elif tabmorpion[3][1]==0:
                tabmorpion[1][1]=1
                displaytab(tabmorpion)
                coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                tabmorpion[coupJoueurX][coupJoueurY]=0
                displaytab(tabmorpion)
                if tabmorpion[3][3]==2:
                    tabmorpion[3][3]=1
                    displaytab(tabmorpion)
                    print("perdu !")
                    return
                else:
                    tabmorpion[3][2]=1
                    displaytab(tabmorpion)
                    coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                    tabmorpion[coupJoueurX][coupJoueurY]=0
                    displaytab(tabmorpion)
                    if tabmorpion[1][2]==2:
                        tabmorpion[1][2]=1
                        displaytab(tabmorpion)
                        print("perdu !")
                        return
                    else:
                        tabmorpion[1][3]=1
                        displaytab(tabmorpion)
                        coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                        tabmorpion[coupJoueurX][coupJoueurY]=0
                        displaytab(tabmorpion)
                        print("égalité !")
                        return
            elif tabmorpion[1][3]==0:
                tabmorpion[1][1]=1
                displaytab(tabmorpion)
                coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                tabmorpion[coupJoueurX][coupJoueurY]=0
                displaytab(tabmorpion)
                if tabmorpion[3][3]==2:
                    tabmorpion[3][3]=1
                    displaytab(tabmorpion)
                    print("perdu !")
                    return
                else:
                    tabmorpion[2][3]=1
                    displaytab(tabmorpion)
                    coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                    tabmorpion[coupJoueurX][coupJoueurY]=0
                    displaytab(tabmorpion)
                    if tabmorpion[3][3]==0:
                        tabmorpion[3][2]=1
                        displaytab(tabmorpion)
                        coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                        tabmorpion[coupJoueurX][coupJoueurY]=0
                        displaytab(tabmorpion)
                        print("égalité !")
                        return
                    else:
                        tabmorpion[3][3]=1
                        displaytab(tabmorpion)
                        coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                        tabmorpion[coupJoueurX][coupJoueurY]=0
                        displaytab(tabmorpion)
                        print("égalité !")
                        return
            elif tabmorpion[3][3]==0:
                tabmorpion[3][1]=1
                displaytab(tabmorpion)
                coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                tabmorpion[coupJoueurX][coupJoueurY]=0
                displaytab(tabmorpion)
                if tabmorpion[1][3]==2:
                    tabmorpion[1][3]=1
                    displaytab(tabmorpion)
                    print("perdu !")
                    return
                else:
                    tabmorpion[2][3]=1
                    displaytab(tabmorpion)
                    coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                    tabmorpion[coupJoueurX][coupJoueurY]=0
                    displaytab(tabmorpion)
                    if tabmorpion[1][1]==0:
                        tabmorpion[1][2]=1
                        displaytab(tabmorpion)
                        coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                        tabmorpion[coupJoueurX][coupJoueurY]=0
                        displaytab(tabmorpion)
                        print("égalité !")
                        return
                    else:
                        tabmorpion[1][1]=1
                        displaytab(tabmorpion)
                        coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                        tabmorpion[coupJoueurX][coupJoueurY]=0
                        displaytab(tabmorpion)
                        print("égalité !")
                        return
            elif tabmorpion[1][2]==0:
                tabmorpion[1][1]=1
                displaytab(tabmorpion)
                coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                tabmorpion[coupJoueurX][coupJoueurY]=0
                displaytab(tabmorpion)
                if tabmorpion[3][3]==2:
                    tabmorpion[3][3]=1
                    displaytab(tabmorpion)
                    print("perdu !")
                    return
                else:
                    tabmorpion[1][3]=1
                    displaytab(tabmorpion)
                    coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                    tabmorpion[coupJoueurX][coupJoueurY]=0
                    displaytab(tabmorpion)
                    if tabmorpion[3][1]==0:
                        tabmorpion[3][1]=1
                        displaytab(tabmorpion)
                        print("perdu !")
                        return
                    else:
                        tabmorpion[3][2]=1
                        displaytab(tabmorpion)
                        coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                        tabmorpion[coupJoueurX][coupJoueurY]=0
                        displaytab(tabmorpion)
                        print("égalité !")
                        return
            elif tabmorpion[3][2]==0:
                tabmorpion[3][1]=1
                displaytab(tabmorpion)
                coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                tabmorpion[coupJoueurX][coupJoueurY]=0
                displaytab(tabmorpion)
                if tabmorpion[1][3]==2:
                    tabmorpion[1][3]=1
                    displaytab(tabmorpion)
                    print("perdu !")
                    return
                else:
                    tabmorpion[3][3]=1
                    displaytab(tabmorpion)
                    coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                    tabmorpion[coupJoueurX][coupJoueurY]=0
                    displaytab(tabmorpion)
                    if tabmorpion[1][1]==0:
                        tabmorpion[1][1]=1
                        displaytab(tabmorpion)
                        print("perdu !")
                        return
                    else:
                        tabmorpion[1][2]=1
                        displaytab(tabmorpion)
                        coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                        tabmorpion[coupJoueurX][coupJoueurY]=0
                        displaytab(tabmorpion)
                        print("égalité !")
                        return
            elif tabmorpion[2][3]==0:
                tabmorpion[1][1]=1
                displaytab(tabmorpion)
                coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                tabmorpion[coupJoueurX][coupJoueurY]=0
                displaytab(tabmorpion)
                if tabmorpion[3][3]==2:
                    tabmorpion[3][3]=1
                    displaytab(tabmorpion)
                    print("perdu !")
                    return
                else:
                    tabmorpion[1][3]=1
                    displaytab(tabmorpion)
                    coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                    tabmorpion[coupJoueurX][coupJoueurY]=0
                    displaytab(tabmorpion)
                    if tabmorpion[3][1]==0:
                        tabmorpion[3][1]=1
                        displaytab(tabmorpion)
                        print("perdu !")
                        return
                    else:
                        tabmorpion[1][2]=1
                        displaytab(tabmorpion)
                        print("perdu !")
                        return
            #kkgbvuzeyvbuzeyviozraaaaayyofg
        elif tabmorpion[1][2]==0:
            tabmorpion[2][2]=1
            displaytab(tabmorpion)
            coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
            tabmorpion[coupJoueurX][coupJoueurY]=0
            displaytab(tabmorpion)
            if tabmorpion[1][1]==0:
                tabmorpion[1][3]=1
                displaytab(tabmorpion)
                coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                tabmorpion[coupJoueurX][coupJoueurY]=0
                displaytab(tabmorpion)
                if tabmorpion[3][1]==2:
                    tabmorpion[3][1]=1
                    displaytab(tabmorpion)
                    print("perdu !")
                    return
                else:
                    tabmorpion[2][1]=1
                    displaytab(tabmorpion)
                    coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                    tabmorpion[coupJoueurX][coupJoueurY]=0
                    displaytab(tabmorpion)
                    if tabmorpion[2][3]==2:
                        tabmorpion[2][3]=1
                        displaytab(tabmorpion)
                        print("perdu !")
                        return
                    else:
                        tabmorpion[3][3]=1
                        displaytab(tabmorpion)
                        coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                        tabmorpion[coupJoueurX][coupJoueurY]=0
                        displaytab(tabmorpion)
                        print("égalité !")
                        return
            elif tabmorpion[1][3]==0:
                tabmorpion[1][1]=1
                displaytab(tabmorpion)
                coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                tabmorpion[coupJoueurX][coupJoueurY]=0
                displaytab(tabmorpion)
                if tabmorpion[3][3]==2:
                    tabmorpion[3][3]=1
                    displaytab(tabmorpion)
                    print("perdu !")
                    return
                else:
                    tabmorpion[2][3]=1
                    displaytab(tabmorpion)
                    coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                    tabmorpion[coupJoueurX][coupJoueurY]=0
                    displaytab(tabmorpion)
                    if tabmorpion[2][1]==2:
                        tabmorpion[2][1]=1
                        displaytab(tabmorpion)
                        print("perdu !")
                        return
                    else:
                        tabmorpion[3][1]=1
                        displaytab(tabmorpion)
                        coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                        tabmorpion[coupJoueurX][coupJoueurY]=0
                        displaytab(tabmorpion)
                        print("égalité !")
                        return
            elif tabmorpion[3][1]==0:
                tabmorpion[1][1]=1
                displaytab(tabmorpion)
                coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                tabmorpion[coupJoueurX][coupJoueurY]=0
                displaytab(tabmorpion)
                if tabmorpion[3][3]==2:
                    tabmorpion[3][3]=1
                    displaytab(tabmorpion)
                    print("perdu !")
                    return
                else:
                    tabmorpion[3][2]=1
                    displaytab(tabmorpion)
                    coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                    tabmorpion[coupJoueurX][coupJoueurY]=0
                    displaytab(tabmorpion)
                    if tabmorpion[1][3]==0:
                        tabmorpion[2][3]=1
                        displaytab(tabmorpion)
                        coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                        tabmorpion[coupJoueurX][coupJoueurY]=0
                        displaytab(tabmorpion)
                        print("égalité !")
                        return
                    else:
                        tabmorpion[1][3]=1
                        displaytab(tabmorpion)
                        coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                        tabmorpion[coupJoueurX][coupJoueurY]=0
                        displaytab(tabmorpion)
                        print("égalité !")
                        return
            elif tabmorpion[3][3]==0:
                tabmorpion[1][3]=1
                displaytab(tabmorpion)
                coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                tabmorpion[coupJoueurX][coupJoueurY]=0
                displaytab(tabmorpion)
                if tabmorpion[3][1]==2:
                    tabmorpion[3][1]=1
                    displaytab(tabmorpion)
                    print("perdu !")
                    return
                else:
                    tabmorpion[3][2]=1
                    displaytab(tabmorpion)
                    coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                    tabmorpion[coupJoueurX][coupJoueurY]=0
                    displaytab(tabmorpion)
                    if tabmorpion[1][1]==0:
                        tabmorpion[1][2]=1
                        displaytab(tabmorpion)
                        coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                        tabmorpion[coupJoueurX][coupJoueurY]=0
                        displaytab(tabmorpion)
                        print("égalité !")
                        return
                    else:
                        tabmorpion[1][1]=1
                        displaytab(tabmorpion)
                        coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                        tabmorpion[coupJoueurX][coupJoueurY]=0
                        displaytab(tabmorpion)
                        print("égalité !")
                        return
            elif tabmorpion[2][1]==0:
                tabmorpion[1][1]=1
                displaytab(tabmorpion)
                coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                tabmorpion[coupJoueurX][coupJoueurY]=0
                displaytab(tabmorpion)
                if tabmorpion[3][3]==2:
                    tabmorpion[3][3]=1
                    displaytab(tabmorpion)
                    print("perdu !")
                    return
                else:
                    tabmorpion[1][3]=1
                    displaytab(tabmorpion)
                    coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                    tabmorpion[coupJoueurX][coupJoueurY]=0
                    displaytab(tabmorpion)
                    if tabmorpion[3][1]==0:
                        tabmorpion[3][1]=1
                        displaytab(tabmorpion)
                        print("perdu !")
                        return
                    else:
                        tabmorpion[3][2]=1
                        displaytab(tabmorpion)
                        coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                        tabmorpion[coupJoueurX][coupJoueurY]=0
                        displaytab(tabmorpion)
                        print("égalité !")
                        return
            elif tabmorpion[2][3]==0:
                tabmorpion[1][3]=1
                displaytab(tabmorpion)
                coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                tabmorpion[coupJoueurX][coupJoueurY]=0
                displaytab(tabmorpion)
                if tabmorpion[3][1]==2:
                    tabmorpion[3][1]=1
                    displaytab(tabmorpion)
                    print("perdu !")
                    return
                else:
                    tabmorpion[1][1]=1
                    displaytab(tabmorpion)
                    coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                    tabmorpion[coupJoueurX][coupJoueurY]=0
                    displaytab(tabmorpion)
                    if tabmorpion[3][3]==0:
                        tabmorpion[3][3]=1
                        displaytab(tabmorpion)
                        print("perdu !")
                        return
                    else:
                        tabmorpion[3][2]=1
                        displaytab(tabmorpion)
                        coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                        tabmorpion[coupJoueurX][coupJoueurY]=0
                        displaytab(tabmorpion)
                        print("égalité !")
                        return
            elif tabmorpion[3][2]==0:
                tabmorpion[1][1]=1
                displaytab(tabmorpion)
                coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                tabmorpion[coupJoueurX][coupJoueurY]=0
                displaytab(tabmorpion)
                if tabmorpion[3][3]==2:
                    tabmorpion[3][3]=1
                    displaytab(tabmorpion)
                    print("perdu !")
                    return
                else:
                    tabmorpion[3][1]=1
                    displaytab(tabmorpion)
                    coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                    tabmorpion[coupJoueurX][coupJoueurY]=0
                    displaytab(tabmorpion)
                    if tabmorpion[1][3]==0:
                        tabmorpion[1][3]=1
                        displaytab(tabmorpion)
                        print("perdu !")
                        return
                    else:
                        tabmorpion[1][2]=1
                        displaytab(tabmorpion)
                        print("perdu !")
                        return
        elif tabmorpion[2][3]==0:
            tabmorpion[2][2]=1
            displaytab(tabmorpion)
            coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
            tabmorpion[coupJoueurX][coupJoueurY]=0
            displaytab(tabmorpion)
            if tabmorpion[1][3]==0:
                tabmorpion[3][3]=1
                displaytab(tabmorpion)
                coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                tabmorpion[coupJoueurX][coupJoueurY]=0
                displaytab(tabmorpion)
                if tabmorpion[1][1]==2:
                    tabmorpion[1][1]=1
                    displaytab(tabmorpion)
                    print("perdu !")
                    return
                else:
                    tabmorpion[1][2]=1
                    displaytab(tabmorpion)
                    coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                    tabmorpion[coupJoueurX][coupJoueurY]=0
                    displaytab(tabmorpion)
                    if tabmorpion[3][2]==2:
                        tabmorpion[3][2]=1
                        displaytab(tabmorpion)
                        print("perdu !")
                        return
                    else:
                        tabmorpion[3][1]=1
                        displaytab(tabmorpion)
                        coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                        tabmorpion[coupJoueurX][coupJoueurY]=0
                        displaytab(tabmorpion)
                        print("égalité !")
                        return
            elif tabmorpion[3][3]==0:
                tabmorpion[1][3]=1
                displaytab(tabmorpion)
                coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                tabmorpion[coupJoueurX][coupJoueurY]=0
                displaytab(tabmorpion)
                if tabmorpion[3][1]==2:
                    tabmorpion[3][1]=1
                    displaytab(tabmorpion)
                    print("perdu !")
                    return
                else:
                    tabmorpion[3][2]=1
                    displaytab(tabmorpion)
                    coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                    tabmorpion[coupJoueurX][coupJoueurY]=0
                    displaytab(tabmorpion)
                    if tabmorpion[1][2]==2:
                        tabmorpion[1][2]=1
                        displaytab(tabmorpion)
                        print("perdu !")
                        return
                    else:
                        tabmorpion[1][1]=1
                        displaytab(tabmorpion)
                        coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                        tabmorpion[coupJoueurX][coupJoueurY]=0
                        displaytab(tabmorpion)
                        print("égalité !")
                        return
            elif tabmorpion[1][1]==0:
                tabmorpion[1][3]=1
                displaytab(tabmorpion)
                coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                tabmorpion[coupJoueurX][coupJoueurY]=0
                displaytab(tabmorpion)
                if tabmorpion[3][1]==2:
                    tabmorpion[3][1]=1
                    displaytab(tabmorpion)
                    print("perdu !")
                    return
                else:
                    tabmorpion[2][1]=1
                    displaytab(tabmorpion)
                    coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                    tabmorpion[coupJoueurX][coupJoueurY]=0
                    displaytab(tabmorpion)
                    if tabmorpion[3][3]==0:
                        tabmorpion[3][2]=1
                        displaytab(tabmorpion)
                        coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                        tabmorpion[coupJoueurX][coupJoueurY]=0
                        displaytab(tabmorpion)
                        print("égalité !")
                        return
                    else:
                        tabmorpion[3][3]=1
                        displaytab(tabmorpion)
                        coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                        tabmorpion[coupJoueurX][coupJoueurY]=0
                        displaytab(tabmorpion)
                        print("égalité !")
                        return
            elif tabmorpion[3][1]==0:
                tabmorpion[3][3]=1
                displaytab(tabmorpion)
                coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                tabmorpion[coupJoueurX][coupJoueurY]=0
                displaytab(tabmorpion)
                if tabmorpion[1][1]==2:
                    tabmorpion[1][1]=1
                    displaytab(tabmorpion)
                    print("perdu !")
                    return
                else:
                    tabmorpion[2][1]=1
                    displaytab(tabmorpion)
                    coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                    tabmorpion[coupJoueurX][coupJoueurY]=0
                    displaytab(tabmorpion)
                    if tabmorpion[1][3]==0:
                        tabmorpion[1][2]=1
                        displaytab(tabmorpion)
                        coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                        tabmorpion[coupJoueurX][coupJoueurY]=0
                        displaytab(tabmorpion)
                        print("égalité !")
                        return
                    else:
                        tabmorpion[1][3]=1
                        displaytab(tabmorpion)
                        coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                        tabmorpion[coupJoueurX][coupJoueurY]=0
                        displaytab(tabmorpion)
                        print("égalité !")
                        return
            elif tabmorpion[1][2]==0:
                tabmorpion[1][3]=1
                displaytab(tabmorpion)
                coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                tabmorpion[coupJoueurX][coupJoueurY]=0
                displaytab(tabmorpion)
                if tabmorpion[3][1]==2:
                    tabmorpion[3][1]=1
                    displaytab(tabmorpion)
                    print("perdu !")
                    return
                else:
                    tabmorpion[1][1]=1
                    displaytab(tabmorpion)
                    coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                    tabmorpion[coupJoueurX][coupJoueurY]=0
                    displaytab(tabmorpion)
                    if tabmorpion[3][3]==0:
                        tabmorpion[3][3]=1
                        displaytab(tabmorpion)
                        print("perdu !")
                        return
                    else:
                        tabmorpion[3][2]=1
                        displaytab(tabmorpion)
                        coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                        tabmorpion[coupJoueurX][coupJoueurY]=0
                        displaytab(tabmorpion)
                        print("égalité !")
                        return
            elif tabmorpion[3][2]==0:
                tabmorpion[3][3]=1
                displaytab(tabmorpion)
                coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                tabmorpion[coupJoueurX][coupJoueurY]=0
                displaytab(tabmorpion)
                if tabmorpion[1][1]==2:
                    tabmorpion[1][1]=1
                    displaytab(tabmorpion)
                    print("perdu !")
                    return
                else:
                    tabmorpion[3][1]=1
                    displaytab(tabmorpion)
                    coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                    tabmorpion[coupJoueurX][coupJoueurY]=0
                    displaytab(tabmorpion)
                    if tabmorpion[1][3]==0:
                        tabmorpion[1][3]=1
                        displaytab(tabmorpion)
                        print("perdu !")
                        return
                    else:
                        tabmorpion[1][2]=1
                        displaytab(tabmorpion)
                        coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                        tabmorpion[coupJoueurX][coupJoueurY]=0
                        displaytab(tabmorpion)
                        print("égalité !")
                        return
            elif tabmorpion[2][1]==0:
                tabmorpion[1][1]=1
                displaytab(tabmorpion)
                coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                tabmorpion[coupJoueurX][coupJoueurY]=0
                displaytab(tabmorpion)
                if tabmorpion[3][3]==2:
                    tabmorpion[3][3]=1
                    displaytab(tabmorpion)
                    print("perdu !")
                    return
                else:
                    tabmorpion[1][3]=1
                    displaytab(tabmorpion)
                    coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                    tabmorpion[coupJoueurX][coupJoueurY]=0
                    displaytab(tabmorpion)
                    if tabmorpion[3][1]==0:
                        tabmorpion[3][1]=1
                        displaytab(tabmorpion)
                        print("perdu !")
                        return
                    else:
                        tabmorpion[1][2]=1
                        displaytab(tabmorpion)
                        print("perdu !")
                        return
        elif tabmorpion[3][2]==0:
            tabmorpion[2][2]=1
            displaytab(tabmorpion)
            coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
            tabmorpion[coupJoueurX][coupJoueurY]=0
            displaytab(tabmorpion)
            if tabmorpion[3][3]==0:
                tabmorpion[3][1]=1
                displaytab(tabmorpion)
                coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                tabmorpion[coupJoueurX][coupJoueurY]=0
                displaytab(tabmorpion)
                if tabmorpion[1][3]==2:
                    tabmorpion[1][3]=1
                    displaytab(tabmorpion)
                    print("perdu !")
                    return
                else:
                    tabmorpion[2][3]=1
                    displaytab(tabmorpion)
                    coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                    tabmorpion[coupJoueurX][coupJoueurY]=0
                    displaytab(tabmorpion)
                    if tabmorpion[2][1]==2:
                        tabmorpion[2][1]=1
                        displaytab(tabmorpion)
                        print("perdu !")
                        return
                    else:
                        tabmorpion[1][1]=1
                        displaytab(tabmorpion)
                        coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                        tabmorpion[coupJoueurX][coupJoueurY]=0
                        displaytab(tabmorpion)
                        print("égalité !")
                        return
            elif tabmorpion[3][1]==0:
                tabmorpion[3][3]=1
                displaytab(tabmorpion)
                coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                tabmorpion[coupJoueurX][coupJoueurY]=0
                displaytab(tabmorpion)
                if tabmorpion[1][1]==2:
                    tabmorpion[1][1]=1
                    displaytab(tabmorpion)
                    print("perdu !")
                    return
                else:
                    tabmorpion[2][1]=1
                    displaytab(tabmorpion)
                    coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                    tabmorpion[coupJoueurX][coupJoueurY]=0
                    displaytab(tabmorpion)
                    if tabmorpion[2][3]==2:
                        tabmorpion[2][3]=1
                        displaytab(tabmorpion)
                        print("perdu !")
                        return
                    else:
                        tabmorpion[1][3]=1
                        displaytab(tabmorpion)
                        coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                        tabmorpion[coupJoueurX][coupJoueurY]=0
                        displaytab(tabmorpion)
                        print("égalité !")
                        return
            elif tabmorpion[1][1]==0:
                tabmorpion[3][1]=1
                displaytab(tabmorpion)
                coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                tabmorpion[coupJoueurX][coupJoueurY]=0
                displaytab(tabmorpion)
                if tabmorpion[1][3]==2:
                    tabmorpion[1][3]=1
                    displaytab(tabmorpion)
                    print("perdu !")
                    return
                else:
                    tabmorpion[1][2]=1
                    displaytab(tabmorpion)
                    coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                    tabmorpion[coupJoueurX][coupJoueurY]=0
                    displaytab(tabmorpion)
                    if tabmorpion[3][3]==0:
                        tabmorpion[2][3]=1
                        displaytab(tabmorpion)
                        coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                        tabmorpion[coupJoueurX][coupJoueurY]=0
                        displaytab(tabmorpion)
                        print("égalité !")
                        return
                    else:
                        tabmorpion[3][3]=1
                        displaytab(tabmorpion)
                        coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                        tabmorpion[coupJoueurX][coupJoueurY]=0
                        displaytab(tabmorpion)
                        print("égalité !")
                        return
            elif tabmorpion[1][3]==0:
                tabmorpion[3][3]=1
                displaytab(tabmorpion)
                coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                tabmorpion[coupJoueurX][coupJoueurY]=0
                displaytab(tabmorpion)
                if tabmorpion[1][1]==2:
                    tabmorpion[1][1]=1
                    displaytab(tabmorpion)
                    print("perdu !")
                    return
                else:
                    tabmorpion[1][2]=1
                    displaytab(tabmorpion)
                    coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                    tabmorpion[coupJoueurX][coupJoueurY]=0
                    displaytab(tabmorpion)
                    if tabmorpion[3][1]==0:
                        tabmorpion[2][1]=1
                        displaytab(tabmorpion)
                        coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                        tabmorpion[coupJoueurX][coupJoueurY]=0
                        displaytab(tabmorpion)
                        print("égalité !")
                        return
                    else:
                        tabmorpion[3][1]=1
                        displaytab(tabmorpion)
                        coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                        tabmorpion[coupJoueurX][coupJoueurY]=0
                        displaytab(tabmorpion)
                        print("égalité !")
                        return
            elif tabmorpion[2][1]==0:
                tabmorpion[3][1]=1
                displaytab(tabmorpion)
                coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                tabmorpion[coupJoueurX][coupJoueurY]=0
                displaytab(tabmorpion)
                if tabmorpion[1][3]==2:
                    tabmorpion[1][3]=1
                    displaytab(tabmorpion)
                    print("perdu !")
                    return
                else:
                    tabmorpion[3][3]=1
                    displaytab(tabmorpion)
                    coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                    tabmorpion[coupJoueurX][coupJoueurY]=0
                    displaytab(tabmorpion)
                    if tabmorpion[3][1]==0:
                        tabmorpion[3][1]=1
                        displaytab(tabmorpion)
                        print("perdu !")
                        return
                    else:
                        tabmorpion[1][2]=1
                        displaytab(tabmorpion)
                        coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                        tabmorpion[coupJoueurX][coupJoueurY]=0
                        displaytab(tabmorpion)
                        print("égalité !")
                        return
            elif tabmorpion[2][3]==0:
                tabmorpion[3][3]=1
                displaytab(tabmorpion)
                coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                tabmorpion[coupJoueurX][coupJoueurY]=0
                displaytab(tabmorpion)
                if tabmorpion[1][1]==2:
                    tabmorpion[1][1]=1
                    displaytab(tabmorpion)
                    print("perdu !")
                    return
                else:
                    tabmorpion[3][1]=1
                    displaytab(tabmorpion)
                    coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                    tabmorpion[coupJoueurX][coupJoueurY]=0
                    displaytab(tabmorpion)
                    if tabmorpion[1][3]==0:
                        tabmorpion[1][3]=1
                        displaytab(tabmorpion)
                        print("perdu !")
                        return
                    else:
                        tabmorpion[1][2]=1
                        displaytab(tabmorpion)
                        coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                        tabmorpion[coupJoueurX][coupJoueurY]=0
                        displaytab(tabmorpion)
                        print("égalité !")
                        return
            elif tabmorpion[1][2]==0:
                tabmorpion[1][1]=1
                displaytab(tabmorpion)
                coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                tabmorpion[coupJoueurX][coupJoueurY]=0
                displaytab(tabmorpion)
                if tabmorpion[3][3]==2:
                    tabmorpion[3][3]=1
                    displaytab(tabmorpion)
                    print("perdu !")
                    return
                else:
                    tabmorpion[3][1]=1
                    displaytab(tabmorpion)
                    coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
                    tabmorpion[coupJoueurX][coupJoueurY]=0
                    displaytab(tabmorpion)
                    if tabmorpion[1][3]==0:
                        tabmorpion[1][3]=1
                        displaytab(tabmorpion)
                        print("perdu !")
                        return
                    else:
                        tabmorpion[1][2]=1
                        displaytab(tabmorpion)
                        print("perdu !")
                        return
        elif tabmorpion[2][2]==0:
            tabmorpion[1][1]
            displaytab(tabmorpion)
            coupJoueurX,coupJoueurY=int(input("choisir la case souhaité : ")), int(input("choisir la case souhaité : "))
            tabmorpion[coupJoueurX][coupJoueurY]=0
            displaytab(tabmorpion)
