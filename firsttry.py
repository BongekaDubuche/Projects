import random


username = input("Hi, What should we call you? ")
print("Ok!," + username+" welcome to  Guessing Game!")

def start_game():



  number_to_guess = random.randrange(1, 10)


  guess = input("Okay, I have picked a random number between 1 and 10. What's your guess? ")
  try:
    int(guess)
  except ValueError:
        guess = input("That is not a valid number. Please input a number between 1-10. ")
        guess = 1

  while int(guess) != number_to_guess:
        guess += 1
  if int(guess) < number_to_guess:
        print("it's lower")
  else:
        print("it's higher")
        guess = input("Your guess was {lower_or_higher} than the secret number. Guess again: ")
        try:
            int(guess)
        except ValueError:
         guess = input("{guess} isn't a valid entry. Please input a number between 1-10.")
  else:
        print("Good job!," + username + "! You got it right!")
        print("Your guessed the number in ," + str(guess) + "tries!")
        print("Game Over!!")


  start_game():
