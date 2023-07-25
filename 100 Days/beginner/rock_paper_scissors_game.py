import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

# Greeting
print('Welcome to the ROCK, PAPER or SCISSORS game! ')
# Ask user what their move is

user_move = input(f"To begin, choose between 'rock', 'paper' or 'scissors' \n > ").lower()

# Use random choice to get computer's random move is

choices = ['rock', 'paper', 'scissors']
computer_choice = random.choice(choices)

# Use if statements to compare both moves

# ================ DRAW =================
if user_move == 'rock' and computer_choice == 'rock':
    print(f"Computer: {rock} \n You: {rock} \n It's a draw!")

elif user_move == 'paper' and computer_choice == 'paper':
    print(f"Computer: {paper} \n You: {paper} \n It's a draw!")

elif user_move == 'scissors' and computer_choice == 'scissors':
    print(f"Computer: {scissors} \n You: {scissors} \n It's a draw!")

# ================ END OF DRAW =================

# ================ USER LOSE =================
elif user_move == 'rock' and computer_choice == 'paper':
    print(f"Computer: {rock} \n You: {scissors} \n You lose!")

elif user_move == 'rock' and computer_choice == 'paper':
    print(f"Computer: {paper} \n You: {rock} \n You lose!")

elif user_move == 'rock' and computer_choice == 'paper':
    print(f"Computer: {scissors} \n You: {paper} \n You lose!")

# ================ END OF USER LOSE =================

# ================ USER WIN =================
elif user_move == 'rock' and computer_choice == 'scissors':
    print(f"Computer: {scissors} \n You: {paper} \n You win!")

elif user_move == 'paper' and computer_choice == 'rock':
    print(f"Computer: {rock} \n You: {paper} \n You win!")

elif user_move == 'scissors' and computer_choice == 'paper':
    print(f"Computer: {paper} \n You: {scissors} \n You win!")

else:
    print(f"Input invalid move")