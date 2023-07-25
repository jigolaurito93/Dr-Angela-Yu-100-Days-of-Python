# Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.

# Based on a user's order, work out their final bill.

# Small Pizza: $15

# Medium Pizza: $20

# Large Pizza: $25

# Pepperoni for Small Pizza: +$2

# Pepperoni for Medium or Large Pizza: +$3

# Extra cheese for any size pizza: + $1

# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

size = size.upper()
add_pepperoni = add_pepperoni.upper()
extra_cheese = extra_cheese.upper()


total = 0
if size == 'S':
    total += 15
    if add_pepperoni == 'Y':
        total += 2
elif size == 'M':
    total += 20
    if add_pepperoni == 'Y':
        total += 3
elif size == 'L':
    total += 25
    if add_pepperoni == 'Y':
        total += 3

if extra_cheese == 'Y':
    total += 1
print(f"Your final bill is ${total}.")
