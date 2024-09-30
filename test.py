import tkinter as tk
import Pendu_lib as pdl

# Mot à deviner
mot_a_deviner = "TORTUE"
lettres_trouvees = ["_" if lettre != "T" else "T" for lettre in mot_a_deviner]

# Fonction pour proposer une lettre
def proposer_lettre(lettre, bouton):
    print(f"Lettre cliquée : {lettre}")
    lettres_trouvees.append(lettre)
    label_mot.config(text=" ".join(lettres_trouvees))
 

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Jeu du Pendu")

# Affichage du mot à deviner
label_mot = tk.Label(fenetre, text=" ".join(lettres_trouvees), font=("Arial", 24))
label_mot.grid(row=0, column=0, columnspan=13, pady=20)


# Création des boutons pour les lettres de l'alphabet
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
boutons = {}

for i, lettre in enumerate(alphabet):
    bouton = tk.Button(fenetre, text=lettre, font=("Arial", 14), width=5,
                       command=lambda l=lettre, b=boutons: proposer_lettre(l, b))
    boutons[lettre] = bouton
    bouton.grid(row=1 + i // 13, column=i % 13, padx=5, pady=5)

bouton_exit = tk.Button(fenetre, text="Exit", font=("Arial", 14), width=6, command=fenetre.quit)
bouton_exit.grid(row=3, column=12, padx=5, pady=5, columnspan=2)  # Placement en bas à droite

# Démarrage de la boucle principale de Tkinter
fenetre.mainloop()

