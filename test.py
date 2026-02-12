
'''
       # Fixed the spelling here
secret = "python123" 
i=True
while i:
    guess = input("Enter your password: ")
    
    # Now this 'secret' matches the one at the top!
    if guess == secret:
        print("Access Granted")
        break
    else:
        print("Wrong! try again!")
    
        '''

secret = "python123" 

while True:
    guess = input("Enter your password: ")
    
    # Now this 'secret' matches the one at the top!
    if guess == secret:
        print("Access Granted")
        break
    else:
        print("Wrong! try again!")    
        
       