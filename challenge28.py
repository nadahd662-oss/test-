import numpy as np
salaries = np.array([2000, 2100, 2200, 5000])
mediane = np.median(salaries)
ecart_type = np.std(salaries).round(1)

print(f"Mediane: {mediane}")
print(f"Ecart-type: {ecart_type}")