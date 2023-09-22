##Faire randomint et donner des "plus haut" ou "plus bas" a l'utilisateur
import random
# importer random pour un random number generator

#faire une loop pour que le jeu puisse continer meme apres qu'il finisse
for i in range(300):
    #Choisir un nombre random entre 0 et 100
    nb = random.randrange(100)
    #Commencer le nombre d'essai a 0
    tries = 0
    print(nb)
    essai = 0
    #Demander utilisateur pour un nombre
    print("J'ai choisi un nombre au hasard entre 0 et 100, a vous de deviner lequel")
    while essai != nb:
        essai= int(input("Votre essai:"))


        ##Savoir si le nombre est au dessus ou en dessous du nombre randomly generated
        if essai > nb:
            print("Ton essai est plus grand! il etait: ", essai)
            tries += 1
        if essai < nb:
            print("Ton essai est plus petit! il etait: ", essai)
            tries += 1
    print("Tu as trouvé le nombre!")
    print("Voulez-vous recommencer?")
    restart = input(" o/n :")

    if restart == "n":
        print("YELLOW")
    else:
        print("BLUEWo")