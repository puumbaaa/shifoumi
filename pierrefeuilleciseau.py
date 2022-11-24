import random

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

jouer=int(input("pierre = 0 | feuille = 1 | ciseau = 2"))
PierreFeuilleCiseau(jouer)

    
