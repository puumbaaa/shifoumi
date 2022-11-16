import random

def PierreFeuilleCiseau(pfc_joueur):
    pfc=["pierre","feuille","ciseau"]
    pfc_ordi=random.randint(0,2)
    if pfc_ordi==pfc_joueur:
        print("égalité !")
    elif (pfc_ordi==0 and pfc_joueur==2) or (pfc_ordi==1 and pfc_joueur==0) or (pfc_ordi==2 and pfc_joueur==1):
        print("perdu !")
    elif (pfc_ordi==2 and pfc_joueur==0) or (pfc_ordi==0 and pfc_joueur==1) or (pfc_ordi==1 and pfc_joueur==2):
        print("gagné !")
