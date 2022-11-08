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

