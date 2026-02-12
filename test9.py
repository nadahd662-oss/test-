
#THE BEAST WHILE


'''''
attempts = 2

while  attempts < 3:
    guess = input("Enter password: ")
    
    if guess == "python123":
        print("Access Granted")
        break
    else:
        attempts = attempts + 1
        print("Wrong! try again!")
if attempts == 3:
    print("Looked out! too many tries.")

'''
'''
#PRACTICE FOR 1
names = ["alice", "bob", "eve"]
for N in names:
    print(N.upper())
    '''

#PRACTICE FOR 2
scores = [ 50, 85, 99, 19, 100]
grand_total = 0
for nbr in scores:
    grand_total = grand_total + nbr
    print(f"YOUR SCORE NOW IS: { grand_total + nbr}")
   
print(f" the final score is: {grand_total}")





       
       
       