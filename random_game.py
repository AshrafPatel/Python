from sys import argv
from random import randint

randomLow = argv[1]
randomHigh = argv[2]
guessesMade = 0;

try:
	randomNum = randint(int(randomLow), int(randomHigh))
except Exception:
	print("Program failed to start number given was not recognised")


while True:
	try:
		guess = int(input(f"Please enter a number between {randomLow} and {randomHigh}\n"))
	except Exception:
		print("Please check your number and try again!")
	else:
		guessesMade += 1
		if (guess == randomNum):
			break

print(f"Congratulations you guessed correctly after {guessesMade} attempts")
print(f"The number was {randomNum}")