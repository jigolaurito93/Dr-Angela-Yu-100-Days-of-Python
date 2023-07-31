#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
from guess_game_logo import logo
import random
# Print the Logo
print(logo)

# Variables

attempts = 0
answer = random.randint(1, 100)

# Welcome message
print('Welcome to the Number Guessing Game!')
# Guess number from 1 - 100
print("I'm thinking of a number between 1 and 100.")

# Print answer for now
# print(f'Pssst, the correct answer is {answer}')

# Ask for difficulty level
difficulty = input(f"Choose a difficulty. Type 'easy' or 'hard':\n")
# easy is 10 attempts, hard is 5 attempts
if difficulty == 'easy':
    attempts = 10
elif difficulty == 'hard':
    attempts = 5



while attempts > 0:
      # Print how many attempts available
      print(f"You have {attempts} attempts remaining to guess the number.")

      # Ask to make a guess
      guess = int(input(f"Make a guess: "))
      if guess == answer:
           print(f"You got it! The answer was {answer}.")
           attempts = 0
      elif guess != answer and attempts == 1:
           if guess > answer:
                attempts -= 1
                print(f"Too high.")
                print(f"You've run out of guesses, you lose.")
           elif guess < answer:
                attempts -= 1
                print(f"Too low.")
                print(f"You've run out of guesses, you lose.")
      elif guess != answer:
           if guess > answer:
                print(f"Too high.\nGuess again.")
                attempts -= 1
           elif guess < answer:
                print(f"Too low.\nGuess again.")
                attempts -= 1

                

    

# Guess again
# Show how many attempts left
# Ask to make a guess again


# If right, print YOU GOT IT, THE ANSWER WAS {answer}
# If wrong, print You've run out of guesses, you lose.