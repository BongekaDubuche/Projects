import random


name = input("Hi, What's your name? ")
print("Ok!" + name + "Welcome to Guessing Game.!")
guess = input("Okay, I have picked a random number between 1-10. What's your guess? ")
try:
    int(guess)
except ValueError:
    guess = input("That is not a valid number. Please input a number between 1-10. ")

    number = 0
guess_number = 0
count_number_of_tries = 0


def start_game():

 number = random.randint(1, 10)


count_number_of_tries = 1
number = int(input('Please guess a number between 1 and 10: '))
while guess != number:
    print("Try again! ")
    if count_number_of_tries == 4:
        break
    elif guess_number < number:
        print("It's too lower")
    else:
        print("It's too Higher")
        guess = int(input("Guess the number between 1-10"))
        count_number_of_tries += 1

    if number == guess:
        print("Good job!," + name + "! You got it right!")
        print("You took" + str(count_number_of_tries) + "tries!")
    else:
        print("Sorry! You did not make it.")
        print("The number you needed to guess was", number)
        print("Game Over")

        break

start_game()

