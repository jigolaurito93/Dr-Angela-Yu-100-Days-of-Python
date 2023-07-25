import random 
import pi_module

random_integer = random.randint(1,10)

# print(random_integer)
# print(pi_module.pi)

random_float = random.random()
random_float = random_float*5

love_score = random.randint(1,100)
print(f"Your love score is {love_score}.")
print(f"{round(random_float, 2)}%")
