import random


username = input("Hi, What's your name? ")
print("Ok!" + username + "Welcome to Guessing Game.!")

def start_game():


 number = random.randrange(1, 10)


guess = input("Okay, I have picked a random number between 1 and 10. What's your guess? ")
try:
    int(guess)
except 'ValueError':
    guess = input("That is not a valid number. Please input a number between 1-10. ")
    #guess = 1

while guess != 'number_of_guess':
    if guess < 'number':
        print("it's lower")
        guess = input("Guess again!")
    if guess > 'number':
        print("it's higher")
        guess = input("Guess again! ")

        try:
            int(guess)
        except ValueError:
            guess = input("{guess} isn't a valid entry. Please input a number between 1-10.")
    else:
         print("Good job!," + username + "! You got it right!")
         print("Your guessed the number in ," + str(guess) + "tries!")
         print("Game Over!!")
         break

    start_game()
