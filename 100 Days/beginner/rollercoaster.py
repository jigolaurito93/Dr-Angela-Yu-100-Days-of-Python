print(f"Welcom to the rollercoaster")
height = int(input("What is your height in cm? "))

if height >= 120:
    print(f'You can ride the rollercoaster')
    age = int(input("What is your age? "))
    if age < 12:
        u12 = 5
        photo = input(f'Do you want a photo? Y or N ? ')
        photo = photo.upper()
        if photo == 'Y':
            print(f'Your total is {3 + u12}')
        else:
            print(f'Your total is {u12}')
    elif age >=12 and age <18:
        middle = 7
        photo = input(f'Do you want a photo? Y or N ? ')
        photo = photo.upper()
        if photo == 'Y':
            print(f'Your total is {3 + middle}')
        else:
            print(f'Your total is {middle}')
    else:
        adult = 12
        photo = input(f'Do you want a photo? Y or N ? ')
        photo = photo.upper()
        if photo == 'Y':
            print(f'Your total is {3 + adult}')
        else:
            print(f'Your total is {adult}')
else:
    print(f'Sorry you cant ride the rollercoaster')

