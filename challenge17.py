'''
username = input("Enter your username: ")
username.find(" ")


if len(username) > 12:
    print("Your username can't be more than 12 characters!!")
elif not username == -1:
    print("Your username can't contain spaces!")
elif not username.isalpha:
    print("Your username can't contain digits!")
else:
    print(f"WELCOME! {username}")

    '''
numbers = [1, 2, 2, 3, 3, 3]
output = list(set(numbers))
print(output)        

