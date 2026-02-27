from utils import *

# Challenge 1
transactions = [120, -30, 250, None, 80, -5, 300]
transactions_valides = list(filter(est_transaction_valide, transactions))
print("Transactions valides:", transactions_valides)

# Challenge 2
clients = [" ali ", "SARA", "Omar ", " sara"]
clients_propres = list(map(nettoyer_nom, clients))
clients_uniques = list(set(clients_propres))
print("Clients propres:", clients_uniques)

# Challenge 3
prix_ht = [100, 250, 80]
prix_ttc = list(map(ajouter_tva, prix_ht))
print("Prix TTC:", prix_ttc)

# Challenge 4
ventes = [50, 120, 700]
categories = list(map(categorie_vente, ventes))
print("Catégories:", categories)

# Challenge 6
total, moyenne, maximum = resume_liste(ventes)
print("Résumé:", total, moyenne, maximum)