def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
safe_to_turn = False
stopEngines = False

def safely_go_UP():
    if stopEngines != True: 
        turn_left()
        move()
        turn_right()
        if wall_in_front():
            safe_to_turn = False
        else:
            move()
            turn_right()
            safely_go_DOWN()
            stopEngines = True
            safe_to_turn = True
    else: 
        return

def safely_go_DOWN():
    while not wall_in_front():
        move()
    else: 
        turn_left()
        while not at_goal():
            if wall_in_front():    
                safely_go_UP()
            else:
                while not wall_in_front() and not at_goal():
                    move()
                else: 
                    safely_go_UP()
        else: 
            return
        
def start(): 
    while not wall_in_front():
        move()
    else: 
        while safe_to_turn == False and stopEngines == False:
            safely_go_UP()
        else: 
            return

while not at_goal():
    if stopEngines != True: 
        start()
    else: 
        break
        
    
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
