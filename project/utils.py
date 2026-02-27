
# Challenge 1

def est_transaction_valide(montant):
    """
    Retourne True si le montant est un nombre positif
    """
    if isinstance(montant, (int, float)):
        return montant > 0
    return False


# Challenge 2

def nettoyer_nom(nom):
    """
    Supprime les espaces et met en minuscules
    """
    return nom.strip().lower()


# challenge 3

def ajouter_tva(prix, taux=0.2):
    """
    Ajoute la TVA au prix HT
    taux par défaut = 20%
    """
    return prix * (1 + taux)


# Challenge 4

def categorie_vente(montant):
    """
    Classe une vente selon son montant
    """
    if montant < 100:
        return "Petite"
    elif 100 <= montant <= 500:
        return "Moyenne"
    else:
        return "Grande"


# Challenge 6

def resume_liste(liste):
    """
    Retourne somme, moyenne et maximum
    """
    total = sum(liste)
    moyenne = total / len(liste)
    maximum = max(liste)

    return total, moyenne, maximum