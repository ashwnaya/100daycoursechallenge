def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    

while True:
    jump()
    if at_goal():
        break
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
