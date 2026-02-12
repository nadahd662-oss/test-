voyelles = ["a", "e", "i", "o", "u"]
name = "Data Engineering"
compteur = 0
name = input("Enter a name: ")

for v in name:
   if v in voyelles:
      compteur += 1
print(f" Nombre of voyelles: {compteur} ")
