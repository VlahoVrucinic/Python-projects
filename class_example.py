	class Profil:

    profil_counter = 0

    def __init__(self):
        self.nickname = input('Enter a nickname: ')
        self.password = input('Enter your password: ')
        self.email = input('Enter your e-mail: ')
    
    
    def display_profil(self):
        print('Nickname: ' + self.nickname + '\npassword: ' + self.password + '\nE-mail: ' + self.email)
    

profil1 = Profil()
profil2 = Profil()
profil1.display_profil()




