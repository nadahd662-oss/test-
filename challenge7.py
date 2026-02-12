

nombre = -1

while nombre <= 0:
    nombre = float(input("Entrer un nombre strictement positif : "))
    
    if nombre <= 0:
        print("Erreur : Le nombre doit être plus grand que 0. Réessaie !")

print(f"le nombre valide : {nombre}")