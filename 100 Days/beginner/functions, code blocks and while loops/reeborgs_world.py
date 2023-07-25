def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
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