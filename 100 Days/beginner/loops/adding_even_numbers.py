# Instructions
# You are going to write a program that calculates the sum of all the even numbers from 1 to 100. Thus, the first even number would be 2 and the last one is 100:

# i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100

# Important, there should only be 1 print statement in your console output. It should just print the final total and not every step of the calculation.

#Write your code below this row 👇

# create a variable called sum_of_even_numbers and put 0 as its initial value
# create a for loop with the range function
# create an if statement that checks if the number is an even number
# if the number is even, add that number to the sum of even numbers variable
# print sum_of_even_numbers

sum_of_even_numbers = 0

for i in range(1,101):
    if i % 2 == 0:
        sum_of_even_numbers += i

print(sum_of_even_numbers)