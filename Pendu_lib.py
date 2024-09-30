#Jeu du Pendu
#9/23/24
#Léonard Rivaux
#ToDo:

import random as rd


def lire_dico(name):
    data = open(name).read() 

    l_dico = list(data.split())
    return l_dico



def lancement_partie():
    pendu(0)



def pendu(meilleurscore):
    listemots = lire_dico("dico.txt")
    motrandom = listemots[rd.randint(0,len(listemots))]
    print(motrandom)
    motsplit = list(motrandom)
    for lettre in motsplit:
        lettres_trouvées = ["_" if str(lettre) != motsplit[0] else motsplit[0] for lettre in motsplit]
    essais = 0
    lettresessayées = []


    while (essais != 8) and (motsplit) != (lettres_trouvées):
        
        Message = "lettres trouvées:",str(lettres_trouvées),"Choisissez une lettre à ajouter.Lettres déja essayées:",lettresessayées,"essais restants:",8-essais
        demandelettre= input(Message)
        if demandelettre not in lettresessayées:
            lettresessayées.append(demandelettre)
            lettres_trouvées = ajouterlettre(motsplit,lettres_trouvées,demandelettre)
            essais+=1
        else:
            print("lettre déjà demandée auparavant.")

    if essais ==8 and motsplit != lettres_trouvées:
        print("Dommage vous avez perdu ! Le mot était:",motrandom)
    else:
        if meilleurscore>essais or meilleurscore==0:
            meilleurscore = essais 
        print("Bravo vous avez trouvé le mot",motrandom,"en",essais,"essais !" 'Votre meilleur score actuel est', meilleurscore,"essais")
    a = input("Voulez vous rejouer ? (yes / no)")
    if a == "yes" :
        pendu(meilleurscore)
    else:
        print("le meilleur score de votre session est",meilleurscore,"essais")
        return False


def ajouterlettre(mot,lettres_trouvées,lettredonnée):
    if isinstance(lettredonnée,str)==True:
        for i in range (len(mot)):
            if mot[i] == lettredonnée:
                lettres_trouvées[i] = lettredonnée
        return lettres_trouvées
    return False       