##Faire randomint et donner des "plus haut" ou "plus bas" a l'utilisateur
import random
# importer random pour un random number generator

#faire une loop pour que le jeu puisse continer meme apres qu'il finisse
jeux = True
while jeux:
    #Choisir un nombre random entre 0 et 100
    nb = random.randrange(100)
    #Commencer le nombre essai a 0
    essai = 0
    #print(nb)
    #définir le nombre d'essai a 1, pour qu'il compte le dernier essai aussi
    tries = 1
    #Demander utilisateur pour un nombre
    print("J'ai choisi un nombre au hasard entre 0 et 100, a vous de deviner lequel")
    #la loop s'arretera quand l'utilisateur aura le bon nombre
    while essai != nb:
        essai= int(input("Votre essai:"))


        ##Savoir si le nombre est au dessus ou en dessous du nombre randomly generated
        if essai > nb:
            print("Le nombre est plus petit! Votre essai: ", essai)
            tries += 1
        if essai < nb:
            print("Le nombre est plus grand! Votre essai: ", essai)
            tries += 1
    print("Tu as trouvé le nombre en ", tries, " essais, bravo!")
    print("Voulez-vous recommencer?")
    restart = input(" o/n :")
    restart = restart.strip()
    if restart == "o":
        print("Recommencons!")
        #la loop va recommencer
    if restart == "n":
        print("Merci et au revoir!")
        #rendre la variable jeux a false pour que le jeux ne recommence pas
        jeux = False
