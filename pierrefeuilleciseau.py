# on admet une fonction 'random' qui choisit au hasard une valeur comprise entre 0 et 2 lors de son exécution
import random
# on admet 'input' une fonction qui récupère l'entrée d'un joueur lors de son exécution
# on admet 'attendre' une fonction qui permet d'ajoute du temps entre les exécutions
import time

# on affiche le didacticiel du jeu expliquant les règles mais aussi expliquant les fonctions et comment s'en servir
print("DIDACTICIEL")
print("- ceci est un jeu pierre feuille ciseaux -")
print("- il y a deux type de jeu joueur contre bot / jcb ou joueur contre joueur / jcj")
print("- il y a quatre langue utilisable : Français, Englais, Japonais et Chinois")
print("- il faut appeler la fonction grace au commande .match(genre, langue) ou tournoi(genre,langue) en fonction de vos envis")
print("- tout dois ètre ecrit en minuscule et sans accents")

# créer un dico 'langueliste'
langueliste = {
    # ajouter une liste pour le jeu pierre-feuille-ciseau en français / ['pierre','feuille','ciseaux'] a 'langueliste'
    'français' : ['pierre','feuille','ciseaux'],
    # ajouter une liste pour le jeu pierre-feuille-ciseau en chinois / ['chi','fou','mi'] a 'langueliste'
    'chinois' : ['chi','fou','mi'],
    # ajouter une liste pour le jeu pierre-feuille-ciseau en anglais / ['rock','paper','scisors'] a 'langueliste'
    'anglais' : ['rock','paper','scisors'],
    # ajouter une liste pour le jeu pierre-feuille-ciseau en japonais / ['jan','ken','pon'] a 'langueliste'
    'japonais' : ['jan','ken','pon']
}

# on défini 'fin' une fonction qui prend en paramètre langue et qui permet de faire une fin plus esthétique au match
def fin(langue):
    # créer 'liste' une liste qui prend les valeurs de dico en fonction de la clé langue
    liste = langueliste[langue]
    # on affiche la valeur de 'liste' correspondant a l'index 0
    print(liste[0])
    # attend 1.5 sec
    time.sleep(1.5)
    # on affiche la valeur de 'liste' correspondant a l'index 1
    print(liste[1])
    # attend 1.5 sec
    time.sleep(1.5)
    # on affiche la valeur de 'liste' correspondant a l'index 2
    print(liste[2])
    # attend 1.5 sec
    time.sleep(1.5)

# on défini 'match' une fonction qui exécute le jeu pierre feuille ciseau et prend en paramètre une langue et genre (' jcj' ou 'jcb' )
def match(genre, langue):
    # créer 'liste' une liste qui prend les valeurs de 'langueliste' en fonction de la clé langue
    liste = langueliste[langue]
    
    # si genre est égal a 'jcb'
    if genre == 'jcb':
        # alors créer une variable 'choixbot' qui assigne une valeur de 'liste' grâce à un index donner par un entier entre 0 et 2 venant du retour de 'random'
        choixbot = liste[int(random.randint(0, 2))]
        # alors créer une variable 'choixjoueur' qui assigne une valeur de 'liste' grâce à un index donner par un entier entre 0 et 2 venant du retour de 'input' en affichant les valeurs de 'liste' et leur index
        choixjoueur = liste[int(input("choisissez votre coup : 0 = pierre, 1 = feuille, 2 = ciseaux"))]

        # on compare le 'choixbot' au 'choixjoueur' et s'il y a égalité donc que 'choixbot' est égal a 'choixjoueur'
        if choixjoueur == choixbot:
            # alors utiliser la fonction 'fin', afficher 'égalité' et le choix de chacun
            fin(langue)
            print("il y a eu une égalité car le bot et vous avez choisi",choixjoueur)
            return
        # si le joueur gagne donc si le joueur a pierre contre ciseaux ou feuille contre pierre ou ciseaux contre feuille
        elif choixjoueur == 'pierre' and choixbot == 'ciseaux' or choixjoueur == 'ciseaux' and choixbot == 'feuille' or choixjoueur == 'feuille' and choixbot == 'pierre':
            # alors utiliser la fonction 'fin', afficher "vous avez gagner", le choix de chacun et retourner 1
            fin(langue)
            print("vous avez gagné avec",choixjoueur,"contre",choixbot)
            return 1
        # sinon (si le bot gagne)
        else:
            # alors utiliser la fonction 'fin', afficher "vous avez perdu", le choix de chacun et retourner 0
            fin(langue)
            print("vous avez perdu avec",choixjoueur,"contre",choixbot)
            return 0

    # si genre est égal a 'jcj'
    if genre == 'jcj':
        # alors créer une variable 'choixjoueur1' qui assigne une valeur de liste grâce à un index donner par un entier entre 0 et 2 venant du retour de 'input' en affichant les valeurs de 'liste' et leur index
        choixjoueur1 = liste[int(input("choisissez votre coup : 0 = pierre, 1 = feuille, 2 = ciseaux"))]
        # alors créer une variable 'choixjoueur2' qui assigne une valeur de liste grâce à un index donner par un entier entre 0 et 2 venant du retour de 'input' en affichant les valeurs de 'liste' et leur index
        choixjoueur2 = liste[int(input("choisissez votre coup : 0 = pierre, 1 = feuille, 2 = ciseaux"))]

        # on compare le 'choixjoueur1' au 'choixjoueur2' et s'il y a égalité donc que 'choixjoueur1' est égal a 'choixjoueur2'
        if choixjoueur1 == choixjoueur2 :
            # alors utiliser la fonction 'fin', afficher 'égalité' et le choix de chacun
            fin(langue)
            print("il y a eu une égalité car le bot et vous avez choisi",choixjoueur1)
            return
        # si le joueur1 gagne donc si le joueur1 a pierre contre ciseaux ou feuille contre pierre ou ciseaux contre feuille
        elif choixjoueur1 == 'pierre' and choixjoueur2 == 'ciseaux' or choixjoueur1 == 'ciseaux' and choixjoueur2 == 'feuille' or choixjoueur1 == 'feuille' and choixjoueur2 == 'pierre':
            # alors utiliser la fonction 'fin', afficher "joueur1 a gagné", le choix de chacun et retourner 1
            fin(langue)
            print("joueur1 a gagné avec",choixjoueur1,"contre",choixjoueur2)
            return 1
        # sinon (si le joueur2 gagne)
        else:
            # alors utiliser la fonction 'fin', afficher "joueur2 a gagné", le choix de chacun et retourner 0
            fin(langue)
            print("joueur2 a gagné avec",choixjoueur2,"contre",choixjoueur1)
            return 0

# on défini 'tournoi' une fonction qui prend en paramètre nbmatch le nombre de match souhaité, langue et genre ( 'jcj' ou 'jcb' )
def tournoi(nbmatch, genre, langue):
    
    # si genre est égal a 'jcb'
    if genre == 'jcb':
        # on crée 'pointjoueur' une variable égale a 0
        pointjoueur = 0
        # on crée 'pointbot' une variable égale a 0
        pointbot = 0
        
        # tant que nbmatch est supérieur à 0
        while nbmatch > 0:
            # on joue un match en utilisant la fonction dont le retour est nommé 'retourmatch'
            retourmatch = match(genre, langue)
            # si 'retourmatch' est égal à 1
            if retourmatch == 1:
                # alors on ajoute 1 a 'pointjoueur'
                pointjoueur += 1
            # si 'retourmatch' est égal à 0
            elif retourmatch == 0:
                # alors on ajoute 1 a 'pointbot'
                pointbot += 1
            # retire 1 a nbmatch
            nbmatch -= 1
        
        # si 'pointjoueur' est supérieur a 'pointbot'
        if pointjoueur > pointbot:
            # alors afficher "vous avez gagne avec /pointjoueur/ points contre /pointbot/"
            print("vous avez gagné avec ",pointjoueur," points contre ",pointbot," points")
        # si 'pointbot' est supérieur a 'pointjoueur'
        elif pointbot > pointjoueur:
            # alors retourner "vous avez perdu avec /pointjoueur/ points contre /pointbot/"
            print("vous avez perdu avec ",pointjoueur," points contre ",pointbot," points")
        # sinon il y a égalité
        else:
            # alors afficher égalité
            print("égalité, vous et le bot avez ",pointjoueur," points")

    # si genre est égal a 'jcj'
    if genre == 'jcj':
        # on crée 'pointjoueur1' une variable égale a 0
        pointjoueur1 = 0
        # on crée 'pointjoueur2' une variable égale a 0
        pointjoueur2 = 0

        # tant que nbmatch est supérieur à 0
        while nbmatch > 0:
            # on joue un match en utilisant la fonction dont le retour est nommé 'retourmatch'
            retourmatch = match(genre, langue)
            # si 'retourmatch' est égal a 1
            if retourmatch == 1:
                # alors on ajoute 1 a 'pointjoueur1'
                pointjoueur1 +=1
            # si 'retourmatch' est égal a 0
            elif retourmatch == 0:
                # alors on ajoute 1 a 'pointjoueur2'
                pointjoueur2 += 1
            # retire 1 a nbmatch
            nbmatch -= 1

        # si 'pointjoueur1' est supérieur a 'pointjoueur2'
        if pointjoueur1 > pointjoueur2:
            # alors retourner 'joueur1 a gagne avec /pointjoueur1/ points contre /pointjoueur2/'
            print("joueur1 gagné avec ",pointjoueur1," points contre ",pointjoueur2," points")
        # si 'pointjoueur2' est supérieur a 'pointjoueur1'
        elif pointjoueur2 > pointjoueur1:
            # alors retourner 'joueur2 a gagne avec /pointjoueur2/ points contre /pointjoueur1/'
            print("joueur2 gagné avec ",pointjoueur2," points contre ",pointjoueur1," points")
        # sinon il y a égalité
        else:
            # alors afficher égalité
            print("égalité, vous avez tout les deux ",pointjoueur1," points")