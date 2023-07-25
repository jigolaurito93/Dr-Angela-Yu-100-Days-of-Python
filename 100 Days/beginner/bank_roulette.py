# Import the random module here
# Instructions
# You are going to write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.

# Important: You are not allowed to use the choice() function.

# Line 8 splits the string names_string into individual names and puts them inside a List called names. For this to work, you must enter all the names as names followed by comma then space. e.g. name, name, name

import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# get the lenght of the list of names
# use the random module and input the length number as an argument in the random function
# use if statements to get the names in the list


list_length = len(names)

random_number = random.randint(0, list_length-1)

person_paying = names[random_number]

print(f"{person_paying.capitalize()} is going to buy the meal today!")

