# Faire randomint et donner des "plus haut" ou "plus bas" a l'utilisateur
# importer random pour un random number generator
import random


# faire une loop pour que le jeu puisse continer meme apres qu'il finisse
jeux = True

# Fonction qui retourne le premier et le dernier nombre de la borne


def choix():
    global a, b
    a = int(input("Choissisez le premier nombre: "))
    b = int(input("Choissisez le deuxieme nombre: "))
    return a, b


# Loop du jeu
while jeux:
    global a, b, nb
    print("Voulez vous garder les bornes (0,100) ou les changer?")
    change = input("G pour les garder C pour les changer: ")
    change = change.strip()
    if change == "g":
        print("Elles ne vont pas changer: (0,100)")
        nb = random.randint(0, 100)
        print("J'ai choisi un nombre au hasard entre 0 et 100, a vous de deviner lequel")
    elif change == "c":
        choix()
        # Si l'utilisateur fait une erreur et inverse les nombres
        if a > b:
            print("Vous avez inversé les bornes! Je pense donc que vous vouliez dire que nombre sera entre ", b, " et ",
                  a)
            nb = random.randint(b, a)
        # Si tout va bien
        else:
            print("Votre nombre sera entre ", a, " et ", b)
            nb = random.randint(a, b)
    essai = 0
    tries = 1

    # Loop de essai jusqua bon nombre
    while essai != nb:
        essai = int(input("Votre essai:"))
        # Si le nombre randomly generated est plus grand
        if essai > nb:
            print("Le nombre est plus petit! Votre essai: ", essai)
            tries += 1
        # Si le nombre randomly gnerated est plus petit
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
        # Rendre la variable jeux a false pour que le jeux ne recommence pas
        jeux = False
