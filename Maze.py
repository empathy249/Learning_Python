def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def u_turn():
    turn_left()
    turn_left()
    
def wall_on_left():
    u_turn()
    value = wall_on_right()
    u_turn()
    return value

def right_is_clear():
    turn_right()
    value = front_is_clear()
    turn_left()
    return value

def left_is_clear():
    turn_left()
    value = front_is_clear()
    turn_right()
    return value

def wall_on_left(): 
    turn_left()
    value = wall_in_front()
    turn_right()
    return value

while not at_goal(): 
    if right_is_clear():
        turn_right()
        while front_is_clear():
            move()
    elif wall_on_right() and wall_on_left() and front_is_clear():
        move()
    elif left_is_clear():
        turn_left()
        move()
    else: 
        u_turn()
    
        


################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
