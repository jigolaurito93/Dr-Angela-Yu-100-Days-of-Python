print(f"Welcomt to the tip calculator")
total_bill = float(input(f"What was the total bill? $"))
percentage = int(input(f"What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input(f"How many people to split the bill? "))

the_tip = total_bill * (percentage/100)
overall_bill = the_tip + total_bill
each_person = overall_bill / people



print(f"Each person should pay: ${round(each_person,2)}")

                 