"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces.

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random


def start_game():

    """Psuedo-code Hints

   When the program starts, we want to:
   ------------------------------------
   1. Display an intro/welcome message to the player.
   2. Store a random number as the answer/solution.
   3. Continuously prompt the player for a guess.
     a. If the guess greater than the solution, display to the player "It's lower".
     b. If the guess is less than the solution, display to the player "It's higher".

   4. Once the guess is correct, stop looping, inform the user they "Got it"
        and show how many attempts it took them to get the correct number.
   5. Let the player know the game is ending, or something that indicates the game is over.

   ( You can add more features/enhancements if you'd like to. )
   """
# write your code inside this function.

number = 0
guess_number = 0
count_number_of_tries = 0
name = input("Hi, What's your name? ")
print("Ok!" + name + "Welcome to Guessing Game.!")
guess = input("Okay, I have picked a random number between 1-10. What's your guess? ")
number = random.randint(1, 10)
count_number_of_tries = 1
while guess != number:
    try:
        guess = int(input("Enter any number from 1 to 10: "))
        print("Guess the number Between 1 and 10: ")

    except ValueError:
        print("Must be number")
        guess = input("That is not a valid number. Please input a number between 1-10. ")
    if count_number_of_tries == 4:
        continue
    elif number not in range(1,10):
        print("The number is outside the range of numbers. Guess number between 1 and 10: ")
    elif guess_number < number:
        print("It's too lower")
    else:
        print("It's too Higher")
        guess = int(input("Guess the number between 1-10"))
        count_number_of_tries += 1
    if number == guess:
        print("Good job!," + name + "! You got it right!")
        print("it's took you" + str(count_number_of_tries) + "tries!")
    else:
        print("Sorry! You did not make it.")
        print("The number you needed to guess was", number)
        print("Game Over")

        break

start_game()


