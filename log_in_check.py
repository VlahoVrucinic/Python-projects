while True:
    count = 0
    nickname = input('Enter a nickname: ')
    password = input('Enter a password: ')
    count += 1
    
    if count == 3:
        print('Invalid info')
        break
    
    if nickname == 'Vlaho22' and password == 'mojpass':
        print('You succesfully logged in')
        break
    else:
        print('Wrong nickname and password')