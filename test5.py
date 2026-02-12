# CHALLENGE NUMBER 1
age = 19
Day_of_week = "WEDNESDAY"
is_rated_r = True
has_parent = False

#CHECK FOR INTERY FIRST: 

if age < 17 and is_rated_r and not has_parent:
 print("Sorry, you can't enter! you need a parent.")
else: 
 
#PRICE 
 if age < 13:
    price = 8.00

 elif age <= 64 :
    price = 12.00

 else:
    price = 10.00

#THE WEDNESDAY DISCOUNT: 
 if  Day_of_week == "WEDNESDAY": 
   price = price - 2
   print(f" Wednesday Discount Applied !")
   print(f"Your ticket price is {price}.")
   


