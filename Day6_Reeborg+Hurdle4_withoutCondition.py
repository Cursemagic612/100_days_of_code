def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turnaround():
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    
jump_counter = 0
jumped = 0
droped = 0
landed = 0

while not at_goal():
    if landed == 1 and droped == 0:
        turn_left()
        landed = 0
    elif front_is_clear() and droped == 0 and jumped == 0:
        move()
 
    elif wall_in_front() and jumped is 0 and jump_counter is 0:
        jump()
        turn_right()
        jump_counter += 1
        jumped = 1
        while wall_in_front():
            jump()
            turn_right()
            jump_counter += 1
    elif front_is_clear() and jumped is 1 and jump_counter > 0 and droped == 1:
        move()
        if jump_counter == 1:
            landed = 1
            jumped = 0
            droped = 0
        jump_counter -= 1
    elif front_is_clear() and jumped is 1 and jump_counter > 0 and droped == 0:
        move()
        turn_right()
        droped = 1
 
    elif front_is_clear():
        move()
