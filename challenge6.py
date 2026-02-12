

work_hours = int(input("ENTER HOURS OF WORK: "))
hourly_rate = int(input("ENTER YOUR HOURLY RATE: "))
total_of_salary = work_hours * hourly_rate

if work_hours > 40:
 normal_work_houes = 40
 sup_hours = work_hours - 40
 salary = (normal_work_houes * work_hours) + (sup_hours * hourly_rate * 1.5)
 print("Calcul avec heures supplémentaires (majorées de 50%).")
else:
 salary = work_hours * hourly_rate
 print("Calcul au tarif normal.")
print(f"YOUR TOTAL SALARY IS: {salary}")

 