#Jeu du Pendu
#9/23/24
#Léonard Rivaux
#ToDo:

import random as rd
import tkinter as tk

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
    print('a')