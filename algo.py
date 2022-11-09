from random import *
from time import *

def inputt():
   alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
   caractère="r"
   caractèrealeatoire=None
   temps=time()
   print(temps)
   while caractèrealeatoire!=caractère:
      #définition d'une variable aléatoire entre 0 et 26
      caractèrealeatoire=alphabet[randint(0,25)]     
   #renvoie un caractere de type string au hasard
   temps2=time()
   print("bravo tu as trouvé le caractère secret qui est :",caractère)
   print(temps2)
   return
inputt()

tableau=[0,1,2,3,4,5,6,7,8,9,15,17,18,19,2,84,581,8892,84]

def concat(str1,str2):
   #retourne les chaines de caractères concaténées avec une virgule au milieu
   return(str1+", "+str2)

def indextab(tableau,variable):
   indexvariable=""
   for i in range (len(tableau)):
      if tableau[i]==variable:
         indexvariabel + str(i) + ", "
   return indexvariable
tableau1=[0,1,1,0,0,1,1,0,0,1]
print(indextab(tableau1,0))

listeutilisateur={"Gabriel":"1234","Gwendal":"5678","Rayouyouchan":"UwU"}
def login (userName,password,listUser):
   if userName in listUser:
      if listUser[userName]==password:
         return "connexion réussi"
   else :
      return "utilisateur ou mot de passe incorrect"


def indextab2(tab,var):
   i=0
   chaineResultat=""
   firstTurn=True
   while i< len(tab):
      if tab[i]==var:
         if firstTurn==True:
            chaineResultat += str(i)
            firstTurn=False
         else:
            chaineResultat= concat(chaineResultat, str(i))
      i+=1
   return chaineResultat   