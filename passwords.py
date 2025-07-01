import string
import random

# Demande la taille du mot de passe
length = int(input("Taille du mot de passe : "))

# Affiche les options
print('''Sélectionnez les types de caractères pour votre mot de passe :
    1. Chiffres
    2. Lettres
    3. Caractères spéciaux
    4. Stop ''')

# Liste vide pour stocker les types de caractères sélectionnés
characterList = ""

# Boucle permettant à l'utilisateur de personnaliser son mot de passe
while True:
    choice = int(input("Choisissez un numéro (1-4) : "))
    
    if choice == 1:
        characterList += string.digits
    elif choice == 2:
        characterList += string.ascii_letters
    elif choice == 3:
        characterList += string.punctuation
    elif choice == 4:
        if characterList == "":
            print("Veuillez sélectionner au moins un type de caractère.")
        else:
            break
    else:
        print("Option invalide. Veuillez choisir entre 1 et 4.")

# Génère le mot de passe
password = ''.join(random.choice(characterList) for _ in range(length))

# Affiche le mot de passe
print("Votre mot de passe généré est :", password)
