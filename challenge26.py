import numpy as np

sold = np.array([12, 18, 9, 25, 14, 20, 11])

sold_max = sold.max()
sold_min = sold.min()
average_sold = sold.mean().round(1)

print(f"maximale sold is: {sold_max} headphone per day.")
print(f"minimale sold is: {sold_min} headphone.")
print(f"average sold is: {average_sold} headphone.")

