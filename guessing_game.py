print('Welcome to the guessing game')
print('Im going to guess a number between 1 and 10, can you try to guess it?')

import random
number = random.randint(1,10)
number_of_guesses = 0	

while number_of_guesses < 10:
	guess = int(input('Write your guess here: '))
	number_of_guesses += 1
	if guess < number:
		print('Your guess is too low')
	elif guess > number:
		print('Your guess is too high')
	elif guess == number:
		print('Congratulations, you guessed the number in ' + str(number_of_guesses) + ' tries')
	else:
		print('You didnt guess it, the number was' + str(number))
		break