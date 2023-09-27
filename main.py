##Faire randomint et donner des "plus haut" ou "plus bas" a l'utilisateur
# importer random pour un random number generator
import random


#faire une loop pour que le jeu puisse continer meme apres qu'il finisse
jeux = True
#Loop du jeu
while jeux:
    #Choisir un nombre random entre 0 et 100
    nb = random.randrange(100)
    essai = 0
    tries = 1
    print("J'ai choisi un nombre au hasard entre 0 et 100, a vous de deviner lequel")
    #Loop de essai jusqua bon nombre
    while essai != nb:
        essai= int(input("Votre essai:"))
        #Si le nombre randomly generated est plus grand
        if essai > nb:
            print("Le nombre est plus petit! Votre essai: ", essai)
            tries += 1
        #Si le nombre randomly gnerated est plus petit
        if essai < nb:
            print("Le nombre est plus grand! Votre essai: ", essai)
            tries += 1
    print("Tu as trouvé le nombre en ", tries, " essais, bravo!")
    print("Voulez-vous recommencer?")
    restart = input(" o/n :")
    restart = restart.strip()
    if restart == "o":
        print("Recommencons!")
    if restart == "n":
        print("Merci et au revoir!")
        #rendre la variable jeux a false pour que le jeux ne recommence pas
        jeux = False
