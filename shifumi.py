from random import randint





def jouer():

    score_j = 0

    score_pc = 0

    while score_j < 3 and score_pc < 3:

        coup_j = input("choisi ton coup entre pierre, feuille et ciseaux:")

        if coup_j == "pierre" or coup_j == "feuille" or coup_j == "ciseaux":

            coup_pc = randint(1,3)

            if coup_pc == 1:

                coup_pc = "pierre"

            if coup_pc == 2:

                coup_pc = "feuille"

            if coup_pc == 3:

                coup_pc = "ciseaux"

            print(coup_pc)

            

            #la on gère les égalités

            if (coup_j =="pierre" and coup_pc == "pierre") or (coup_j =="ciseaux" and coup_pc == "ciseaux") or (coup_j =="feuille" and coup_pc == "feuille"):

                print("égalité")

            

            #on gère quand le joueur gagne sinon c'est le pc qui gagne en augmentant les scores 

            else:

                if (coup_j =="pierre" and coup_pc == "ciseaux") or (coup_j =="ciseaux" and coup_pc == "feuille") or (coup_j =="feuille" and coup_pc == "pierre"):

                    print("joueur à gagner")

                    score_j += 1 

                else:

                    print("pc à gagner")

                    score_pc += 1

        else:

            print("Mauvais coup")

    

    print("Partie terminé")

    print("Score joueur:",score_j)

    print("Score pc:",score_pc)



    

jouer()