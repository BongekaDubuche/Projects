import random


def start_game():

 def start_game():
    number = 0
    guess = 0
    tries = 0


number = random.randint(1, 10)


name = input("Hi, What's your name? ")
print("Ok!" + name + "Welcome to Guessing Game.!")

guess = input("Okay, I have picked a random number between 1-10. What's your guess? ")
number = random.randint(1,10)
try:
    int(guess)
except ValueError:
    guess = input("That is not a valid number. Please input a number between 1-10. ")
guess = 1
while guess != number:
    if guess <= 0 or guess >= 10:
        print("Please only guess a number between 1-10")
        guess = int(input("Guess the number between 1-10"))
    elif guess < number:
        print("It's too lower")
        guess = int(input("Guess the number between 1-10"))
    elif guess > number:
        print("It's too Higher")
        guess = int(input("Guess the number between 1-10"))
    else:
        break
    if guess == number:
        print("Good job!," + name + "! You got it right!")
        print("Your guessed the number in ," + str(guess) + "tries!")
        print("Game Over!!")

        break

start_game()

