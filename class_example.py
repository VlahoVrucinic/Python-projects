class Profile:
    
    def __init__(self):
        self.nickname = input('Enter a nickname: ')
        self.password = input('Enter your password: ')
        self.email = input('Enter your e-mail: ')
    
    
    def display_profile(self):
        print('Nickname: ' + self.nickname + '\npassword: ' + self.password + '\nE-mail: ' + self.email)
    

profil1 = Profile()
print('\n')
profil1.display_profile()



