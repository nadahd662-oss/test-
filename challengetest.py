
#CHALLENGE 1



'''
age = 80
student = False
is_off_peak = True

# 1. Entry Check (The Gatekeeper)
if age < 16:
    print("Sorry! you are under 16. you can't join.")
else: 
    # 2. Start the pricing chain inside the 'else'
    if age >= 75: 
        price = 0
        print("Welcome! you can join for free.")
    
    # Use 'elif' so it only checks this if the person is NOT 75+
    elif (age >= 16 and age <= 19) or student:
        price = 30.00
    
    # The final 'else' for standard adults
    else:
        price = 50.00

    # 3. Stackable Discount (Outside the age chain, but still inside the age 16+ check)
    if is_off_peak and price > 0:
        price -= 10
        
    print(f"Your monthly total is: ${price}")
    '''
#CHALLENGE 2
final_bill = 0
cart_prices = [25, 120, 50, 200, 10]

for p in cart_prices:
    if p > 100:
        discount = p - 20
        final_bill = final_bill + discount
        print("Luxury item detected, Discount applied!")
    else:
         final_bill = final_bill + p   
print(f"you are one of our great customers! your bill is: ${final_bill}") 

