import secrets
import string

def password_generator():
    while True:
        characters = string.ascii_letters +  string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

        password_range = int(input('Enter the range of the password: '))
        if password_range < 8:
            print('Password too short, try again')
            continue
        password = ''

        for num in range(password_range):
            password = ''.join(secrets.choice(characters))
            print(password, end='')
        
        again = input('Do you want to go again? type yes to go again: ')
        if again == 'yes':
            continue
        else:
            break
