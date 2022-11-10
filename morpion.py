tab = [['#','#','#'],
        ['#','#','#'],
        ['#','#','#']]


def ester_egg():
    if tab[0][2] == "O" and tab[1][1] == "O" and tab[2][0] == "O" and tab[1][2] == "X" and tab[2][2] == "X":
        print("Succés dévérouiller")
        print(" FISHING ROAD ")
        print("Vous avez craft votre première canne à pêche")
    if tab[1][1] == "O" and tab[2][1] == "O" and tab[0][0] == "X" and tab[0][1] == "X" and tab[0][2] == "X":
        print("Succés dévérouiller")
        print(" MINING ")
        print("Vous avez craft votre première pioche")
    if tab[1][1] == "O" and tab[2][1] == "O" and tab[0][1] == "X":
        print("Succés dévérouiller")
        print(" LIGHTING ")
        print("Vous avez craft votre première torche")

def affiche_tab():
    print(" ", 1, 2, 3)
    for i in range(0,len(tab)):
        print(i+1,tab[i][0],tab[i][1],tab[i][2])

print("Choix des noms de joueurs, le joueur X jouera en premier")
j_o = input("qui va jouer les O? : ")
j_x = input("qui va jouer les X? : ")

def jeu():
    fini = True
    affiche_tab()
    
    nbr_coup = 0
    while fini:
        if nbr_coup < 9:
            #tour du joueur X
            print(j_x," à votre tour")
            
            fin_x = True
            while fin_x:
                ligne = int(input("Quelle ligne ?: ")) -1
                colonne = int(input("Quelle Colonne ?: ")) -1
                if 0 <= ligne <= 2 and 0 <= colonne <= 2:
                    if tab[ligne][colonne] == "X" or tab[ligne][colonne] == "O":
                        affiche_tab()
                        print("case déjà jouer")
                    else:
                        tab[ligne][colonne] = "X"
                        affiche_tab()
                        nbr_coup += 1
                        ester_egg()
                        if verif():
                            fini = False
                        fin_x = False
                else:
                    print("Mauvaise coordonnées, ressayer ")
    
    
            if fini == True and nbr_coup < 9:
                #tour du joueur O
                print(j_o," à votre tour")
                fin_o = True
                while fin_o:
                    ligne = int(input("Quelle ligne ?: ")) -1
                    colonne = int(input("Quelle Colonne ?: ")) -1
                    if 0 <= ligne <= 2 and 0 <= colonne <= 2:
                        if tab[ligne][colonne] == "X" or tab[ligne][colonne] == "O":
                            affiche_tab()
                            print("case déjà jouer")
                        else:
                            tab[ligne][colonne] = "O"
                            affiche_tab()
                            nbr_coup += 1
                            ester_egg()
                            if verif():
                                fini = False
                            fin_o = False
                    else:
                        print("Mauvaise coordonnées, ressayer ")
        
        else:
            fini = False
            
    print("partie terminé")

def verif():
    for i in range(0, len(tab)):
        if tab[i][0] == "X" and tab[i][1] == "X" and tab[i][2] == "X" or tab[0][i] == "X" and tab[1][i] == "X" and tab[2][i] == "X":
            print("le joueur X", j_x," à gagner")
            affiche_tab()
            return True
        elif tab[i][0] == "O" and tab[i][1] == "O" and tab[i][2] == "O" or tab[0][i] == "O" and tab[1][i] == "O" and tab[2][i] == "O":
            print("le joueur O", j_o," à gagner")
            affiche_tab()
            return True
    if tab[0][0] == "X" and tab[1][1] == "X" and tab[2][2] == "X" or tab[0][2] == "X" and tab[1][1] == "X" and tab[2][0] == "X":
        print("le joueur X", j_x," à gagner")
        affiche_tab()
        return True
    if tab[0][0] == "O" and tab[1][1] == "O" and tab[2][2] == "O" or tab[0][2] == "O" and tab[1][1] == "O" and tab[2][0] == "O":   
        print("le joueur O", j_o," à gagner")
        affiche_tab()
        return True


jeu()
