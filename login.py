# List of approved users
creds = [
    ['Hamish', '122']
]

user = input('Enter your username \n')

def checkCreds():
    for x in range(len(creds)):
        if (user == creds[x][0]):
            pwd = input('Enter your password \n')

            if (pwd == creds[x][1]):
               return True

if (checkCreds()):
    print("Login Successful")
else:
    print('Login Unsuccessful')
