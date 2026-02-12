
'''
phrase = input("Enter a phrase: ")
words = phrase.lower().split()
frequences = {}
for word in words: 
    frequences [word] += 1
else:
    frequences[word] = 1
for word, count in frequences.items():
    print(f"'{word}' appeared {count} fois")
    '''



phrase = "le chat mange la souris et le chat boit du lait"

# 1. Nettoyage et découpage : on transforme la phrase en liste de mots
mots = phrase.lower().split()

# 2. Création du dictionnaire de fréquences
frequences = {}

for mot in mots:
    if mot in frequences:
        frequences[mot] += 1  # Si le mot existe déjà, on ajoute 1
    else:
        frequences[mot] = 1   # Sinon, on l'initialise à 1

# 3. Affichage des résultats
for mot, compte in frequences.items():
    print(f"'{mot}' apparaît {compte} fois")