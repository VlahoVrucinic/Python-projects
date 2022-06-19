import random
import string

def password_generator():
	# postavi listu koja sadrzi abecedu, brojeve od 1 do 9 i znakove
	characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
	# u prazni string ce se unositi znakovi iz characters liste
	password = ''
	# pitam usera koliko dugacak password zeli
	length_of_pass = int(input('How long do you want the password to be?'))
	# prolazi kroz duzinu passworda(broj koji dam), i nasumicno dodaje znakove iz characters liste
	for x in range(length_of_pass):
		password_char = random.choice(characters)
		password = password + password_char

		
	print(password)
