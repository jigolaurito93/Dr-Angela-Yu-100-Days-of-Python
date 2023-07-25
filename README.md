# Dr-Angela-Yu-100-Days-of-Python

Reeborg's World [Game] (Hurdle 3)
https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json
  - Created a function that assigns a specific movement for the robot
  - Nested a while loop with if statements
    ex. (Click the url and use this code I created for the game)

def dead_end():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    if not wall_in_front():
        move()
    elif wall_in_front():
        dead_end()
        
  - While the robot is not at the goal, the program will keep running

FizzBuzz Game
  - I wrote a program that automatically prints the solution to the FizzBuzz game
  - I created a for loop with the range() function
  - The range had to include the numbers from 1 to 100
  - I created an if statement with certain conditions
  - I used the modulo operator to check if the numbers are divisible by 5 or 3 or both 5 and 3

Password Generator Program
  - I created a password generating program by getting the number of characters for each character type
  - Used the input prompt to ask the user how many letters, numbers and symbols to use for the password
  - Created an empty list to hold all the randmon characters
  - Created a for loop with a range function to generate random characters
  - Used random.choice() method to generate random characters
  - Appended that random number to the empty list which is the total_characters
  - Got the length of total characters and created an empty string variable
  - Created a for loop with the range function using the length of total characters as an argument
  - Got the random character in the total_characters list. Remove it from the list using remove() method and add it to the password string using arithmetic operations
  - Print your newly generated password

Rock Paper Scissors Game
  - I used random module with random.choice() function to get random move from computer
  - I used input prompt to get user's answer
  - If statements for conditions

Get Average Height
  - (NOT ALLOWED TO USE len() and sum() function for this project)
  - Used input prompt to get the value of heights of every student
  - Used the split() method to convert it to a list
  - Set up a counter variable to 0
  - Set up sum of height variable to 0
  - Created a for loop for each height in the list
  - Used arithmetic operations += to add height of every student in the loop
  - Used arithmetic operation to  increment counter for every student
  - Divided the sum of heights to the number of students and rounding it off to the nearest whole number

Highest Score
  - I have to write a program that calculates the highest score from a list
  - I'm not allowed to use max() or min() function
  - I used the input prompt to get the value of the numbers
  - I used the split() method to convert the string to a list
  - Set up a variable named "highest score" with a zero value temporarily
  - Set up a for loop to run each score
  - Used comparison operator for each score and if the score is greater than the current value, that will replace the current highest score
  - print the highest score variable

Adding Even Numbers
  - I wrote a program that calculates the sum of all the even numbers from 1 to 100. Thus, the first even number would be 2 and the last one is 100
  - Created a variable called sum_of_even_numbers and put 0 as its initial value
  - Created a for loop with the range function
  - Created an if statement that checks if the number is an even number
  - Using the modulo operator, I divided the number to 2, if the result is 0, that means the number is even
  - Printed sum_of_even_numbers


