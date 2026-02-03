# username contain less than 12 characters
# username not contain any spaces
# username not contain any digits

username = input("Enter a username: ")

if len(username) > 12:
    print("your user can't more than 12 Characters")
elif not username.find(" ") == -1:
     print("Your can't contain spaces")
elif not username. isalpha():
    print(" Your can't contain numbers")
else:
    print("welcome")
