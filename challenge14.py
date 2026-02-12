email = "nada@email.com"
email = input("Enter an email: ")
if "@" in email and ".com" in email:
    print ("Your email is valid!")
else:
    print("Your email must contain a '@' and '.com'!")