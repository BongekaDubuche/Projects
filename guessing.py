import random


def start_game():

    number = random.randint(1, 10)


name = input("Hi, What's your name? ")
print("Ok!" + name + "Welcome to Guessing Game.!")

number = input("Okay, I have picked a random number between 1 and 10. What's your guess? ")
try:
    int(number)
except ValueError:
    guess = input("That is not a valid number. Please input a number between 1-10. ")
    tries = 1
    guessing = 1
    number = 0

while number != guess:
    if guess < number:
        print("it's lower")
        guess = input("Guess again!")
    if guess > number:
        print("it's higher")
        guess = input("Guess again! ")
        tries = tries + 1

        try:
            int(guess)
        except ValueError:
            guess = input("{guess} isn't a valid entry. Please input a number between 1-10.")
    elif guess == number:
        print("Good job!," + name + "! You got it right!")
        print("Your guessed the number in: ," + str(guess) + "tries!")
        print("Game Over!!")

        break

    start_game()
