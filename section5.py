# Guessing game in python
import random

print('Hello, what is your name?')
name = input()
secretNumber = random.randint(1, 20)
print(name +', I\'m thinking of a number between 1 and 20. What is it?')

#Ask player to guess 6 times
for guessTaken in range(1,7):
    print('Take a guess')
    guess = int(input())
    if guess < secretNumber:
        print('Too low, perro')
        print('Guess #' + str(guessTaken))
    elif guess > secretNumber:
        print('Too high amigo')
        print('Guess #' + str(guessTaken))
    else:
        print('You guessed right')
        break 

if guess == secretNumber:
    print('Good job ' + name + ', you guessed right')
else:
    print('Wrong! The secret number was ' + str(secretNumber))