from sys import argv
from random import randint

randomLow = 1
randomHigh = 10
if (len(argv) > 1):
	randomLow = argv[1]
	randomHigh = argv[2]
guessesMade = 0

def getInput(randomLow, randomHigh):
	'''Get input from user'''
	random = ""
	try:
		randomLow = int(min(abs(randomLow), abs(randomHigh)))
		randomHigh = int(max(abs(randomLow), abs(randomHigh)))
		return randint(int(randomLow), int(randomHigh))
	except Exception as e:
		return e


def promptGuess():
	'''Check answer against random number'''
	guess = input(f"Please enter a number between {randomLow} and {randomHigh}\n")
	try:
		guess = int(guess)
		return guess
	except Exception as e:
		return e


def runGame(randomNum):
	global guessesMade
	if (isinstance(randomNum, int)):
		while True:
			guess = promptGuess()
			if (isinstance(guess, int)):
				if (guess < randomLow or guess > randomHigh):
					print(f"Please enter a valid number")
				else:
					guessesMade += 1
					if (guess == randomNum):
						print(f"After {guessesMade} attempts you guessed correctly \nThe answer is {randomNum}")
						break
					else:
						print(f"You guessed incorrectly")
			else:
				print(f"Please enter a valid guess")
	else:
		print(f"Please enter a valid min and max number to start the program")


randomNum = getInput(randomLow, randomHigh)
runGame(randomNum)
